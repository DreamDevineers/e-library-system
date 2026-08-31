from e_library_system.database.connection import get_connection


connection = get_connection()

print("Connected to MySQL!")

connection.close()