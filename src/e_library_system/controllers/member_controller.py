from uuid import UUID

from fastapi import APIRouter, HTTPException

from e_library_system.dtos.create_member_request import CreateMemberRequest
from e_library_system.dtos.login_request import LoginRequest
from e_library_system.services.member_service import MemberService
from e_library_system.repositories.member_repository_impl import MemberRepositoryImpl


router = APIRouter(prefix="/member", tags=["member"])


def get_member_service():
    repository = MemberRepositoryImpl()
    return MemberService(repository)


@router.post("/")
def register(member: CreateMemberRequest):
    try:
        service = get_member_service()
        return service.register(member)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(login_request: LoginRequest):
    try:
        service = get_member_service()
        return service.authenticate(login_request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/")
def get_all():
    service = get_member_service()
    return service.get_all()


@router.get("/email/{email}")
def get_by_email(email: str):
    try:
        service = get_member_service()
        return service.get_by_email(email)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/status/{status}")
def get_by_status(status: str):
    service = get_member_service()
    return service.get_by_status(status)


@router.put("/{member_id}")
def update(member_id: UUID, member: CreateMemberRequest):
    try:
        service = get_member_service()
        return service.update(member_id, member)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{member_id}/disable")
def disable(member_id: UUID):
    try:
        service = get_member_service()
        service.disable(member_id)
        return {"detail": "Member disabled"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{member_id}/enable")
def enable(member_id: UUID):
    try:
        service = get_member_service()
        service.enable(member_id)
        return {"detail": "Member enabled"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{member_id}")
def get_by_id(member_id: UUID):
    try:
        service = get_member_service()
        return service.get_by_id(member_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))