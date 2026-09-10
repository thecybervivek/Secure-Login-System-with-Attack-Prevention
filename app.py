from datetime import datetime, timedelta, timezone
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "CHANGE_THIS_BEFORE_DEPLOYMENT"
DB = Path(__file__).with_name("users.db")

MAX_FAILED_ATTEMPTS = 5
LOCKOUT_MINUTES = 5

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            failed_attempts INTEGER NOT NULL DEFAULT 0,
            locked_until TEXT
        )
    """)
    conn.commit()
    conn.close()

def utc_now():
    return datetime.now(timezone.utc)

@app.route("/")
def home():
    return render_template("home.html", username=session.get("username"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")

        if not 3 <= len(username) <= 40:
            flash("Username must be 3–40 characters.")
        elif len(password) < 10:
            flash("Password must be at least 10 characters.")
        elif password != confirm:
            flash("Passwords do not match.")
        else:
            conn = get_db()
            try:
                conn.execute(
                    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username, generate_password_hash(password))
                )
                conn.commit()
                flash("Registration successful. Please log in.")
                return redirect(url_for("login"))
            except sqlite3.IntegrityError:
                flash("Username already exists.")
            finally:
                conn.close()

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()

        if not user:
            conn.close()
            flash("Invalid username or password.")
            return render_template("login.html")

        if user["locked_until"]:
            try:
                locked_until = datetime.fromisoformat(user["locked_until"])
                if utc_now() < locked_until:
                    remaining = max(1, int((locked_until - utc_now()).total_seconds() / 60) + 1)
                    conn.close()
                    flash(f"Account temporarily locked. Try again in about {remaining} minute(s).")
                    return render_template("login.html")
            except ValueError:
                pass

        if check_password_hash(user["password_hash"], password):
            conn.execute(
                "UPDATE users SET failed_attempts = 0, locked_until = NULL WHERE id = ?",
                (user["id"],)
            )
            conn.commit()
            conn.close()
            session.clear()
            session["username"] = username
            return redirect(url_for("dashboard"))

        failures = user["failed_attempts"] + 1
        if failures >= MAX_FAILED_ATTEMPTS:
            lock_until = utc_now() + timedelta(minutes=LOCKOUT_MINUTES)
            conn.execute(
                "UPDATE users SET failed_attempts = 0, locked_until = ? WHERE id = ?",
                (lock_until.isoformat(), user["id"])
            )
            flash("Too many failed attempts. Account locked for 5 minutes.")
        else:
            conn.execute(
                "UPDATE users SET failed_attempts = ? WHERE id = ?",
                (failures, user["id"])
            )
            flash(f"Invalid username or password. Failed attempts: {failures}/{MAX_FAILED_ATTEMPTS}.")

        conn.commit()
        conn.close()

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["username"])

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)