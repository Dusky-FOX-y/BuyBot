# from chat.api import chat_router

# from db import database
# from game.api import game_router

import uvicorn
from jobs.api import jobs_router
from employee.api import auth_router, employee_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import database, engine, metadata
from incomes.api import income_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(jobs_router)
app.include_router(income_router)
app.include_router(auth_router)
app.include_router(employee_router)

# app.include_router(game_router)

# app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, use_colors=True, host="176.99.12.178")
