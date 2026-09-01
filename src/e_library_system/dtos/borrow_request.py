from uuid import UUID

from pydantic import BaseModel


class BorrowRequestDto(BaseModel):
    member_id: UUID
    book_id: UUID
    loan_period: int = 14