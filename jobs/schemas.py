from pydantic import BaseModel


class CreateJob(BaseModel):
    job: str
    salary: float


class GetJob(CreateJob):
    id_: int
