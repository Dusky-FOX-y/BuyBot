import ormar
from db import MainMeta


class Good(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: int = ormar.Integer(primary_key=True, autoincrement=True)
    name: str = ormar.String(unique=True, max_length=2048)
    value: float = ormar.Float()
