from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    author: str
    id: UUID = Field(default_factory=uuid4)
    isbn: Optional[str] = None
    category: str
    total_copies: int
    available_copies: int