from flask import Flask, request, jsonify
import sqlite3
import jwt
import requests
import datetime

app = Flask(__name__)

# 🔥 Weak Secret (API2)
SECRET_KEY = "secret123"

# -----------------------------
# DATABASE SETUP
# -----------------------------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT,
        balance INTEGER
    )
    """)

    cursor.execute("INSERT OR IGNORE INTO users VALUES (1,'admin','admin123','admin',10000)")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2,'arjit','password','user',500)")

    conn.commit()
    conn.close()

init_db()

# -----------------------------
# API2 - Broken Authentication (SQL Injection)
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 🔥 Vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        payload = {
            "user_id": user[0],
            "username": user[1],
            "role": user[3],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify({"message": "Login Successful", "token": token})
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# -----------------------------
# API1 - BOLA (IDOR)
# -----------------------------
@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, balance FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"id": user[0], "username": user[1], "balance": user[2]})
    else:
        return jsonify({"message": "User not found"}), 404


# -----------------------------
# API3 - Mass Assignment
# -----------------------------
@app.route("/update-profile", methods=["PUT"])
def update_profile():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"message": "Token missing"}), 401

    token = token.split(" ")[1]
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    data = request.json

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 🔥 Mass Assignment Vulnerability
    for key, value in data.items():
        cursor.execute(f"UPDATE users SET {key} = ? WHERE id = ?", (value, decoded["user_id"]))

    conn.commit()
    conn.close()

    return jsonify({"message": "Profile updated"})


# -----------------------------
# API5 - Broken Function Level Authorization
# -----------------------------
@app.route("/admin/dashboard", methods=["GET"])
def admin_dashboard():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"message": "Token missing"}), 401

    token = token.split(" ")[1]
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if decoded["role"] != "admin":
        return jsonify({"message": "Access denied"}), 403

    return jsonify({
        "message": "Welcome Admin!",
        "sensitive_data": "Database backups, financial reports"
    })


# -----------------------------
# API6 - Business Logic Flaw
# -----------------------------
@app.route("/transfer", methods=["POST"])
def transfer():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"message": "Token missing"}), 401

    token = token.split(" ")[1]
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    data = request.json
    amount = data.get("amount")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 🔥 Negative transfer allowed (Business Logic flaw)
    cursor.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (amount, decoded["user_id"]))
    conn.commit()
    conn.close()

    return jsonify({"message": "Transfer processed"})


# -----------------------------
# API7 - SSRF
# -----------------------------
@app.route("/fetch-url", methods=["POST"])
def fetch_url():
    data = request.json
    url = data.get("url")

    # 🔥 No validation (SSRF)
    response = requests.get(url)
    return jsonify({"content": response.text})


# -----------------------------
# API8 - Security Misconfiguration
# -----------------------------
@app.route("/debug-info", methods=["GET"])
def debug_info():
    # 🔥 Exposing internal information
    return jsonify({
        "secret_key": SECRET_KEY,
        "debug": True,
        "server": "Flask Development Server"
    })


# -----------------------------
# API9 - Improper Inventory Management
# -----------------------------
@app.route("/api/v1/users", methods=["GET"])
def old_api_version():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()
    conn.close()

    return jsonify({"version": "v1", "data": users})


# -----------------------------
# API10 - Unsafe Consumption of APIs
# -----------------------------
@app.route("/external-data", methods=["POST"])
def external_data():
    data = request.json
    api_url = data.get("api_url")

    # 🔥 Trusting external API blindly
    response = requests.get(api_url)
    return jsonify({"external_response": response.json()})


# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
