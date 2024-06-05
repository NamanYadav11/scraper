from db.config import connect_db
import psycopg2

def create_database(cursor):
    try:
        cursor.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname = 'car_scrap'")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE car_scrap")
            print("Database 'car_scrap' created")
        else:
            print("Database 'car_scrap' already exists")
    except psycopg2.Error as e:
        print(f"Error creating database: {e}")



def input_data(data):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        create_database(cursor)
        cursor.execute("""
                 CREATE TABLE IF NOT EXISTS sample (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255),
                    mileage VARCHAR(255),
                    price VARCHAR(20)
                )
        """)
        print("Table 'data' created or already exists")

        for dat in data:
            print("naman",dat)
            cursor.execute("""
                INSERT INTO sample ( name, mileage, price)
                VALUES ( %s, %s, %s)
                """, (
                    dat['name'], dat['mileage'],
                    dat['price']
                ))
        conn.commit()
        print("data have been successfully stored in the database")

    except psycopg2.Error as e:
        print(f"Error: {e}")

   







