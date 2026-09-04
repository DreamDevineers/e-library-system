from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Member(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    phone: str
    password: str
    joined_at: datetime
    active: bool