from sqlalchemy.orm import Session

from e_library_system.models.member import Member
from e_library_system.repositories.member_repository import MemberRepository


class MemberRepositoryImpl(MemberRepository):

    def __init__(self, db: Session):
        self.db = db

    def create_member(self, member_id: str, data: Member):
        member = Member(
            id=member_id,
            name=data.name,
            email=data.email,
            phone=data.phone,
            join_date=data.join_date,
            active=data.active
        )

        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)

        return member

    def get_all(self):
        return self.db.query(Member).all()

    def get_by_id(self, member_id: str):
        return self.db.query(Member).filter(Member.id == member_id).first()

    def get_by_email(self, email: str):
        return self.db.query(Member).filter(Member.email == email).first()

    def update_member(self, member_id: str, data: Member):
        member = self.get_by_id(member_id)

        if member is None:
            return None

        member.name = data.name
        member.email = data.email
        member.phone = data.phone
        member.join_date = data.join_date
        member.active = data.active

        self.db.commit()
        self.db.refresh(member)

        return member

    def delete_member(self, member_id: str):
        member = self.get_by_id(member_id)

        if member is None:
            return False

        self.db.delete(member)
        self.db.commit()

        return True