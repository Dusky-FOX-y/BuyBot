from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import Job
from .schemas import CreateJob, GetJob

jobs_router = APIRouter(prefix='/jobs', tags=["HR"])


@jobs_router.post("/create", response_model=GetJob)
async def create_job(job: CreateJob):
    try:
        return await Job.objects.create(**job.dict())
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))


@jobs_router.get("/all", response_model=List[GetJob])
async def get_jobs():
    return await Job.objects.all()
