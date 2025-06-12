import sqlite3

def show_users():
    conn = sqlite3.connect("momo.db")
    cur = conn.cursor()
    for row in cur.execute("SELECT * FROM users"):
        print(row)
    conn.close()

def show_transactions():
    conn = sqlite3.connect("momo.db")
    cur = conn.cursor()
    for row in cur.execute("SELECT * FROM transactions"):
        print(row)
    conn.close()

