import sqlite3

def add_user(name, phone):
    conn = sqlite3.connect("momo.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()

def add_transaction(user_id, t_type, amount):
    conn = sqlite3.connect("momo.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions (user_id, type, amount) VALUES (?, ?, ?)",
        (user_id, t_type, amount)
    )
    conn.commit()
    conn.close()

