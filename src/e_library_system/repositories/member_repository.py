from abc import ABC, abstractmethod

from e_library_system.models.member import Member


class MemberRepository(ABC):

    @abstractmethod
    def create_member(self, member_id: str, data: Member):
        ...

    @abstractmethod
    def get_all(self):
        ...

    @abstractmethod
    def get_by_id(self, member_id: str):
        ...

    @abstractmethod
    def get_by_email(self, email: str):
        ...

    @abstractmethod
    def update_member(self, member_id: str, data: Member):
        ...

    @abstractmethod
    def delete_member(self, member_id: str):
        ...