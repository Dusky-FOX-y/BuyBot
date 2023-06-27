from pydantic import BaseModel


class CreateNotify(BaseModel):
    order_id: int


class GetNotify(CreateNotify):
    id_: int
