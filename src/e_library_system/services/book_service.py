from e_library_system.models.book import Book
from e_library_system.repositories.book_repository import BookRepository


class IdDoNotMatchException(Exception):
    pass

class NoBookFoundException(Exception):
    pass


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository


    def add_book(self, book: Book) -> Book:
        save_book= self.repository.add_book(self,book)
        return save_book

    def get_all_books(self) -> list[Book]:
        all_books = self.repository.get_all()
        return all_books

    def get_book_by_id(self, book_id: int) -> Book:
        found_book = self.repository.get_by_id(book_id)
        if found_book != book_id:
            raise IdDoNotMatchException
        return found_book

    def get_available_books(self) -> Book:
        found_books = self.repository.get_available()
        if len(found_books) == 0:
            raise NoBookFoundException

        return found_books


    def update_book(self, book: Book) -> None:
        updated_book = self.repository.update_book(book)
        if updated_book != book:
            raise NoBookFoundException
        return updated_book

    def delete_book(self, book_id: int) -> None:
        deleted_book = self.repository.delete_book(book_id)
        if deleted_book != book_id:
            raise NoBookFoundException
        return deleted_book


