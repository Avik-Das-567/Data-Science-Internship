# URL Shortener Application - Advanced Version
A secure, full-stack web application designed to shorten URLs, track click analytics, and manage personal link history. This advanced version introduces **User Authentication** and **Session-Based Access Control**, ensuring that link data is persistent, private, and secure.

## Tech Stack

- **Backend:** Python, Flask

- **Database:** SQLite, SQLAlchemy (ORM)

- **Authentication:** Flask-Login, Werkzeug Security

- **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templating

---

## Project Structure

```
Flask-Project/
│
├── app.py                # Application entry point & Routes
├── models.py             # Database models
├── extensions.py         # Database initialization (db = SQLAlchemy)
│
├── instance/
│   └── vault.db          # SQLite Database (Auto-generated)
│
├── static/
│   └── custom_style.css  # Styling files
│
└── templates/
    ├── base.html         # Master layout
    ├── index.html        # Home page
    ├── login.html        # Login page
    └── signup.html       # Signup page
```

---
## Key Features

- **User Authentication System:**

    - **Secure Signup & Login:** complete with error handling and feedback messages.

    - **Password Hashing:** Uses `werkzeug.security` (PBKDF2/SHA256) to ensure passwords are never stored in plain text.

    - **Session Management:** Implements `Flask-Login` to manage user sessions and protect routes.

- **Advanced URL Shortening:**

    - Generates cryptographically secure, collision-resistant short codes.

    - **Duplicate Prevention:** Intelligent logic checks if a user has already shortened a specific URL, preventing redundant database entries.

- **Personalized Dashboard:**

    - **Private History:** Logged-in users view a history table containing only the links they created.

    - **Visit Tracking:** A real-time counter tracks how many times each short link is visited.

- **Strict Input Validation:**

    - **Username Rules:** Enforces constraints (unique, 5-9 characters) at the server level.

    - **URL Verification:** Validates URL formatting to prevent broken or malicious links.

- **Responsive UI:** A modern interface built with **Bootstrap 5**, featuring a dynamic navigation bar that adapts to the user's login state

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
- Install required dependencies : **Flask**, **Flask-SQLAlchemy**, **Flask-Login**, and **validators**
  ```
  pip install flask flask-sqlalchemy flask-login validators
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

- **Sign Up:** Create a secure account (Username must be 5-9 characters).

- **Login:** Authenticate to access the dashboard.

- **Shorten:** Paste any long URL into the input field to generate a short link.

- **Manage:** View your personal **History** section below the form to see your saved links and their click counts.

- **Logout:** Securely end your session via the navigation bar.

---

## Security Implementation

- **Password Hashing:** Credentials are salted and hashed using `generate_password_hash` before storage.

- **Route Protection:** The `@login_required` decorator prevents unauthorized access to the shortening and history features.

- **Data Isolation:** Database queries are filtered by `current_user.id`, ensuring users cannot access or modify each other's data.

---

## App Screenshots

- ### Signup Page:
<img width="1919" height="1033" alt="Signup Page" src="https://github.com/user-attachments/assets/b765fb5f-0152-4d22-af06-b36e37e7d30d" />

- ### Login Page:
<img width="1919" height="1032" alt="Homepage-1" src="https://github.com/user-attachments/assets/6ea32456-880b-4f1c-8e87-fbb8f3970517" />

- ### "Shorten URL" Page:
<img width="1919" height="1032" alt="Shorten URL Page" src="https://github.com/user-attachments/assets/c91fa86c-4c66-4611-8b21-11be87faa027" />

- ### "Recent Links" Page:
<img width="1919" height="1035" alt="Shorten URL Page - 2" src="https://github.com/user-attachments/assets/1dbc9ab9-ced5-43ef-90ac-3c0d864a4f27" />

---
