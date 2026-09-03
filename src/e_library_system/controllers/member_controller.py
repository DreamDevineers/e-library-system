from uuid import UUID
from fastapi import APIRouter, HTTPException

from e_library_system.models.member import Member
from e_library_system.dtos.login_request import LoginRequest
from e_library_system.services.member_service import MemberService
from e_library_system.repositories.member_repository_impl import MemberRepositoryImpl


router = APIRouter(prefix="/member", tags=["member"])


def get_member_service():
    repository = MemberRepositoryImpl()
    return MemberService(repository)


@router.post("/")
def create_member(member: Member):
    try:
        service = get_member_service()
        return service.create_member(member)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(login_request: LoginRequest):
    try:
        service = get_member_service()
        return service.login(login_request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/")
def list_members():
    service = get_member_service()
    return service.get_all_members()


@router.get("/{member_id}")
def get_member(member_id: UUID):
    try:
        service = get_member_service()
        return service.get_member_by_id(member_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{member_id}")
def update_member(member_id: UUID, member: Member):
    try:
        service = get_member_service()
        return service.update_member(member_id, member)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{member_id}")
def delete_member(member_id: UUID):
    try:
        service = get_member_service()
        return service.delete_member(member_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))