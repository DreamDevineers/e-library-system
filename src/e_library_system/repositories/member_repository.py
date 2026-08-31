from abc import ABC, abstractmethod
from uuid import UUID
from e_library_system.models.member import Member

class MemberRepository(ABC):
    @abstractmethod
    def create_member(self, member: Member):
        ...

    @abstractmethod
    def get_all(self):
        ...

    @abstractmethod
    def get_by_id(self, member_id: UUID):
        ...

    @abstractmethod
    def get_by_email(self, email: str):
        ...

    @abstractmethod
    def update_member(self, member_id: UUID, member: Member):
        ...

    @abstractmethod
    def delete_member(self, member_id: UUID):
        ...