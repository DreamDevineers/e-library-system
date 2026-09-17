from uuid import UUID, uuid4

from e_library_system.dtos.create_book_request import CreateBookRequest
from e_library_system.models.book import Book
from e_library_system.repositories.book_repository import BookRepository


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_book_by_id(self, book_id: UUID) -> Book:
        found_book = self.repository.get_by_id(book_id)

        if found_book is None:
            raise ValueError("Book not found")

        return found_book

    def update_book(self, book: Book):
        new_book = self.get_book_by_id(book.id)

        return self.repository.update_book(new_book)

    def add_book(self, book_request: CreateBookRequest) -> Book:
        book = Book(
            id=uuid4(),
            title=book_request.title,
            author=book_request.author,
            isbn=self.generate_isbn(),
            category=book_request.category,
            status=book_request.status
        )

        self.repository.add_book(book)

        return book

    def get_all_books(self) -> list[Book]:
        return self.repository.get_all()

    def get_available_books(self) -> list[Book]:
        found_books = self.repository.get_available()

        if len(found_books) == 0:
            raise ValueError("No books available")

        return found_books

    def delete_book(self, book_id: UUID):
        book = self.get_book_by_id(book_id)

        return self.repository.delete_book(book)

    def generate_isbn(self) -> str:
        number = str(uuid4().int)[:12]

        total = sum(
            int(digit) * (1 if index % 2 == 0 else 3)
            for index, digit in enumerate(number)
        )

        check_digit = (10 - (total % 10)) % 10

        return "978" + number[:9] + str(check_digit)