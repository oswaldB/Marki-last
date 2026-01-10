import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        reset_token TEXT,
        reset_token_expiration TIMESTAMP
    )''')
    # Ajout d'un utilisateur admin (optionnel)
    default_password = generate_password_hash("admin123")
    c.execute('''INSERT OR IGNORE INTO users (username, email, password)
              VALUES (?, ?, ?)''', ("admin", "admin@marki.com", default_password))
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('''SELECT id, username, email, password FROM users WHERE username = ?''', (username,))
    user_data = c.fetchone()
    conn.close()
    return user_data

def update_password(email, new_password):
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    hashed_password = generate_password_hash(new_password)
    c.execute('''UPDATE users SET password = ? WHERE email = ?''', (hashed_password, email))
    conn.commit()
    conn.close()