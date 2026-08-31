from uuid import UUID

from e_library_system.models.loan import Loan
from e_library_system.repositories.loan_repository import LoanRepository


class LoanRepositoryImpl(LoanRepository):

    def __init__(self):
        self.loans : list[Loan] = []

    def save(self, data: Loan) -> type[Loan]:
        self.loans.append(data)
        return Loan

    def get_all(self):
        return self.loans

    def update(self, loan_id: UUID, data: Loan):
        loan = self.get_by_id(loan_id)
        if loan is None:
            return None

        index = self.loans.index(loan)
        self.loans[index] = data
        return data

    def get_by_book_id(self, book_id: UUID):
        for loan in self.loans:
            if loan.book_id == book_id:
                return loan

        return None

    def get_by_id(self, loan_id: UUID):
        for loan in self.loans:
            if loan.loan_id == loan_id:
                return loan
        return None

    def delete(self, loan_id: UUID):
        pass

    def count(self):
        return len(self.loans)
