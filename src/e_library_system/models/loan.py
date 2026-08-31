from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel , Field

class Loan(BaseModel):
    loan_id: UUID = Field(default_factory=uuid4)
    member_id: UUID
    book_id: UUID
    loan_date: date
    due_date: date
    return_date: Optional[date] = None
    status: str