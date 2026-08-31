import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MartG09@Meg",
        database="e_library"
    )

    return connection
