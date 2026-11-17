from uuid import UUID
from typing import Optional, List
from e_library_system.models.book import Book, BookStatus
from e_library_system.repositories.book_repository import BookRepository


class MockBookRepository(BookRepository):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> Book:
        self.books.append(book)
        return book

    def get_by_id(self, book_id: UUID) -> Optional[Book]:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def get_all(self) -> List[Book]:
        return list(self.books)

    def update_book(self, book: Book) -> Book:
        for i, existing in enumerate(self.books):
            if existing.id == book.id:
                self.books[i] = book
                return book
        return book

    def delete_book(self, book_id: UUID) -> bool:
        initial_len = len(self.books)
        self.books = [b for b in self.books if b.id != book_id]
        return len(self.books) < initial_len

    def get_available(self) -> List[Book]:
        return [b for b in self.books if b.status == BookStatus.AVAILABLE]
