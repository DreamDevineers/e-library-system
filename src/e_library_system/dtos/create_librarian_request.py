from pydantic import BaseModel


class CreateLibrarianRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str
    address: str
