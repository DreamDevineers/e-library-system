from abc import ABC, abstractmethod
from uuid import UUID

from e_library_system.models.loan import Loan


class LoanRepository(ABC):

    @abstractmethod
    def create_loan(self , loan: Loan):
        ...

    @abstractmethod
    def get_all(self):
        ...

    @abstractmethod
    def get_by_id(self, loan_id: UUID):
        ...

    @abstractmethod
    def get_by_book_id(self, book_id: UUID):
        ...

    @abstractmethod
    def update(self, loan_id: UUID, loan: Loan):
        ...

    @abstractmethod
    def delete(self, loan_id: UUID):
        ...

    @abstractmethod
    def count(self) -> int:
        ...