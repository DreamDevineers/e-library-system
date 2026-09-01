from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class BookStatus(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"

class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=3, max_length=50)
    author: str
    isbn: Optional[str] = None
    category: str
    total_copies: int
    available_copies: int
    status: BookStatus = BookStatus.AVAILABLE

