from e_library_system.models.member import Member
from e_library_system.repositories.member_repository import MemberRepository


class MemberService:

    def __init__(self, repository: MemberRepository):
        self.repository = repository

    def create_member(self, member: Member):
        existing_member = self.repository.get_by_email(member.email)

        if existing_member is not None:
            raise ValueError("A member with this email already exists")

        return self.repository.create_member(member.id, member)

    def get_all_members(self):
        return self.repository.get_all()

    def get_member_by_id(self, member_id):
        member = self.repository.get_by_id(member_id)

        if member is None:
            raise ValueError("Member not found")

        return member

    def get_member_by_email(self, email):
        member = self.repository.get_by_email(email)

        if member is None:
            raise ValueError("Member not found")

        return member

    def update_member(self, member_id, member: Member):
        existing_member = self.repository.get_by_id(member_id)

        if existing_member is None:
            raise ValueError("Member not found")

        member_with_email = self.repository.get_by_email(member.email)

        if (
            member_with_email is not None
            and member_with_email.id != member_id
        ):
            raise ValueError("A member with this email already exists")

        return self.repository.update_member(member_id, member)

    def delete_member(self, member_id):
        existing_member = self.repository.get_by_id(member_id)

        if existing_member is None:
            raise ValueError("Member not found")

        return self.repository.delete_member(member_id)