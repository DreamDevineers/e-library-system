from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

@dataclass
class Member:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    email: str = ""
    phone: str = ""
    joined_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    active: bool = False