from datetime import datetime, timezone
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class Member(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=2, description="Member's full name")
    email: str = Field(..., description="Member's email address")
    phone: str = Field(default="", description="Member's phone number")
    joined_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    active: bool = Field(default=False)