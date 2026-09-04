from pydantic import BaseModel


class CreateMemberRequest(BaseModel):
    name: str
    email: str
    phone: str
    password: str