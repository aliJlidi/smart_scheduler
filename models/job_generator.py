import sqlite3
import random

def generate_jobs(n=50):
    conn = sqlite3.connect("scheduler.db")
    cur = conn.cursor()

    for i in range(n):
        name = f"Job_{i+1}"
        duration = random.randint(1, 8)
        deadline = random.randint(10, 30)
        energy = round(random.uniform(0.5, 5.0), 2)

        cur.execute("INSERT INTO jobs (name, duration, deadline, energy_required) VALUES (?, ?, ?, ?)",
                    (name, duration, deadline, energy))
    conn.commit()
    conn.close()
