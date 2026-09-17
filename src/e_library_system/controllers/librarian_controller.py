from uuid import UUID

from fastapi import APIRouter, HTTPException

from e_library_system.dtos.create_librarian_request import CreateLibrarianRequest
from e_library_system.dtos.login_request import LoginRequest
from e_library_system.services.librarian_service import LibrarianService
from e_library_system.repositories.librarian_repository_impl import LibrarianRepositoryImpl
from e_library_system.repositories.member_repository_impl import MemberRepositoryImpl


router = APIRouter(prefix="/librarian", tags=["librarian"])


def get_librarian_service():
    librarian_repo = LibrarianRepositoryImpl()
    member_repo = MemberRepositoryImpl()
    return LibrarianService(librarian_repo, member_repo)


@router.post("/")
def register(librarian: CreateLibrarianRequest):
    try:
        service = get_librarian_service()
        return service.register(librarian)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(login_request: LoginRequest):
    try:
        service = get_librarian_service()
        return service.authenticate(login_request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/")
def get_all():
    service = get_librarian_service()
    return service.get_all()


@router.get("/{librarian_id}")
def get_by_id(librarian_id: UUID):
    try:
        service = get_librarian_service()
        return service.get_by_id(librarian_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{librarian_id}")
def update(librarian_id: UUID, librarian: CreateLibrarianRequest):
    try:
        service = get_librarian_service()
        return service.update(librarian_id, librarian)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{librarian_id}")
def delete(librarian_id: UUID):
    try:
        service = get_librarian_service()
        service.delete(librarian_id)
        return {"detail": "Librarian deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
