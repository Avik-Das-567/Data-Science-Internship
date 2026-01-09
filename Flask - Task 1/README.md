## Task Objective:

- To Create a Flask Application that takes the **user name** in the **query parameter** from the URL and converts it to UPPER CASE and displays it on the browser.

- To create some cool functions in the Flask App:
  - **Palindrome Checker:** Reverses the username and checks whether it's Palindrome or not.

  - **Spy Name Generator:** Creates a Spy Name by generating a random 3-digit agent number, and slightly scrambling the username.

  - **Hacker (Leetspeak) Mode:** Converts text into numbers/symbols (e.g., "HELLO" → "H3LL0").

  - **Vaporwave Mode:** Spaced out, aesthetic text (e.g., "HELLO" → "H E L L O").

  - **ASCII Sum (Numerology):** Calculates the mathematical value of the username based on computer character codes.

## Folder Structure:

```
Flask_Project/
│
├── app.py
└── templates/
    └── index.html
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

## App Screenshots:

### Homepage

<img width="1480" height="989" alt="Flask_App_Screenshot" src="https://github.com/user-attachments/assets/7c189243-6966-446b-aabe-462e47a7f3ef" />

---
