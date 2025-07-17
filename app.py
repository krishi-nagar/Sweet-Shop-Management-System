from flask import Flask, request, jsonify
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

sweets_db = {}
next_sweet_id = 1 

# Helper function to generate a unique ID for new sweets
def generate_sweet_id():
    global next_sweet_id
    sweet_id = str(next_sweet_id)
    next_sweet_id += 1
    return sweet_id

# 1. Operations: Add Sweets
# Route to add a new sweet to the shop
@app.route('/sweets', methods=['POST'])
def add_sweet():

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    name = data.get('name')
    category = data.get('category')
    price = data.get('price')
    quantity = data.get('quantity')


    if not all([name, category, price is not None, quantity is not None]):
        return jsonify({"error": "Missing required fields: name, category, price, quantity"}), 400

    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        return jsonify({"error": "Price must be a number and quantity must be an integer"}), 400

    if price <= 0 or quantity < 0:
        return jsonify({"error": "Price must be positive and quantity non-negative"}), 400

    # Generate a unique ID for the new sweet
    sweet_id = generate_sweet_id()
    sweet = {
        "id": sweet_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    sweets_db[sweet_id] = sweet
    return jsonify({"message": "Sweet added successfully", "sweet": sweet}), 201

# 1. Operations: Delete Sweets
# Route to delete a sweet by its ID
@app.route('/sweets/<string:sweet_id>', methods=['DELETE'])
def delete_sweet(sweet_id):
    if sweet_id not in sweets_db:
        return jsonify({"error": "Sweet not found"}), 404
    
    deleted_sweet = sweets_db.pop(sweet_id)
    return jsonify({"message": "Sweet deleted successfully", "sweet": deleted_sweet}), 200

# 1. Operations: View Sweets
# Route to get a list of all available sweets
@app.route('/sweets', methods=['GET'])
def get_all_sweets():
    sweets_list = list(sweets_db.values())
    return jsonify(sweets_list), 200

# 2. Search & Sort Features: Search
# Route to search for sweets by name, category, or price range
@app.route('/sweets/search', methods=['GET'])
def search_sweets():

    query_name = request.args.get('name')
    query_category = request.args.get('category')
    query_min_price = request.args.get('min_price')
    query_max_price = request.args.get('max_price')

    results = []
    for sweet in sweets_db.values():
        match = True

        if query_name and query_name.lower() not in sweet['name'].lower():
            match = False

        if query_category and query_category.lower() != sweet['category'].lower():
            match = False
        
        # Check for price range
        if query_min_price:
            try:
                min_price = float(query_min_price)
                if sweet['price'] < min_price:
                    match = False
            except ValueError:
                return jsonify({"error": "min_price must be a number"}), 400
        
        if query_max_price:
            try:
                max_price = float(query_max_price)
                if sweet['price'] > max_price:
                    match = False
            except ValueError:
                return jsonify({"error": "max_price must be a number"}), 400
        
        if match:
            results.append(sweet)
    
    # Return the filtered search results
    return jsonify(results), 200

# 3. Inventory Management: Purchase Sweets
# Route to purchase a sweet, decreasing its quantity
@app.route('/sweets/purchase', methods=['POST'])
def purchase_sweet():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    sweet_id = data.get('id')
    purchase_quantity = data.get('quantity')

    # Validate required fields
    if not all([sweet_id, purchase_quantity is not None]):
        return jsonify({"error": "Missing required fields: id, quantity"}), 400
    
    # Validate quantity type
    try:
        purchase_quantity = int(purchase_quantity)
    except ValueError:
        return jsonify({"error": "Purchase quantity must be an integer"}), 400

    if purchase_quantity <= 0:
        return jsonify({"error": "Purchase quantity must be positive"}), 400

    if sweet_id not in sweets_db:
        return jsonify({"error": "Sweet not found"}), 404
    
    sweet = sweets_db[sweet_id]

    if sweet['quantity'] < purchase_quantity:
        return jsonify({"error": f"Not enough stock for {sweet['name']}. Available: {sweet['quantity']}"}), 400
    
    sweet['quantity'] -= purchase_quantity
    return jsonify({"message": "Sweet purchased successfully", "sweet": sweet}), 200

# 3. Inventory Management: Restock Sweets
# Route to restock a sweet, increasing its quantity
@app.route('/sweets/restock', methods=['POST'])
def restock_sweet():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    sweet_id = data.get('id')
    restock_quantity = data.get('quantity')

    if not all([sweet_id, restock_quantity is not None]):
        return jsonify({"error": "Missing required fields: id, quantity"}), 400
    
    # Validate quantity type
    try:
        restock_quantity = int(restock_quantity)
    except ValueError:
        return jsonify({"error": "Restock quantity must be an integer"}), 400

    if restock_quantity <= 0:
        return jsonify({"error": "Restock quantity must be positive"}), 400

    # Check if the sweet exists
    if sweet_id not in sweets_db:
        return jsonify({"error": "Sweet not found"}), 404
    
    sweet = sweets_db[sweet_id]
    sweet['quantity'] += restock_quantity
    return jsonify({"message": "Sweet restocked successfully", "sweet": sweet}), 200

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000, debug=True)
