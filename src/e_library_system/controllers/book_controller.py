from uuid import UUID
from fastapi import APIRouter, HTTPException, status

from e_library_system.dtos.create_book_request import CreateBookRequest
from e_library_system.repositories.book_repository_impl import BookRepositoryImpl
from e_library_system.services.book_service import BookService

router = APIRouter(prefix="/book", tags=["Book"])


def get_book_service():
    repository = BookRepositoryImpl()
    return BookService(repository)


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_book(book_request: CreateBookRequest):
    try:
        service = get_book_service()
        return service.add_book(book_request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def get_all_books():
    try:
        service = get_book_service()
        return service.get_all_books()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/available")
def get_available_books():
    try:
        service = get_book_service()
        return service.get_available_books()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{book_id}")
def get_book(book_id: UUID):
    try:
        service = get_book_service()
        return service.get_book_by_id(book_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{book_id}")
def update_book(book_id: UUID, book_data: CreateBookRequest):
    try:
        service = get_book_service()
        return service.update_book(book_id, book_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{book_id}")
def delete_book(book_id: UUID):
    try:
        service = get_book_service()
        service.delete_book(book_id)
        return {"detail": "Book deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
