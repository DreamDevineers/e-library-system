import unittest
from e_library_system.dtos.create_book_request import CreateBookRequest
from e_library_system.models.book import BookCategory, BookStatus
from e_library_system.services.book_service import BookService
from mock_book_repository import MockBookRepository


class BookServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = MockBookRepository()
        self.book_service = BookService(self.repository)

    def test_add_book(self):
        request = CreateBookRequest(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            category=BookCategory.FICTION,
            status=BookStatus.AVAILABLE,
            year=1925,
        )
        saved_book = self.book_service.add_book(request)
        self.assertIsNotNone(saved_book)
        self.assertEqual(saved_book.title, "The Great Gatsby")
        self.assertEqual(saved_book.year, 1925)
        self.assertEqual(len(self.repository.books), 1)

    def test_get_book_by_id(self):
        request = CreateBookRequest(
            title="Things Fall Apart",
            author="Chinua Achebe",
            category=BookCategory.HISTORICAL,
            status=BookStatus.AVAILABLE,
            year=1958,
        )
        saved = self.book_service.add_book(request)
        fetched = self.book_service.get_book_by_id(saved.id)
        self.assertEqual(fetched.title, "Things Fall Apart")

    def test_get_all_books(self):
        req1 = CreateBookRequest(
            title="Book One",
            author="Author One",
            category=BookCategory.FICTION,
            status=BookStatus.AVAILABLE,
            year=2020,
        )
        req2 = CreateBookRequest(
            title="Book Two",
            author="Author Two",
            category=BookCategory.NONFICTION,
            status=BookStatus.AVAILABLE,
            year=2021,
        )
        self.book_service.add_book(req1)
        self.book_service.add_book(req2)
        all_books = self.book_service.get_all_books()
        self.assertEqual(len(all_books), 2)

    def test_delete_book(self):
        request = CreateBookRequest(
            title="Book to Delete",
            author="Author",
            category=BookCategory.FICTION,
            status=BookStatus.AVAILABLE,
            year=2022,
        )
        saved = self.book_service.add_book(request)
        self.book_service.delete_book(saved.id)
        self.assertEqual(len(self.repository.books), 0)


if __name__ == "__main__":
    unittest.main()
