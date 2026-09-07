from abc import ABC, abstractmethod
from typing import Optional

from e_library_system.models.member import Member


class MemberRepository(ABC):

    @abstractmethod
    def save(self, member_id: str, data: Member) -> Member:
        ...

    @abstractmethod
    def find_all(self) -> list[Member]:
        ...

    @abstractmethod
    def find_by_id(self, member_id: str) -> Optional[Member]:
        ...

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Member]:
        ...

    @abstractmethod
    def find_by_status(self, status: str) -> list[Member]:
        ...

    @abstractmethod
    def disable(self, member_id: str) -> None:
        ...

    @abstractmethod
    def enable(self, member_id: str) -> None:
        ...

    @abstractmethod
    def find_active(self) -> list[Member]:
        ...

    @abstractmethod
    def count_active(self) -> int:
        ...