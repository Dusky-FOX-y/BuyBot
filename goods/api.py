from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import Good
from .schemas import CreateGood, GetGood

goods_router = APIRouter(prefix='/goods', tags=["Goods"])


@goods_router.post("/create", response_model=GetGood)
async def create_job(job: CreateGood):
    try:
        return await Good.objects.create(**job.dict())
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))


@goods_router.get("/all", response_model=List[GetGood])
async def get_jobs():
    return await Good.objects.all()
