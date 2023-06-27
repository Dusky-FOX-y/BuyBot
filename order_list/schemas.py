from pydantic import BaseModel
from typing import Optional


class CreateOrderList(BaseModel):
    good_id: int
    order_id: int
    amount: int


class GetOrderList(CreateOrderList):
    id_: int


