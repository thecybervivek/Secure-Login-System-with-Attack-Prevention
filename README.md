# Task 03 — Secure Login System with Attack Prevention

IncodeVision Cyber Security Internship task implementation.

## Requirements covered
- Secure user registration and login
- Passwords stored using password hashing, not plaintext
- Login attempt tracking
- Temporary account lockout after 5 failed attempts
- Protected dashboard
- Parameterized SQL queries
- Logout/session clearing

## Run
```bash
python -m venv venv
# Windows
venv\Scripts\activate

pip install -r requirements.txt
python app.py
```
Open: `http://127.0.0.1:5000`

## Evidence to capture
1. Registration page and successful registration
2. Successful login
3. Wrong password attempts showing counter
4. 5th failed attempt showing lockout
5. Successful login after lockout expires
6. Protected dashboard

> Educational demo. For production, use a strong secret key, HTTPS, secure cookie settings, CSRF protection, external rate limiting, and a production server.