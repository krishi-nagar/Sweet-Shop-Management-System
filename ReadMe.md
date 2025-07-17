Sweet Shop Management System
This project implements a simple Sweet Shop Management System with a Python Flask backend and a pure HTML/JavaScript frontend. It allows users to manage sweet inventory, including adding, deleting, viewing, searching, purchasing, and restocking sweets.

Table of Contents
Features

Technologies Used

Setup and Installation

Backend Setup

Frontend Setup

How to Run

API Endpoints

Project Structure

Future Enhancements

Features
The application supports the following operations:

Add Sweets: Users can add new sweets to the shop with a unique ID, name, category (e.g., chocolate, candy, pastry), price, and quantity in stock.

Delete Sweets: Users can remove sweets from the shop using their unique ID.

View Sweets: Display a list of all sweets currently available in the shop, showing their details and current stock.

Search Sweets: Users can search for sweets by name, category, or within a specified price range.

Purchase Sweets: Allows users to purchase sweets, which decreases their quantity in stock. The system checks for sufficient stock before allowing a purchase.

Restock Sweets: Users can increase the quantity of stock for existing sweets.

Technologies Used
Backend:

Python 3.x

Flask (Web Framework)

Flask-CORS (for Cross-Origin Resource Sharing)

Frontend:

HTML5

CSS3 (with Tailwind CSS for utility-first styling)

JavaScript (ES6+)

Setup and Installation
Backend Setup
Clone the repository (if applicable) or create the app.py file:
Save the Python code provided earlier into a file named app.py.

Create a Virtual Environment (Recommended):
It's good practice to use a virtual environment to manage dependencies.

python -m venv venv

Activate the Virtual Environment:

Windows:

.\venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

Install Dependencies:
With your virtual environment activated, install Flask and Flask-CORS:

pip install Flask Flask-Cors

Frontend Setup
Create the index.html file:
Save the HTML/JavaScript code provided earlier into a file named index.html. You can place it in the same directory as app.py or in a separate frontend folder.

How to Run
Start the Backend Server:
Open your terminal or command prompt, navigate to the directory containing app.py, activate your virtual environment (if you created one), and run:

python app.py

The Flask server will start, typically running on http://127.0.0.1:5000/. Keep this terminal window open.

Open the Frontend in Your Browser:
Navigate to the index.html file in your file explorer and double-click it to open it in your preferred web browser.

The frontend will automatically connect to the running Flask backend to fetch and manage sweet data.

API Endpoints
The Flask backend exposes the following API endpoints:

POST /sweets: Add a new sweet.

Body: {"name": "string", "category": "string", "price": float, "quantity": int}

GET /sweets: Get all sweets.

DELETE /sweets/<sweet_id>: Delete a sweet by ID.

GET /sweets/search: Search sweets.

Query Params: name=string, category=string, min_price=float, max_price=float (any combination)

POST /sweets/purchase: Purchase a sweet.

Body: {"id": "string", "quantity": int}

POST /sweets/restock: Restock a sweet.

Body: {"id": "string", "quantity": int}

Project Structure
.
├── app.py              # Python Flask Backend
├── index.html          # HTML/JavaScript Frontend
└── venv/               # Python Virtual Environment (if created)

Future Enhancements
Persistence: Integrate a real database (e.g., SQLite, PostgreSQL, MongoDB) instead of in-memory storage, so data isn't lost when the server restarts.

User Authentication: Add user login/registration and role-based access control.

Improved UI/UX: Enhance the frontend design, add more interactive elements, and better error displays.

Testing: Implement unit and integration tests for both frontend and backend (following TDD principles as mentioned in the project objective).

Deployment: Set up the application for deployment to a cloud platform (e.g., Heroku, AWS, Google Cloud).

Update Sweet Details: Add functionality to update existing sweet information (name, category, price).