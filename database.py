import sqlite3

def create_database():
    conn = sqlite3.connect("duty.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS duties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        officer_name TEXT NOT NULL,
        duty_location TEXT NOT NULL,
        duty_date TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_duty(officer_name, duty_location, duty_date):
    conn = sqlite3.connect("duty.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO duties (officer_name, duty_location, duty_date) VALUES (?, ?, ?)",
        (officer_name, duty_location, duty_date)
    )

    conn.commit()
    conn.close()


def view_duties():
    conn = sqlite3.connect("duty.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM duties")

    duties = cursor.fetchall()

    conn.close()

    return duties