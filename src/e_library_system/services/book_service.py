from uuid import UUID

from e_library_system.models.book import Book
from e_library_system.repositories.book_repository import BookRepository


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository


    def get_book_by_id(self, book_id: int) -> Book:
        found_book = self.repository.get_by_id(book_id)
        if found_book is None:
            raise ValueError("Book not found")
        return found_book

    def update_book(self, book: Book):
        new_book = self.get_book_by_id(book.id)
        if new_book is None:
            raise ValueError("Book not found")

        return self.repository.update_book(new_book)



    def add_book(self, book: Book) -> Book:
        existing_book = self.get_book_by_id(book.id)

        if existing_book is None:
            self.repository.add_book(book)
            return book

        existing_book.available_copies += 1
        existing_book.total_copies += 1

        return self.repository.update_book(existing_book)


    def get_all_books(self) -> list[Book]:
        all_books = self.repository.get_all()
        return all_books

    def get_available_books(self) -> Book:
        found_books = self.repository.get_available()
        if len(found_books) == 0:
            raise ValueError("No books available")

        return found_books

    def delete_book(self, book_id: UUID):
        book = self.get_book_by_id(book_id)
        if book is None:
            raise ValueError("Book not found")

        count = self.repository.delete_book(book)
        return count


