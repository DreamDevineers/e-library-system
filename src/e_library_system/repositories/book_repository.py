from abc import ABC, abstractmethod

from e_library_system.models.book import Book


class BookRepository(ABC):
    @abstractmethod
    def get_all(self, book_id: int) -> Book:
        ...

    @abstractmethod
    def get_by_id(self, book_id: int) -> Book:
        ...

    @abstractmethod
    def get_available(self, book_id: int) -> Book:
        ...

    @abstractmethod
    def create_book(self, book: Book) -> Book:
        ...