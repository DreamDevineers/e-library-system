from uuid import UUID

from e_library_system.models.member import Member
from e_library_system.dtos.login_request import LoginRequest
from e_library_system.repositories.member_repository import MemberRepository
from datetime import datetime, timezone
from e_library_system.dtos.create_member_request import CreateMemberRequest


class MemberService:

    def __init__(self, repository: MemberRepository):
        self.repository = repository

    def create_member(self, request: CreateMemberRequest):
        existing_member = self.repository.get_by_email(request.email)

        if existing_member is not None:
            raise ValueError("A member with this email already exists")

        member = Member(
            name=request.name,
            email=request.email,
            phone=request.phone,
            password=request.password,
            joined_at=datetime.now(timezone.utc),
            active=True
        )

        return self.repository.create_member(member)

    def login(self, login_request: LoginRequest):
        member = self.repository.get_by_email(login_request.email)

        if member is None:
            raise ValueError("Invalid email or password")

        if member.password != login_request.password:
            raise ValueError("Invalid email or password")

        return member

    def get_all_members(self):
        return self.repository.get_all()

    def get_member_by_id(self, member_id: UUID):
        member = self.repository.get_by_id(member_id)

        if member is None:
            raise ValueError("Member not found")

        return member

    def get_member_by_email(self, email: str):
        member = self.repository.get_by_email(email)

        if member is None:
            raise ValueError("Member not found")

        return member

    def update_member(self, member_id: UUID, member: Member):
        existing_member = self.repository.get_by_id(member_id)

        if existing_member is None:
            raise ValueError("Member not found")

        member_with_email = self.repository.get_by_email(member.email)

        if member_with_email is not None and member_with_email.id != member_id:
            raise ValueError("A member with this email already exists")

        return self.repository.update_member(member_id, member)

    def delete_member(self, member_id: UUID):
        existing_member = self.repository.get_by_id(member_id)

        if existing_member is None:
            raise ValueError("Member not found")

        return self.repository.delete_member(member_id)