import sqlite3

connection = sqlite3.connect("tracker.db")
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO charging_sessions (date, kwh_added, cost, odometer) VALUES (?, ?, ?, ?)",
    ("2026-09-23", 39, 00.00, 106600)
)
cursor.execute(
    "INSERT INTO charging_sessions (date, kwh_added, cost, odometer) VALUES (?, ?, ?, ?)",
    ("2026-09-26", 44, 11.00, 106910)
)

cursor.execute(
    "INSERT INTO charging_sessions (date, kwh_added, cost, odometer) VALUES (?, ?, ?, ?)",
    ("2026-09-18", 62, 32.00, 105600)
)
connection.commit()

cursor.execute("SELECT * FROM charging_sessions ORDER BY date")
for row in cursor.fetchall():
    print(row)

connection.close()