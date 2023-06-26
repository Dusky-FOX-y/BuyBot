from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import Income
from .schemas import CreateIncome, GetIncome

income_router = APIRouter(prefix='/income', tags=["HR"])


@income_router.post("/create", response_model=GetIncome)
async def create_income(income: CreateIncome):
    try:
        return await Income.objects.create(**income.dict())
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))


@income_router.get("/all", response_model=List[GetIncome])
async def get_incomes():
    return await Income.objects.all()
