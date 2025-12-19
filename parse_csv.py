import csv
import pathlib
import mysql.connector

csv_path = pathlib.Path.cwd() / "data.csv"

rows = []

with csv_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        rows.append((
            int(row[0]),
            row[1],
            row[2]
        ))

# 1️⃣ Conexión SIN base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS myempdb")
cursor.close()
connection.close()

# 2️⃣ Conexión CON base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="myempdb"
)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS emptable (
        empid INT PRIMARY KEY,
        name VARCHAR(255),
        phone VARCHAR(50)
    )
""")

insert_sql = """
    INSERT INTO emptable (empid, name, phone)
    VALUES (%s, %s, %s)
"""

cursor.executemany(insert_sql, rows)

connection.commit()

cursor.execute("SELECT * FROM emptable")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
