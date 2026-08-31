import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                database="e_library_system",
                user="olk",
                password="0811"
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Connected to MySQL!")
        except Error as e:
            print(f"Error: {e}")
            return None

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connection closed")