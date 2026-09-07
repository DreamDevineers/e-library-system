from abc import ABC, abstractmethod
from typing import Optional

from e_library_system.models.librarian import Librarian


class LibrarianRepository(ABC):

    @abstractmethod
    def save(self, librarian: Librarian) -> None:
        ...

    @abstractmethod
    def find_all(self) -> list[Librarian]:
        ...

    @abstractmethod
    def find_by_id(self, librarian_id: str) -> Optional[Librarian]:
        ...

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Librarian]:
        ...

    @abstractmethod
    def update(self, librarian_id: str, librarian: Librarian) -> None:
        ...

    @abstractmethod
    def delete(self, librarian_id: str) -> None:
        ...
