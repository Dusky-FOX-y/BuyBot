from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import Notify
from .schemas import CreateNotify, GetNotify

notify_router = APIRouter(prefix='/notify', tags=["Notifies"])


@notify_router.post("/create", response_model=GetNotify)
async def create_good(job: CreateNotify):
    try:
        return await Notify.objects.create(**job.dict())
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))


@notify_router.get("/all", response_model=List[GetNotify])
async def get_goods():
    return await Notify.objects.all()


@notify_router.delete("/delete")
async def delete_order(id_: int):
    notify = await Notify.objects.filter(id_=id_).get()
    await notify.delete()
