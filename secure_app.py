import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO users (id, username, password)
VALUES (1, 'test', 'test')
""")

conn.commit()

# Secure parameterized SQL query
query = "SELECT * FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()