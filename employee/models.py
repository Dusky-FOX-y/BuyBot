import ormar
from db import MainMeta
import datetime


class Employee(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128)
    surname: str = ormar.String(max_length=128)
    patronymic: str = ormar.String(max_length=128)
    phone_number: str = ormar.String(max_length=12)
    email: str = ormar.String(max_length=128)
    passport_series: str = ormar.String(max_length=4)
    passport_number: str = ormar.String(max_length=6)
    employee_date: datetime.datetime = ormar.DateTime()
    experience: str = ormar.String(max_length=128)
    inn: str = ormar.String(max_length=128)
    bank_details: str = ormar.String(max_length=128)
    job_id: int = ormar.Integer()
    login: str = ormar.String(max_length=128)
    password: str = ormar.String(max_length=128)
