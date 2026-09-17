from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class BookStatus(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class BookCategory(str, Enum):
    FICTION = "Fiction"
    MYSTERY = "Mystery"
    MEMOIR = "Memoir"
    HISTORICAL = "Historical"
    SCI_FI = "Sci-Fi"
    NONFICTION = "Nonfiction"
    FOOD = "Food"
    THRILLER = "Thriller"
    NATURE = "Nature"
    YOUNG_ADULT = "Young Adult"


class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=3, max_length=50)
    author: str
    isbn: Optional[str] = None
    category: BookCategory
    status: BookStatus = BookStatus.AVAILABLE