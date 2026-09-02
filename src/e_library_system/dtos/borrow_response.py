from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from e_library_system.models.loan import LoanStatus, Loan


class BorrowResponseDto(BaseModel):
    loan_id: UUID
    member_id: UUID
    book_id: UUID
    loan_date: date
    due_date: date
    return_date: Optional[date] = None
    status: LoanStatus

    @classmethod
    def from_loan(cls, loan: Loan) -> BorrowResponseDto:
        return cls(
            loan_id = loan.loan_id,
            member_id = loan.member_id,
            book_id = loan.book_id,
            loan_date = loan.loan_date,
            due_date = loan.due_date,
            return_date = loan.return_date,
            status = loan.status,
        )