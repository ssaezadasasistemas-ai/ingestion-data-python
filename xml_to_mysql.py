import xml.etree.ElementTree as ET
import pymysql
from pathlib import Path

xml_path = Path.cwd() / "employees.xml"

def extract():
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return root.findall("employee")

def transform(elements):
    data = []

    for emp in elements:
        data.append((
            int(emp.find("empid").text),
            emp.find("name").text.strip(),
            emp.find("phone").text.strip()
        ))

    return data

def load(data):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="myempdb",
        port=3306
    )

    cursor = connection.cursor()

    try:
        cursor.execute("TRUNCATE TABLE emptable")

        insert_sql = """
            INSERT INTO emptable (empid, name, phone)
            VALUES (%s, %s, %s)
        """

        cursor.executemany(insert_sql, data)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"ETL failed: {e}")
        raise

    finally:
        cursor.close()
        connection.close()


def main():
    employees = extract()
    clean_data = transform(employees)
    load(clean_data)
    print("XML ETL finished successfully")

if __name__ == "__main__":
    main()
