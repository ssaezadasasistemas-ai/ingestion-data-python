import requests
import mysql.connector
from mysql.connector import Error

# -------------------------
# CONFIG
# -------------------------
POKEMON_LIST_URL = "https://pokeapi.co/api/v2/pokemon?limit=50"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "pokemon_db"
}

# -------------------------
# EXTRACT
# -------------------------
def get_pokemon_list():
    response = requests.get(POKEMON_LIST_URL)
    response.raise_for_status()
    return response.json()["results"]

def get_pokemon_details(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# -------------------------
# TRANSFORM
# -------------------------
def transform_pokemon(pokemon_json):
    return {
        "id": pokemon_json["id"],
        "name": pokemon_json["name"],
        "height": pokemon_json["height"],
        "weight": pokemon_json["weight"],
        "base_experience": pokemon_json["base_experience"]
    }

# -------------------------
# LOAD
# -------------------------
def create_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"[DB ERROR] {e}")
        return None

def insert_pokemon(connection, pokemon):
    sql = """
    INSERT INTO pokemon (id, name, height, weight, base_experience)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        height = VALUES(height),
        weight = VALUES(weight),
        base_experience = VALUES(base_experience)
    """
    cursor = connection.cursor()
    cursor.execute(sql, (
        pokemon["id"],
        pokemon["name"],
        pokemon["height"],
        pokemon["weight"],
        pokemon["base_experience"]
    ))

# -------------------------
# PIPELINE
# -------------------------
def run_pipeline():
    print("Fetching Pokémon list...")
    pokemon_list = get_pokemon_list()

    connection = create_connection()
    if not connection:
        return

    for pokemon in pokemon_list:
        details = get_pokemon_details(pokemon["url"])
        pokemon_data = transform_pokemon(details)
        insert_pokemon(connection, pokemon_data)
        print(f"Inserted {pokemon_data['name']}")

    connection.commit()
    connection.close()
    print("ETL finished successfully ✅")

if __name__ == "__main__":
    run_pipeline()
