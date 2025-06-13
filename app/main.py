from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.infrastructure.database import models
from app.infrastructure.database.db_session import engine
from app.interfaces.api.comments import comments_router
from app.interfaces.api.posts import posts_router
from app.interfaces.api.users import users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


app.include_router(posts_router)
app.include_router(users_router)
app.include_router(comments_router)
