# Secure Login System with Attack Prevention

A Flask-based secure authentication system developed as part of the **IncodeVision Cyber Security Internship – Task 03**.

The project demonstrates secure user registration and login with password hashing, session-based authentication, brute-force protection, and temporary account lockout.

---

## 🚀 Live Demo

🔗 **Live Application:**  
https://secure-login-system-with-attack.onrender.com

> **Note:** The application is hosted on Render's free instance. After a period of inactivity, the first request may take a few seconds to respond.

---

## 📌 Project Objective

To develop a secure registration and login system that protects user credentials and prevents common authentication attacks such as brute-force password attempts.

---

## 🔐 Security Features

- Secure user registration
- Password hashing using Werkzeug
- Passwords are never stored in plaintext
- Minimum password length validation
- Session-based authentication
- Protected dashboard
- Failed login attempt tracking
- Brute-force attack prevention
- Temporary account lockout after multiple failed attempts
- Parameterized SQL queries
- Secure logout and session clearing
- SQLite database for user data

---

## 🛡️ Brute-Force Protection

The system tracks failed login attempts for each user.

### Lockout Policy

- Maximum failed attempts: **5**
- After 5 consecutive failed attempts:
  - Account is temporarily locked
  - Lockout duration: **5 minutes**
- Correct credentials cannot be used during the lockout period
- After the lockout expires, the user can attempt to log in again

This mechanism helps reduce the risk of automated brute-force attacks.

---

## 🧰 Technologies Used

- **Python 3**
- **Flask**
- **SQLite**
- **Werkzeug**
- **HTML5**
- **CSS3**
- **Jinja2**
- **Gunicorn**

---

## 📂 Project Structure

```text
Secure-Login-System-with-Attack-Prevention/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    ├── base.html
    ├── home.html
    ├── login.html
    ├── register.html
    └── dashboard.html
