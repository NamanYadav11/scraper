from db.config import connect_db
import psycopg2


def insert_property(property):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        insert_query = """
            INSERT INTO sample (name, mileage, price)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (
            property['name'], property['mileage'], property['price']
        ))
        conn.commit()
        print("Data added successfully!")

    except Exception as error:
        print(f"Error inserting property: {error}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def delete_property(sr):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        delete_query = """
            DELETE FROM sample
            WHERE id = %s
        """
        print(f"Executing query: {delete_query} with sr={sr}")
        cursor.execute(delete_query, (sr,))
        conn.commit()

        row_count = cursor.rowcount
        if row_count > 0:
            print(f"{row_count} row(s) deleted successfully.")
        else:
            print("No rows found matching the deletion criteria.")

    except Exception as error:
        print(f"Error deleting property: {error}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def update_property(property):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        update_query = """
            UPDATE sample
            SET name = %s, mileage = %s, price = %s
            WHERE id = %s
        """
        print(f"Executing query: {update_query} with values {property}")
        cursor.execute(update_query, (
            property['name'], property['mileage'], property['price'], property['sr']
        ))
        conn.commit()

        row_count = cursor.rowcount
        if row_count > 0:
            print(f"{row_count} row(s) updated successfully.")
        else:
            print("No rows found matching the update criteria.")

    except Exception as error:
        print(f"Error updating property: {error}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def read_properties():
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        select_query = """
            SELECT * FROM sample
        """
        print(f"Executing query: {select_query}")
        cursor.execute(select_query)
        properties = cursor.fetchall()
        for property in properties:
            print(property)
        return properties
      

    except Exception as error:
        print(f"Error reading properties: {error}")

    finally:
        cursor.close()
        conn.close()
