from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import Good
from .schemas import CreateGood, GetGood, GerOrderByID

goods_router = APIRouter(prefix='/goods', tags=["Goods"])


@goods_router.post("/create", response_model=GetGood)
async def create_good(job: CreateGood):
    try:
        return await Good.objects.create(**job.dict())
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))


@goods_router.get("/all", response_model=List[GetGood])
async def get_goods():
    return await Good.objects.all()


@goods_router.get("/getbyid", response_model=List[GerOrderByID])
async def get_goodbyid(id_: int):
    return await Good.objects.filter(id_=id_).get()
