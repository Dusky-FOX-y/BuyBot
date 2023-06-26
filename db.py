from uuid import uuid4

import databases
import ormar
import sqlalchemy
from pydantic import BaseModel

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite.db")


def get_uuid():
    return str(uuid4())


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Message(BaseModel):
    message: str
