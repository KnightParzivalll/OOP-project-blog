from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import app.domain.models as dm_models
from app.application.post_service import PostService
from app.factories.repository_factory import RepositoryFactory
from app.infrastructure.database.db_session import get_db

# --- Posts router ---
posts_router = APIRouter(prefix="/posts", tags=["Posts"])


@posts_router.get("/", response_model=List[dm_models.Post])
async def get_all_posts(db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    return await service.list_posts()


@posts_router.get("/{post_id}", response_model=dm_models.Post)
async def get_post_by_id(post_id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    post = await service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@posts_router.post("/", response_model=dm_models.Post)
async def create_post(
    title: str, content: str, author_id: int, db: AsyncSession = Depends(get_db)
):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    return await service.create_post(title, content, author_id)


@posts_router.put("/{post_id}")
async def update_post(
    post_id: int, title: str, content: str, db: AsyncSession = Depends(get_db)
):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    await service.update_post(post_id, title, content)
    return {"detail": "Post updated"}


@posts_router.delete("/{post_id}")
async def delete_post(post_id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    await service.delete_post(post_id)
    return {"detail": "Post deleted"}
