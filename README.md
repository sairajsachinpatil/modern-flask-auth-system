# 🔐 Modern Flask Authentication System

A modern authentication system built using **Flask**, **SQLite**, and **Werkzeug Security**.

This project demonstrates secure user authentication with password hashing, session management, route protection, and a clean responsive user interface.

---

## ✨ Features

### Authentication

* User Registration
* User Login
* Secure Password Hashing
* Session Management
* Logout Functionality
* Dashboard Protection

### User Interface

* Modern Login Page
* Modern Signup Page
* Password Visibility Toggle
* Responsive Design
* Social Login UI Buttons
* Forgot Password Page
* Privacy Policy Page

### Security

* Password Hashing using Werkzeug
* SQLite Database Storage
* Session-based Authentication
* Unique Email Validation

---

## 📸 Screens

* Login Page
* Signup Page
* Dashboard
* Privacy Policy
* Forgot Password

---

## 🛠 Tech Stack

| Technology | Purpose                |
| ---------- | ---------------------- |
| Flask      | Backend Framework      |
| SQLite     | Database               |
| Werkzeug   | Password Hashing       |
| HTML5      | Frontend               |
| CSS3       | Styling                |
| JavaScript | Client-side Validation |

---

## 📂 Project Structure

```text
modern-flask-auth-system/
│
├── app.py
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── forgot_password.html
│   ├── privacy.html
│   └── terms.html
│
├── static/
│   └── logo.png
│
├── database.db
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/sairajsachinpatil/modern-flask-auth-system.git

cd modern-flask-auth-system
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask werkzeug
```

### Run Application

```bash
python app.py
```

Application will run on:

```text
http://127.0.0.1:5000
```

---

## 🗄 Database Schema

### Users Table

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```

---

## 🔑 Authentication Flow

### Signup

1. User enters Full Name, Email and Password
2. Password is hashed using Werkzeug
3. User record is stored in SQLite
4. User is automatically logged in
5. Redirected to Dashboard

### Login

1. User enters Email and Password
2. Password hash is verified
3. Session is created
4. Redirected to Dashboard

### Dashboard Access

Only authenticated users can access:

```text
/dashboard
```

### Logout

Session is destroyed and user is redirected to login page.

---

## 🔒 Security Features

* Hashed Password Storage
* Session Authentication
* Route Protection
* Unique Email Constraint
* Server-side Validation

---

## 🚀 Future Improvements

* Email Verification
* Password Reset via Email
* JWT Authentication
* Google OAuth Login
* GitHub OAuth Login
* User Profile Management
* Remember Me Functionality
* Two Factor Authentication (2FA)

---

## 🎯 Learning Outcomes

This project helps understand:

* Flask Routing
* User Authentication
* Session Management
* SQLite Database Operations
* Password Hashing
* Form Handling
* Frontend Validation

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create Pull Request

---

## 👨‍💻 Author

### Sairaj Sachin Patil

* GitHub: https://github.com/sairajsachinpatil

---

⭐ If you found this project useful, please consider giving it a star.
