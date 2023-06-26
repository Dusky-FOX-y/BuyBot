from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import Order
from .schemas import CreateOrder, GetOrder, UpdateOrder
import ormar
from order_list.models import OrderList

order_router = APIRouter(prefix='/order', tags=["Orders"])


@order_router.get("/all", response_model=List[GetOrder])
async def get_orders():
    return await Order.objects.all()


@order_router.post("/create", response_model=GetOrder)
async def create_order(order: CreateOrder):
    try:
        return await Order.objects.create(**order.dict())
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))



@order_router.put("/update")
async def update_order(order: UpdateOrder):
    order = order.dict()

    order = {k:v for k,v in order.items() if v is not None}
    order_db = await Order.objects.get(id_=order["id_"])
    await order_db.update(**order)


@order_router.delete("/delete")
async def delete_order(id_: int):
    orderlist = await OrderList.objects.filter(order_id=id_).all()
    for i in orderlist:
        await i.delete()
    order = await Order.objects.filter(id_=id_).get()
    await order.delete()
