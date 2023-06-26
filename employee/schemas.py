from pydantic import BaseModel
from typing import Optional
import datetime


class CreateEmployee(BaseModel):
    name: str
    surname: str
    patronymic: str
    phone_number: str
    email: str
    passport_series: str
    passport_number: str
    employee_date: datetime.datetime
    experience: str
    inn: str
    bank_details: str
    job_id: int
    login: str
    password: str


class GetEmployee(CreateEmployee):
    id_: int


class UpdateEmployee(BaseModel):
    id_: int
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    passport_series: Optional[str]
    passport_number: Optional[str]
    employee_date: Optional[datetime.datetime]
    experience: Optional[str]
    inn: Optional[str]
    bank_details: Optional[str]
    job_id: Optional[int]
    login: Optional[str]
    password: Optional[str]


class AuthEmployee(BaseModel):
    login: str
    password: str
