from pydantic import BaseModel
from typing import Optional


class CreateUser(BaseModel):
    tid: int
    phone: str
    nickname: str
    name: str
    address: str
    permissions: int


class GetUser(CreateUser):
    ...


class UpdateUser(BaseModel):
    tid: int
    phone: Optional[str]
    nickname: Optional[str]
    name: Optional[str]
    address: Optional[str]
    permissions: Optional[int]


class GetUserByID(CreateUser):
    tid: int
