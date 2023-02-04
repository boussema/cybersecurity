import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "john123", hashlib.sha256("johnpassword".encode()).hexdigest()
username2, password2 = "alex", hashlib.sha256("greatcat111".encode()).hexdigest()
username3, password3 = "neuraline", hashlib.sha256("neuralpassword".encode()).hexdigest()
username4, password4 = "tester147", hashlib.sha256("ilikeshopping".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()

