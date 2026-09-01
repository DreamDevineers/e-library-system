from typing import Any
from uuid import UUID

from e_library_system.database import Database
from e_library_system.models import book
from e_library_system.models.book import Book, BookStatus
from e_library_system.repositories.book_repository import BookRepository


class BookRepositoryImpl(BookRepository):
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def add_book(self,book: Book) -> Book:
        query = """ 
                INSERT INTO books(id, title, author, isbn, category, total_copies, available_copies , status)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                """

        values =(
            str(book.id),
            book.title,
            book.author,
            book.isbn,
            book.category,
            book.total_copies,
            book.available_copies,
            book.status.value
        )

        self.db.cursor.execute(query,values)
        self.db.connection.commit()

        return book

    def get_by_id(self,book_id: UUID):
        query = "SELECT * FROM books WHERE id = %s"
        self.db.cursor.execute(query,(str(book_id),))
        row = self.db.cursor.fetchone()

        if row:
            return Book (
                id = UUID(row["id"]),
                title = row["title"],
                author = row["author"],
                isbn = row["isbn"],
                category = row["category"],
                total_copies = row["total_copies"],
                available_copies = row["available_copies"],
                status = BookStatus(row["status"])
            )

        return None

    def get_all(self) -> list[Book]:
        query = "SELECT * FROM books"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchall()

        book_list = []
        for row in result:
            book_list.append(Book(
                id = UUID(row["id"]),
                title=row["title"],
                author=row["author"],
                isbn=row["isbn"],
                category=row["category"],
                total_copies=row["total_copies"],
                available_copies=row["available_copies"],
                status=BookStatus(row["status"])

            ))
        return book_list





    def update_book(self,book: Book) -> Book:
        query = """
                UPDATE books
                SET title      = %s,
                    author     = %s,
                    isbn     = %s,
                    category = %s,
                    total_copies = %s,
                    available_copies = %s,
                    status   = %s
                WHERE id = %s
                """
        values = (
            book.title,
            book.author,
            book.isbn,
            book.category,
            book.total_copies,
            book.available_copies,
            book.status.value,
            str(book.id)

        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()
        return self.get_by_id(book.id)

    def delete_book(self,book_id: UUID):
        query = "DELETE FROM books WHERE id = %s"
        self.db.cursor.execute(query, (str(book_id),))
        self.db.connection.commit()
        return self.db.cursor.rowcount > 0


    def get_available(self) -> list[Book]:
        query = "SELECT * FROM books WHERE status = %s"
        self.db.cursor.execute(query, (BookStatus.AVAILABLE.value,))
        results = self.db.cursor.fetchall()

        book_list = []

        for row in results:
            book_list.append(Book(
                id=UUID(row["id"]),
                title=row["title"],
                author=row["author"],
                isbn=row["isbn"],
                category=row["category"],
                total_copies=row["total_copies"],
                available_copies=row["available_copies"],
                status=BookStatus(row["status"])
            ))

        return book_list