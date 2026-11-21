import sqlite3
from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("lab_users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT)")
    hashed_pw = generate_password_hash("SenhaSuperSecreta123")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password_hash) VALUES (1, 'admin', ?)", (hashed_pw,))
    conn.commit()
    conn.close()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    conn = sqlite3.connect("lab_users.db")
    cursor = conn.cursor()

    # SEGURO: Consulta parametrizada (Prepared Statement) evita SQL Injection
    query = "SELECT username, password_hash FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[1], password):
        return f"Bem-vindo, {user[0]}!"
    return "Credenciais inválidas.", 401

if __name__ == "__main__":
    init_db()
    # SEGURO: debug desativado em ambiente exposto
    app.run(debug=False)
