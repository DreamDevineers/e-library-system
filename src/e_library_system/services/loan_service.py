from typing import List
from datetime import date, timedelta
from uuid import UUID

from e_library_system.dtos import borrow_response
from e_library_system.dtos.borrow_request import BorrowRequestDto
from e_library_system.models.loan import Loan, LoanStatus
from e_library_system.repositories.book_repository import BookRepository
from e_library_system.repositories.loan_repository import LoanRepository
from e_library_system.repositories.member_repository import MemberRepository


class LoanService:

    def __init__(self , loan_repository: LoanRepository , member_repository: MemberRepository , book_repository: BookRepository):
        self.loan_repo = loan_repository
        self.member_repo = member_repository
        self.book_repo = book_repository

    def get_all_loan(self) -> List[Loan]:
        loan = self.loan_repo.get_all()
        if loan is None:
            raise ValueError(f"No loans found")

        return loan

    def get_member_loans(self , member_id: UUID) -> List[Loan]:
        member =  self.member_repo.get_by_id(member_id)

        if member is None:
            raise ValueError(f"Member {member_id} not found")

        return self.loan_repo.get_by_member_id(member_id)

    def borrow_book(self , borrow: BorrowRequestDto):
        member = self.member_repo.get_by_id(borrow.member_id)
        if member is None:
            raise ValueError(f"Member {borrow.member_id} not found")

        book = self.book_repo.get_by_id(borrow.book_id)
        if book is None:
            raise ValueError(f"Book {borrow.book_id} not found")

        loan = Loan(
            member_id = borrow.member_id,
            book_id = borrow.book_id,
            loan_date = date.today(),
            due_date = date.today() + timedelta(days = borrow.loan_period),
            status = LoanStatus.ACTIVE,
        )

        created_loan = self.loan_repo.create_loan(loan)
        book.available_copies -= 1
        self.book_repo.update_book(book)

        return borrow_response.BorrowResponseDto.from_loan(created_loan)

    def return_loan(self , loan_id: UUID):
        loan = self.loan_repo.get_by_id(loan_id)
        if loan is None:
            raise ValueError(f"Loan {loan_id} does not exist")

        if loan.status == LoanStatus.RETURNED:
            raise ValueError(f"Book has been returned")

        loan.status = LoanStatus.RETURNED
        loan.return_date = date.today()

        updated_loan = self.loan_repo.update(loan_id, loan)
        book = self.book_repo.get_by_id(loan.book_id)

        if book is not None:
            book.available_copies += 1
            self.book_repo.update_book(book)

        return updated_loan
