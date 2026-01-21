# URL Shortener Application
A robust and lightweight full-stack web application designed to shorten long URLs into concise, shareable links. Built with **Flask** and **SQLAlchemy**, this project features a modular architecture, persistent data storage, URL validation, and usage analytics (visit tracking).

## Features
- **Secure URL Shortening:** Generates unique, URL-safe short codes using Python's `secrets` library to prevent collisions.

- **Data Persistence:** Uses SQLite to store original URLs, short codes, and timestamps.

- **Analytics:** Tracks the number of clicks (visits) for every shortened link.

- **Duplicate Prevention:** Checks the database before creating a new entry; if a URL was already shortened, it returns the existing code to optimize storage.

- **Input Validation:** Validates URL formatting server-side to prevent errors and ensure data integrity.

- **History Dashboard:** A dedicated page to view the history of all shortened links and their performance stats.

- **Responsive UI:** Built with **Bootstrap 5** and custom CSS for a modern, mobile-friendly interface with "Copy to Clipboard" functionality.

---

## Tech Stack
- **Backend:** Python 3, Flask (Microframework)

- **Database:** SQLite, SQLAlchemy (ORM)

- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript

- **Templating:** Jinja2

---

## Project Structure
This project follows a modular **Model-View-Controller (MVC)** adaptation to ensure code maintainability and scalability.

```
Flask-Project
├── static/
│   └── custom_style.css    # Custom styling overrides
├── templates/
│   ├── base.html           # Master layout (Navbar, CDN links)
│   ├── index.html          # Home page (Input form & Result)
│   └── history.html        # History page (Data table)
├── app.py                  # Application entry point & Routes
├── extensions.py           # Database instance initialization
├── models.py               # Database Schema (Table definitions)
└── README.md

```

---

## How to run the Application
- Navigate to your local **Flask-Project** folder (where `app.py` is), and open **Command Prompt** in that folder. Create a **virtual environment** :
  ```
  python -m venv venv  
  ```
- Activate the **virtual environment** :
  ```
  venv\Scripts\activate
  ```
- Install required dependencies : **Flask**, **Flask-SQLAlchemy**, and **validators**
  ```
  pip install flask flask-sqlalchemy validators
  ```
- Run the app :
  ```
  python app.py
  ```
- Open your browser and go to :
  ```
  http://127.0.0.1:5000
  ```
  **Note:** The database (`instance/vault.db`) will be automatically created the first time you run the application.

---

## Usage Guide
- **Shorten a Link:** Navigate to the home page, paste a long URL (e.g., `https://mail.google.com/mail/u/1/#inbox`), and click **Shorten URL**.

- **Copy & Share:** Click the **Copy** button to grab your new short link.

- **Track Visits:** Go to the **History** page to see a list of all shortened URLs and how many times they have been accessed.

---

## Security & Optimization
- **SQL Injection Protection:** Utilizes SQLAlchemy ORM to handle database queries securely.

- **XSS Protection:** Jinja2 templates auto-escape output to prevent Cross-Site Scripting.

- **Modular Code:** Database models and extensions are separated from the main application logic to prevent circular imports.

---

## App Screenshots

- ### Home Page:

<img width="1919" height="1032" alt="Homepage-1" src="https://github.com/user-attachments/assets/133ab215-2f05-416b-9bf2-bd86751de1ab" />


- ### "Shortened URL" Page:

<img width="1919" height="1032" alt="Homepage-2" src="https://github.com/user-attachments/assets/7c1e9d2a-0704-4de0-9d0d-0d3696a7a0c2" />


- ### History Page:
<img width="1919" height="1032" alt="History" src="https://github.com/user-attachments/assets/7487892b-965f-43b3-aa24-8b746246e65f" />

---
