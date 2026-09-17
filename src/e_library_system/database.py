import mysql.connector
from mysql.connector import Error
from pathlib import Path


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="olk",
                password="0811"
            )

            cursor = self.connection.cursor()

            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS e_library_system"
            )

            cursor.close()
            self.connection.close()

            self.connection = mysql.connector.connect(
                host="localhost",
                database="e_library_system",
                user="olk",
                password="0811"
            )

            sql_file = Path(__file__).parent / "create_tables.sql"

            with open(sql_file, "r") as file:
                sql_script = file.read()

            cursor = self.connection.cursor()

            for statement in sql_script.split(";"):
                statement = statement.strip()

                if statement:
                    cursor.execute(statement)

            self.connection.commit()
            cursor.close()

            self.cursor = self.connection.cursor(dictionary=True)

            print("Connected to MySQL!")

        except Error as e:
            print(f"Error: {e}")
            return None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connection closed")