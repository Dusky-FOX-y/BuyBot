import ormar
from db import MainMeta


class Job(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: int = ormar.Integer(primary_key=True)
    job: str = ormar.String(unique=True, max_length=256)
    salary: float = ormar.Float()
