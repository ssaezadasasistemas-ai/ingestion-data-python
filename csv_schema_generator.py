import pandas as pd
import mysql.connector

CSV_FILE = "employees_auto.csv"
TABLE_NAME = "employees_auto"
DATABASE = "auto_schema_db"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": DATABASE
}

def infer_mysql_type(series: pd.Series) -> str:
    if pd.api.types.is_integer_dtype(series):
        return "INT"
    if pd.api.types.is_float_dtype(series):
        return "DECIMAL(10,2)"
    if pd.api.types.is_bool_dtype(series):
        return "BOOLEAN"
    if pd.api.types.is_datetime64_any_dtype(series):
        return "DATETIME"
    return "VARCHAR(255)"

def generate_create_table_sql(df: pd.DataFrame) -> str:
    columns_sql = []

    for column in df.columns:
        mysql_type = infer_mysql_type(df[column])
        columns_sql.append(f"`{column}` {mysql_type}")

    columns_definition = ",\n  ".join(columns_sql)

    return f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
      {columns_definition}
    );
    """

def create_database_if_not_exists(cursor):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
    cursor.execute(f"USE {DATABASE}")

def main():
    df = pd.read_csv(CSV_FILE, parse_dates=True)

    create_sql = generate_create_table_sql(df)
    print("Generated SQL:")
    print(create_sql)

    connection = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor = connection.cursor()

    create_database_if_not_exists(cursor)
    cursor.execute(create_sql)

    connection.commit()
    cursor.close()
    connection.close()

    print("Schema created successfully ✅")

if __name__ == "__main__":
    main()
