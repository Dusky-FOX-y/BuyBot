import ormar
from db import MainMeta


class OrderList(ormar.Model):

    class Meta(MainMeta):
        pass
    id_: int = ormar.Integer(primary_key=True, autoincrement=True)
    good_id: int = ormar.Integer()
    order_id: int = ormar.Integer()
    amount: int = ormar.Integer()
