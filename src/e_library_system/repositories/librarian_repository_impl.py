from uuid import UUID
from typing import Optional

from e_library_system.models.librarian import Librarian
from e_library_system.repositories.librarian_repository import LibrarianRepository
from e_library_system.database import Database


class LibrarianRepositoryImpl(LibrarianRepository):

    def __init__(self):
        self.db = Database()
        self.db.connect()

    def save(self, librarian: Librarian) -> None:

        query = """
                INSERT INTO librarians
                (id, first_name, last_name, email, password, phone, address, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """

        values = (
            str(librarian.id),
            librarian.first_name,
            librarian.last_name,
            librarian.email,
            librarian.password,
            librarian.phone,
            librarian.address,
            librarian.created_at,
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

    def find_all(self) -> list[Librarian]:

        query = "SELECT * FROM librarians"

        self.db.cursor.execute(query)
        results = self.db.cursor.fetchall()

        librarians = []

        for row in results:
            librarians.append(self._map_row(row))

        return librarians

    def find_by_id(self, librarian_id: str) -> Optional[Librarian]:

        query = "SELECT * FROM librarians WHERE id = %s"

        self.db.cursor.execute(query, (librarian_id,))
        row = self.db.cursor.fetchone()

        if row is None:
            return None

        return self._map_row(row)

    def find_by_email(self, email: str) -> Optional[Librarian]:

        query = "SELECT * FROM librarians WHERE email = %s"

        self.db.cursor.execute(query, (email,))
        row = self.db.cursor.fetchone()

        if row is None:
            return None

        return self._map_row(row)

    def update(self, librarian_id: str, librarian: Librarian) -> None:

        query = """
                UPDATE librarians
                SET first_name = %s,
                    last_name = %s,
                    email = %s,
                    password = %s,
                    phone = %s,
                    address = %s
                WHERE id = %s
                """

        values = (
            librarian.first_name,
            librarian.last_name,
            librarian.email,
            librarian.password,
            librarian.phone,
            librarian.address,
            librarian_id,
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

    def delete(self, librarian_id: str) -> None:

        query = "DELETE FROM librarians WHERE id = %s"

        self.db.cursor.execute(query, (librarian_id,))
        self.db.connection.commit()

    def _map_row(self, row: dict) -> Librarian:
        return Librarian(
            id=UUID(row["id"]),
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=row["email"],
            password=row["password"],
            phone=row["phone"],
            address=row["address"],
            created_at=row["created_at"]
        )
