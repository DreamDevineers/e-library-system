from uuid import UUID

from e_library_system.models.member import Member
from e_library_system.models.member import MemberStatus
from e_library_system.dtos.login_request import LoginRequest
from e_library_system.dtos.create_member_request import CreateMemberRequest
from e_library_system.repositories.member_repository import MemberRepository


class MemberService:

    def __init__(self, repository: MemberRepository):
        self.repository = repository

    def register(self, request: CreateMemberRequest) -> Member:

        existing_member = self.repository.find_by_email(request.email)

        if existing_member is not None:
            raise ValueError("A member with this email already exists")

        member = Member(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            phone=request.phone,
            password=request.password,
            address=request.address
        )

        return self.repository.save(str(member.id), member)

    def authenticate(self, login_request: LoginRequest) -> Member:

        member = self.repository.find_by_email(login_request.email)

        if member is None:
            raise ValueError("Invalid email or password")

        if member.password != login_request.password:
            raise ValueError("Invalid email or password")

        if member.status != MemberStatus.ACTIVE:
            raise ValueError("Member account is disabled")

        return member

    def get_all(self) -> list[Member]:
        return self.repository.find_all()

    def get_by_id(self, member_id: UUID) -> Member:

        member = self.repository.find_by_id(str(member_id))

        if member is None:
            raise ValueError("Member not found")

        return member

    def get_by_email(self, email: str) -> Member:

        member = self.repository.find_by_email(email)

        if member is None:
            raise ValueError("Member not found")

        return member

    def get_by_status(self, status: str) -> list[Member]:
        return self.repository.find_by_status(status)

    def update(
        self,
        member_id: UUID,
        request: CreateMemberRequest
    ) -> Member:

        existing_member = self.repository.find_by_id(str(member_id))

        if existing_member is None:
            raise ValueError("Member not found")

        member = Member(
            id=member_id,
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            phone=request.phone,
            password=request.password,
            address=request.address,
            status=existing_member.status,
            created_at=existing_member.created_at
        )

        return self.repository.save(str(member_id), member)

    def disable(self, member_id: UUID) -> None:

        member = self.repository.find_by_id(str(member_id))

        if member is None:
            raise ValueError("Member not found")

        self.repository.disable(str(member_id))

    def enable(self, member_id: UUID) -> None:

        member = self.repository.find_by_id(str(member_id))

        if member is None:
            raise ValueError("Member not found")

        self.repository.enable(str(member_id))

    def is_active(self, member_id: UUID) -> bool:

        member = self.repository.find_by_id(str(member_id))

        if member is None:
            raise ValueError("Member not found")

        return member.status == MemberStatus.ACTIVE