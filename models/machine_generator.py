import sqlite3

def generate_machines(n=10):
    conn = sqlite3.connect("scheduler.db")
    cur = conn.cursor()

    for i in range(n):
        name = f"Machine_{i+1}"
        capacity = 10  # fixed for simplicity
        available = 1  # initially all are available

        cur.execute("INSERT INTO machines (name, capacity, is_available) VALUES (?, ?, ?)",
                    (name, capacity, available))
    conn.commit()
    conn.close()
