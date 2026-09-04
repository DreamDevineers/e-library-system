import data

from e_library_system.models.book import Book
from fastapi import APIRouter, HTTPException
from uuid import UUID

from e_library_system.repositories.book_repository import BookRepository
from e_library_system.services.book_service import BookService

router = APIRouter(prefix="/book", tags=["Book"])

def get_book_service():
    repository = BookRepository()
    return BookService(repository)

@router.post("/")
def add_book(book: Book):
    try:
        service = get_book_service()
        return service.add_book(book)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail=str(e))


@router.get("/",)
def get_all_books():
    try:
        service = get_book_service()
        return service.get_all_books()
    except ValueError as e:
        raise HTTPException(status_code = 400, detail=str(e))

@router.get("/{book_id}",)
def get_book(book_id: UUID):
    try:
        service = get_book_service()
        return service.get_book_by_id(book_id)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail=str(e))

@router.put("/{book_id}")
def update_book(book_id: UUID,data:Book):
    try:
        service = get_book_service()
        return service.update_book(book_id)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail=str(e))


@router.delete("/{book_id}")
def delete_book(book_id: UUID):
    try:
        service = get_book_service(book_id)
        return service.delete_book(book_id)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail=str(e))
