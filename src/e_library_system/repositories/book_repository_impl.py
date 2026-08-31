from e_library_system.models.book import Book
from e_library_system.repositories.book_repository import BookRepository


class BookRepositoryImpl(BookRepository):
    def __init__(self,db_session):
        self.db = db_session

    def get_by_id(self,book_id: int) -> Book:
        return self.db.query(Book).filter(Book.id == book_id).first()

    def get_all(self) -> list[Book]:
        return self.db.query(Book).all()

    def add_book(self,book: Book) -> Book:
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update_book(self,book: Book) -> Book:
        self.db.merge(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def delete_book(self,book_id: int) -> bool:
        book = self.get_by_id(book_id)

        if book is None:
            return False

        self.db.delete(book)
        self.db.commit()
        return True


    def get_available(self) -> Book:
        return self.db.query(Book).all()