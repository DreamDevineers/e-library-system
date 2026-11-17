from uuid import UUID

from e_library_system.database import Database
from e_library_system.models.book import Book, BookCategory, BookStatus
from e_library_system.repositories.book_repository import BookRepository


class BookRepositoryImpl(BookRepository):
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def add_book(self, book: Book) -> Book:
        query = """
                INSERT INTO books(id, title, author, isbn, category, status, year)
                VALUES(%s, %s, %s, %s, %s, %s, %s)
                """

        values = (
            str(book.id),
            book.title,
            book.author,
            book.isbn,
            book.category.value if hasattr(book.category, "value") else str(book.category),
            book.status.value if hasattr(book.status, "value") else str(book.status),
            book.year,
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

        return book

    def get_by_id(self, book_id: UUID):
        query = "SELECT * FROM books WHERE id = %s"
        self.db.cursor.execute(query, (str(book_id),))
        row = self.db.cursor.fetchone()

        if row:
            return self._map_row(row)

        return None

    def get_all(self) -> list[Book]:
        query = "SELECT * FROM books"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchall()

        return [self._map_row(row) for row in result]

    def update_book(self, book: Book) -> Book:
        query = """
                UPDATE books
                SET title = %s,
                    author = %s,
                    isbn = %s,
                    category = %s,
                    status = %s,
                    year = %s
                WHERE id = %s
                """

        values = (
            book.title,
            book.author,
            book.isbn,
            book.category.value if hasattr(book.category, "value") else str(book.category),
            book.status.value if hasattr(book.status, "value") else str(book.status),
            book.year,
            str(book.id),
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

        return self.get_by_id(book.id)

    def delete_book(self, book_id: UUID):
        query = "DELETE FROM books WHERE id = %s"

        self.db.cursor.execute(query, (str(book_id),))
        self.db.connection.commit()

        return self.db.cursor.rowcount > 0

    def get_available(self) -> list[Book]:
        query = "SELECT * FROM books WHERE status = %s"

        self.db.cursor.execute(
            query,
            (BookStatus.AVAILABLE.value,)
        )

        results = self.db.cursor.fetchall()
        return [self._map_row(row) for row in results]

    def _map_row(self, row: dict) -> Book:
        return Book(
            id=UUID(row["id"]),
            title=row["title"],
            author=row["author"],
            isbn=row["isbn"],
            category=BookCategory(row["category"]),
            status=BookStatus(row["status"]),
            year=int(row["year"]),
        )
