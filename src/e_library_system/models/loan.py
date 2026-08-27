from datetime import date
from typing import Optional

from pydantic import BaseModel

class Loan(BaseModel):
    loan_id: int
    member_id: int
    book_id: int
    loan_date: date
    due_date: date
    return_date: Optional[date] = None
    status: str