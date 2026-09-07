from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Librarian(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str
    address: str
    created_at: datetime = Field(default_factory=datetime.now)

    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name