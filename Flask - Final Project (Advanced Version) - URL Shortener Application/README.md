# URL Shortener Application - Advanced Version

## Project Structure

```
Flask-Project/
│
├── app.py                # Main controller (Now includes Login/Signup logic)
├── models.py             # Database models (Updated with 'User' table)
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
  pip install flask flask-sqlalchemy flask-login validators flask-login
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
