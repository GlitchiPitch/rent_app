from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import main_router
from core.models.database import create_db_and_tables, delete_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await create_db_and_tables()
    yield
    # await delete_db_and_tables()


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(main_router)


@app.get("/front", tags=["root"])
async def read_root() -> list[dict]:
    return [
        {
            "id": "1",
            "item": "Read a book."
        },
        {
            "id": "2",
            "item": "Cycle around town."
        }
    ]

if __name__ == '__main__':
    uvicorn.run(
        app
    )
