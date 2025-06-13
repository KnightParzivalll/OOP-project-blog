from contextlib import asynccontextmanager
from typing import List

from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

import app.domain.models as dm_models
from app.application.comment_service import CommentService
from app.application.post_service import PostService
from app.application.user_service import UserService
from app.factories.repository_factory import RepositoryFactory
from app.infrastructure.database import models
from app.infrastructure.database.db_session import engine, get_db


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


@app.get("/posts", response_model=List[dm_models.Post])
async def get_posts(db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    return await service.list_posts()


@app.get("/comments", response_model=List[dm_models.Comment])
async def get_comments(post_id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return await service.get_comments(post_id)


@app.post("/posts", response_model=dm_models.Post)
async def create_post(
    title: str, content: str, author_id: int, db: AsyncSession = Depends(get_db)
):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    return await service.create_post(title, content, author_id)


@app.post("/users", response_model=dm_models.User)
async def create_user(username: str, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    return await service.create_user(username)


@app.post("/comments", response_model=dm_models.Comment)
async def create_comment(
    post_id: int, author_id: int, content: str, db: AsyncSession = Depends(get_db)
):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return await service.create_comment(post_id, author_id, content)
