import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
                    dbname = "car_scrap",
                    user = "postgres",
                    password = "naman",
                    host = "localhost",
                    port = 5432
        )
        print("Successfully connected to the database")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
    
connect_db()