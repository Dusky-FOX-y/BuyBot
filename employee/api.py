from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import Employee
from .schemas import CreateEmployee, GetEmployee, AuthEmployee
from jobs.models import Job
import ormar

employee_router = APIRouter(prefix='/employee', tags=["HR"])
auth_router = APIRouter(tags=["Auth"])


@employee_router.get("/all", response_model=List[GetEmployee])
async def get_employees():
    return await Employee.objects.all()


@employee_router.post("/create", response_model=GetEmployee)
async def create_income(employee_: CreateEmployee):
    employee_ = employee_.dict()

    try:
        job_ = await Job.objects.get_or_none(id_=employee_["job_id"])

        if not job_:
            raise sqlite3.IntegrityError("Bad job_id")

        return await Employee.objects.create(**employee_)
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))


@employee_router.put("/update")
async def update_employee(employee_: GetEmployee):
    employee_ = employee_.dict()
    employee_db = await Employee.objects.get(id_=employee_["id_"])
    await employee_db.update(**employee_)


@employee_router.delete("/delete")
async def delete_employee(id_: int):
    employee_ = await Employee.objects.filter(id_=id_).get()
    await employee_.delete()


@auth_router.post("/auth", response_model=GetEmployee)
async def auth_employee(creditals_: AuthEmployee):
    creditals_ = creditals_.dict()

    try:
        return await Employee.objects.get(login=creditals_["login"], password=creditals_["password"])

    except ormar.exceptions.NoMatch as err:
        raise HTTPException(status_code=404, detail=str(err))
