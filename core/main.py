from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import main_router
from core.models.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run(
        app
    )