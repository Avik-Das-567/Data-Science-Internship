# Regex101 Clone using Flask

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)

A simple web application built with **Flask** that clones the core functionality of [regex101.com](https://regex101.com). This tool allows users to input a text string and a regular expression to identify and display all matching patterns.

## Features:

- **Regex Testing:** Input a regular expression and a test string to find matches.

- **Match Highlighting:** Displays a list of all successful matches found in the text.

- **Match Counting:** Shows the total number of matches found.

- **Error Handling:** Gracefully handles invalid regular expressions and displays helpful error messages to the user.

- **Responsive UI:** Clean and simple interface styled with custom CSS.

## Project Structure:

```
Flask_Project/
|
├── app.py              # Main Flask application logic
|
├── static/
│   └── style.css       # CSS styling for the application
|
├── templates/
│   └── index.html      # HTML template for the frontend
|
└── README.md           # Project documentation
```

## How to run the Application:

- Navigate to your local **Flask_Project** folder (where `app.py` is), and open **Command Prompt** in that folder. Create a **virtual environment** :
  ```
  python -m venv venv  
  ```
- Activate the **virtual environment** :
  ```
  venv\Scripts\activate
  ```
- Install required dependencies : **flask**
  ```
  pip install flask
  ```
- Run the app :
  ```
  python app.py
  ```
- Open your browser and go to :
  ```
  http://127.0.0.1:5000
  ```

## Usage:

- Enter your **Regular Expression** in the top input box (e.g., \d+ to find numbers).

- Enter your **Test String** in the large text area.

- Click the **Test Regex** button.

- View the matches or error messages displayed below the form.

---
