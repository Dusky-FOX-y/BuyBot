from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import OrderList
from .schemas import CreateOrderList, GetOrderList
import ormar

orderlist_router = APIRouter(prefix='/orderlist', tags=["OrdersList"])


@orderlist_router.get("/all", response_model=List[GetOrderList])
async def get_orders():
    return await OrderList.objects.all()


@orderlist_router.post("/create", response_model=GetOrderList)
async def create_order(orderlist: CreateOrderList):
    try:
        return await OrderList.objects.create(**orderlist.dict())
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))
