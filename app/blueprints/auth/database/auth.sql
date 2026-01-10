CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    reset_token TEXT,
    reset_token_expiration TIMESTAMP
);

INSERT OR IGNORE INTO users (username, email, password)
VALUES ("admin", "admin@marki.com", "admin123");