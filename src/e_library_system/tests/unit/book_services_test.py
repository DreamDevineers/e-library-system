import unittest

from e_library_system.models.book import Book
from e_library_system.repositories.book_repository import BookRepository
from e_library_system.services.book_service import BookService


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = BookRepository
        self.book_service = BookService

    def test_save_book(self):
        self.book = Book
        saved_book = self.book_service.add_book(self,book=self.book)
        self.assertIsNone(saved_book, self.book)


if __name__ == '__main__':
    unittest.main()
