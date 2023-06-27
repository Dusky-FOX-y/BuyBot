import ormar
from db import MainMeta


class Order(ormar.Model):

    class Meta(MainMeta):
        pass
    id_: int = ormar.Integer(primary_key=True, autoincrement=True)
    tid: int = ormar.Integer()
    price: float = ormar.Float()
    description: str = ormar.String(max_length=4096, nullable=True)
    status: int = ormar.Integer()
