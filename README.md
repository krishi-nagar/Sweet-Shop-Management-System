# 🍬 Sweet Shop Management System

This project is a simple web-based Sweet Shop Management System built with a **Python Flask backend** and a **pure HTML/JavaScript frontend**. It allows users to manage sweet inventory, including operations like adding, deleting, viewing, searching, purchasing, and restocking sweets.

---

## 📚 Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup and Installation](#setup-and-installation)

   * [Backend Setup](#backend-setup)
   * [Frontend Setup](#frontend-setup)
4. [How to Run](#how-to-run)
5. [API Endpoints](#api-endpoints)
6. [Project Structure](#project-structure)
7. [Future Enhancements](#future-enhancements)

---

## ✅ Features

The application supports the following functionalities:

* **Add Sweets:** Add new sweets with a unique ID, name, category (e.g., chocolate, candy, pastry), price, and quantity.
* **Delete Sweets:** Remove sweets from the shop using their unique ID.
* **View Sweets:** Display all available sweets with full details.
* **Search Sweets:** Search by name, category, or within a specific price range.
* **Purchase Sweets:** Buy sweets, reducing stock only if sufficient quantity is available.
* **Restock Sweets:** Increase stock for existing sweets.

---

## 🛠 Technologies Used

### Backend:

* Python 3.x
* Flask
* Flask-CORS

### Frontend:

* HTML5
* CSS3 (Tailwind CSS)
* JavaScript (ES6+)

---

## ⚙️ Setup and Installation

### 🔹 Backend Setup

1. **Create the main application file**
   Save the Python code into `app.py`.

2. **Create a Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   * **Windows:**

     ```bash
     .\venv\Scripts\activate
     ```
   * **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install Flask Flask-Cors
   ```

---

### 🔹 Frontend Setup

1. **Create the HTML file**
   Save your HTML/JavaScript frontend code in `index.html`.
   You may keep it in the same directory or in a `frontend/` folder.

---

## 🚀 How to Run

### 1. Start the Backend Server

* Navigate to the directory with `app.py`, activate the virtual environment, then run:

  ```bash
  python app.py
  ```

* This will start the Flask server on:
  `http://127.0.0.1:5000/`

### 2. Open the Frontend

* Double-click `index.html` or open it manually in your browser.
* It will connect to the Flask backend automatically.

---

## 🔌 API Endpoints

| Method | Endpoint             | Description                     |
| ------ | -------------------- | ------------------------------- |
| POST   | `/sweets`            | Add a new sweet                 |
| GET    | `/sweets`            | Retrieve all sweets             |
| DELETE | `/sweets/<sweet_id>` | Delete sweet by ID              |
| GET    | `/sweets/search`     | Search sweets by filters        |
| POST   | `/sweets/purchase`   | Purchase a sweet (reduce stock) |
| POST   | `/sweets/restock`    | Restock existing sweet          |

### Sample Request Bodies:

* **Add Sweet**

  ```json
  {
    "name": "Ladoo",
    "category": "Traditional",
    "price": 25.0,
    "quantity": 100
  }
  ```

* **Purchase Sweet**

  ```json
  {
    "id": "12345",
    "quantity": 5
  }
  ```

* **Restock Sweet**

  ```json
  {
    "id": "12345",
    "quantity": 50
  }
  ```

* **Search Parameters (Query):**

  ```
  ?name=Ladoo&category=Traditional&min_price=10&max_price=50
  ```

---

## 🗂 Project Structure

```
sweet-shop/
├── app.py              # Flask backend server
├── index.html          # Frontend HTML/JS
└── venv/               # Python virtual environment
```

---

## 🔮 Future Enhancements

* **Persistence Layer:**
  Integrate a database (e.g., SQLite, PostgreSQL) to save sweet data permanently.

* **Authentication System:**
  Add user login/registration and roles (e.g., admin, cashier).

* **Enhanced UI/UX:**
  Use frameworks (e.g., React or Vue) or improve Tailwind design components.

* **Testing:**
  Implement unit and integration tests using `pytest` or `unittest`.

* **Deployment:**
  Deploy on platforms like Heroku, AWS, or Render.

* **Edit Sweets:**
  Add functionality to update sweet details (e.g., name, category, price).

