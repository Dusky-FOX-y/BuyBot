from pydantic import BaseModel
from typing import Optional


class CreateOrder(BaseModel):
    tid: int
    price: float
    description: str
    status: int


class GetOrder(CreateOrder):
    id_: int


class UpdateOrder(BaseModel):
    id_: int
    tid: Optional[int]
    price: Optional[float]
    description: Optional[str]
    status: Optional[int]
