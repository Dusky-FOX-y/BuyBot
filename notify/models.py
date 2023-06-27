import ormar
from db import MainMeta


class Notify(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: int = ormar.Integer(primary_key=True, autoincrement=True)
    order_id: int = ormar.Integer()
