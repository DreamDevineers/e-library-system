import os
from pathlib import Path
from urllib.parse import urlparse
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def _get_connection_params(self):
        database_url = os.getenv("DATABASE_URL") or os.getenv("MYSQL_URL")

        if database_url:
            parsed = urlparse(database_url)
            return {
                "host": parsed.hostname or "localhost",
                "port": parsed.port or 3306,
                "user": parsed.username or "root",
                "password": parsed.password or "",
                "database": parsed.path.lstrip("/") if parsed.path else "e_library_system",
            }

        return {
            "host": os.getenv("DB_HOST", os.getenv("MYSQLHOST", "localhost")),
            "port": int(os.getenv("DB_PORT", os.getenv("MYSQLPORT", 3306))),
            "user": os.getenv("DB_USER", os.getenv("MYSQLUSER", "root")),
            "password": os.getenv("DB_PASSWORD", os.getenv("MYSQLPASSWORD", "")),
            "database": os.getenv("DB_NAME", os.getenv("MYSQLDATABASE", "e_library_system")),
        }

    def connect(self):
        params = self._get_connection_params()
        db_name = params["database"]

        try:
            # First try connecting directly to the specified database
            try:
                self.connection = mysql.connector.connect(**params)
            except Error:
                # If database does not exist yet, connect without db and create it
                temp_params = {k: v for k, v in params.items() if k != "database"}
                temp_conn = mysql.connector.connect(**temp_params)
                temp_cursor = temp_conn.cursor()
                temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
                temp_cursor.close()
                temp_conn.close()

                self.connection = mysql.connector.connect(**params)

            self._init_tables()
            self.cursor = self.connection.cursor(dictionary=True)
            return self.connection

        except Error as e:
            print(f"Database connection error: {e}")
            return None

    def _init_tables(self):
        sql_file = Path(__file__).parent / "create_tables.sql"
        if not sql_file.exists():
            return

        with open(sql_file, "r") as file:
            sql_script = file.read()

        cursor = self.connection.cursor()
        for statement in sql_script.split(";"):
            statement = statement.strip()
            if statement:
                try:
                    cursor.execute(statement)
                except Error as err:
                    print(f"Error executing statement: {err}")

        self.connection.commit()
        cursor.close()

    def close(self):
        if self.connection and self.connection.is_connected():
            if self.cursor:
                self.cursor.close()
            self.connection.close()
