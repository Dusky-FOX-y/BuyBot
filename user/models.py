import ormar
from db import MainMeta


class User(ormar.Model):

    class Meta(MainMeta):
        pass

    tid: int = ormar.Integer(primary_key=True)
    phone: str = ormar.String(max_length=12, nullable=True)
    nickname: str = ormar.String(max_length=512, nullable=True)
    name: str = ormar.String(max_length=512, nullable=True)
    address: str = ormar.String(max_length=2048, nullable=True)
    permissions: int = ormar.Integer(nullable=True)
