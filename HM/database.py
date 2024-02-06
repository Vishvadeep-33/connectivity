import sqlite3
db = sqlite3.connect('database.db')

cursor = db.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                ) 
""")

db.commit()

cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))
db.commit()

cursor.execute("""SELECT * FROM users""")
rows = cursor.fetchall()
for row in rows:
    print(row)

db.close()