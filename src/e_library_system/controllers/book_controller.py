import data

from e_library_system.models.book import Book
from fastapi import APIRouter
from uuid import UUID

from e_library_system.repositories.book_repository import BookRepository
from e_library_system.services.book_service import BookService

router = APIRouter(prefix="/book", tags=["Book"])

def get_book_service():
    repository = BookRepository()
    return BookService(repository)

@router.get("/{book_id}")
def create_book(data: Book):
    pass

@router.post("/",)
def get_all_books():
    pass

@router.get("/",)
def get_book(book_id: UUID):
    pass


@router.delete("/{book_id}")
def update_book(book_id: UUID,data:Book):
    pass

@router.delete("/{book_id}")
def delete_book(member_id: str):
    pass