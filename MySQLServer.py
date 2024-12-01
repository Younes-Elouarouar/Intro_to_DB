pip install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",       # MySQL server hostname (default is localhost)
            user="root",            # MySQL username
            password="your_password"  # MySQL password (replace with your password)
        )

        cursor = connection.cursor()

        # SQL query to create the database
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        
        # Execute the query
        cursor.execute(create_db_query)

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied. Please check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
