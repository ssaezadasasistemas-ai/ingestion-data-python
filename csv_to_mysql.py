import csv
import pymysql

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "etl_demo",
    "port": 3306
}

def extract():
    with open("employees.csv", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def transform(data):
    for row in data:
        row["email"] = row["email"].lower()
        row["salary"] = float(row["salary"])
    return data

def load(data):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    sql = """
        INSERT INTO employees (name, email, salary)
        VALUES (%s, %s, %s)
    """

    for row in data:
        cursor.execute(sql, (row["name"], row["email"], row["salary"]))

    connection.commit()
    cursor.close()
    connection.close()

def main():
    data = extract()
    data = transform(data)
    load(data)
    print("ETL finished successfully")

if __name__ == "__main__":
    main()
