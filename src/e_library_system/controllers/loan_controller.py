from uuid import UUID

from fastapi import APIRouter, HTTPException

from e_library_system.dtos.borrow_request import BorrowRequestDto
from e_library_system.repositories.book_repository_impl import BookRepositoryImpl
from e_library_system.repositories.loan_repository_impl import LoanRepositoryImpl
from e_library_system.repositories.member_repository_impl import MemberRepositoryImpl
from e_library_system.services.loan_service import LoanService

router = APIRouter(prefix = "/loan", tags = ["loan"])

def get_loan_service():
    loan_repository = LoanRepositoryImpl()
    member_repository = MemberRepositoryImpl()
    book_repository = BookRepositoryImpl()

    return LoanService(loan_repository, member_repository, book_repository)

@router.get("/")
def get_all_loans():
    try:
        service = get_loan_service()
        return service.get_all_loan()
    except ValueError as e:
        raise HTTPException(status_code = 404, detail = str(e))


@router.get("/member/{member_id}")
def get_member_loans(member_id: UUID):
    try:
        service = get_loan_service()
        return service.get_member_loans(member_id)
    except ValueError as e:
        raise HTTPException(status_code = 404, detail = str(e))

@router.post("/borrow")
def borrow_book(borrow: BorrowRequestDto):
    try:
        service = get_loan_service()
        return service.borrow_book(borrow)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))

@router.post("/return/{loan_id}")
def return_loan(loan_id: UUID):
    try:
        service = get_loan_service()
        return service.return_loan(loan_id)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))


