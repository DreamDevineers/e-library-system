from pydantic import BaseModel


class CreateMemberRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    password: str
    address: str