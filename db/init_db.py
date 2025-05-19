import sqlite3

def init_db():
    conn = sqlite3.connect("scheduler.db")
    cur = conn.cursor()

    # Drop if exists
    cur.execute("DROP TABLE IF EXISTS jobs")
    cur.execute("DROP TABLE IF EXISTS machines")

    # Jobs Table
    cur.execute("""
    CREATE TABLE jobs (
        id INTEGER PRIMARY KEY,
        name TEXT,
        duration INTEGER,
        deadline INTEGER,
        energy_required REAL
    )
    """)

    # Machines Table
    cur.execute("""
    CREATE TABLE machines (
        id INTEGER PRIMARY KEY,
        name TEXT,
        capacity INTEGER,
        is_available INTEGER
    )
    """)

    conn.commit()
    conn.close()
