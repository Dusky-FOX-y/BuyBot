import ormar
from db import MainMeta


class Income(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: int = ormar.Integer(primary_key=True)
    employer_id: int = ormar.Integer()
    all_income: float = ormar.Float(minumum=0)
    month_income: float = ormar.Float(minumum=0)
