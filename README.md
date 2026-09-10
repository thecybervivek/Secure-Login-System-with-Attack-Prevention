# Secure Login System with Attack Prevention

A Flask-based secure authentication system developed as part of the IncodeVision Cyber Security Internship – Task 03.

## Live Demo

Live Application: https://secure-login-system-with-attack.onrender.com

Note: The application is hosted on Render's free instance, so the first request may take some time after inactivity.

## Project Objective

The objective of this project is to develop a secure registration and login system that protects user credentials and prevents common authentication attacks such as brute-force attacks.

## Features

- Secure user registration
- Secure login authentication
- Password hashing using Werkzeug
- Passwords are not stored in plaintext
- Minimum password length validation
- Session-based authentication
- Protected dashboard
- Failed login attempt tracking
- Brute-force attack prevention
- Temporary account lockout
- Parameterized SQL queries
- Secure logout and session clearing
- SQLite database

## Brute-Force Protection

The system tracks failed login attempts for each user.

After 5 consecutive failed login attempts, the account is temporarily locked for 5 minutes.

During the lockout period:

- Login attempts are blocked
- Correct credentials cannot bypass the temporary lockout
- The user can log in again after the lockout period expires

## Technologies Used

- Python
- Flask
- SQLite
- Werkzeug
- HTML5
- CSS3
- Jinja2
- Gunicorn

## Project Structure

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

## Security Implementation

### Password Hashing

Passwords are securely hashed before being stored in the database using Werkzeug.

The application uses password hashing instead of storing passwords in plaintext.

### SQL Injection Protection

The application uses parameterized SQL queries instead of directly inserting user input into SQL statements.

### Session Authentication

Flask sessions are used to maintain authenticated user sessions and protect restricted routes.

### Account Lockout

Failed login attempts are tracked and the account is temporarily locked after repeated failed attempts.

## Testing

The following scenarios were tested:

1. User registration with a new account
2. Successful login with valid credentials
3. Failed login with incorrect credentials
4. Five consecutive failed login attempts
5. Temporary account lockout
6. Blocking login during the lockout period
7. Successful login after the lockout period
8. Redirecting unauthenticated users from the protected dashboard
9. Logout and session clearing

## Deployment

The application is deployed on Render using Gunicorn.

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

## Internship Task

Internship: Cyber Security Intern – IncodeVision

Task 03: Secure Login System with Attack Prevention

The project covers secure authentication, password hashing, login attempt limits, temporary account lockout, and brute-force attack prevention.

## Author

Vivek Sharma

Cyber Security Student & Intern

## Disclaimer

This project was developed for educational and internship purposes to demonstrate basic web authentication security and brute-force attack prevention.

Do not use the demo application with real or sensitive passwords.
