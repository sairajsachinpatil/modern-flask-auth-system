from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

app.secret_key = "your_secret_key"


# =========================
# DATABASE CONNECTION
# =========================

def get_db_connection():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    return conn


# =========================
# CREATE USERS TABLE
# =========================

def create_table():

    conn = get_db_connection()

    conn.execute("""

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            fullname TEXT,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL

        )

    """)

    conn.commit()
    conn.close()


create_table()


# =========================
# HOME ROUTE
# =========================

@app.route("/")
def home():

    if "user" in session:

        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# =========================
# LOGIN ROUTE
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        conn = get_db_connection()

        user = conn.execute(

            "SELECT * FROM users WHERE email = ?",
            (email,)

        ).fetchone()

        conn.close()

        # CHECK PASSWORD

        if user and check_password_hash(user["password"], password):

            # CREATE SESSION

            session["user"] = email

            flash("Login Successful")

            # REDIRECT TO DASHBOARD

            return redirect(url_for("dashboard"))

        else:

            flash("Invalid Email or Password")

            return redirect(url_for("login"))

    return render_template("login.html")


# =========================
# SIGNUP ROUTE
# =========================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        fullname = request.form.get("fullname")
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)

        try:

            conn = get_db_connection()

            conn.execute(

                "INSERT INTO users (fullname, email, password) VALUES (?, ?, ?)",

                (fullname, email, hashed_password)

            )

            conn.commit()
            conn.close()

            # AUTO LOGIN AFTER SIGNUP

            session["user"] = email

            flash("Account Created Successfully")

            # REDIRECT TO DASHBOARD

            return redirect(url_for("dashboard"))

        except sqlite3.IntegrityError:

            flash("Email Already Exists")

            return redirect(url_for("signup"))

    return render_template("signup.html")


# =========================
# DASHBOARD ROUTE
# =========================



@app.route("/dashboard")
def dashboard():

    if "user" not in session:

        return redirect(url_for("signup"))

    return render_template("dashboard.html")
# =========================
# LOGOUT ROUTE
# =========================

@app.route("/logout")
def logout():

    session.pop("user", None)

    flash("Logged Out Successfully")

    return redirect(url_for("login"))


# =========================
# TERMS PAGE
# =========================

@app.route("/terms")
def terms():

    return render_template("terms.html")


# =========================
# PRIVACY POLICY PAGE
# =========================

@app.route("/privacy")
def privacy():

    return render_template("privacy.html")


# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    app.run(debug=True)