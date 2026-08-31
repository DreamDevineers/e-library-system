from e_library_system.models.book import Book
from fastapi import APIRouter
from uuid import UUID

router = APIRouter(prefix="/book", tags=["Book"])

@router.post("/",)
def get_all_books():
    pass

@router.get("/",)
def get_book(book_id: UUID):
    pass

@router.get("/{book_id}")
def create_book(book_id: data):
    pass

@router.delete("/{book_id}")
def update_book(book_id: UUID,data:Book):
    pass

@router.delete("/{book_id}")
def delete_book(member_id: str):
    pass