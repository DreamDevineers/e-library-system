from abc import ABC, abstractmethod

from e_library_system.models.book import Book


class BookRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Book]:
        ...

    @abstractmethod
    def get_by_id(self, book_id: int) -> Book:
        ...

    @abstractmethod
    def get_available(self) -> Book:
        ...

    @abstractmethod
    def add_book(self, book: Book) -> Book:
        ...

    @abstractmethod
    def update_book(self, book: Book) -> Book:
        ...

    @abstractmethod
    def delete_book(self, book_id: int) -> bool:
        ...