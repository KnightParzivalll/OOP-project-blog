from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import app.domain.models as dm_models
from app.application.comment_service import CommentService
from app.factories.repository_factory import RepositoryFactory
from app.infrastructure.database.db_session import get_db

comments_router = APIRouter(prefix="/comments", tags=["Comments"])


@comments_router.get("/", response_model=List[dm_models.Comment])
async def get_comments_by_post_id(post_id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return await service.get_comments(post_id)


@comments_router.get("/all", response_model=List[dm_models.Comment])
async def get_all_comments(db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return await service.get_all_comments()


@comments_router.get("/{comment_id}", response_model=dm_models.Comment)
async def get_comment_by_id(comment_id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    comment = await service.get_comment(comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@comments_router.post("/", response_model=dm_models.Comment)
async def create_comment(
    post_id: int, author_id: int, content: str, db: AsyncSession = Depends(get_db)
):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return await service.create_comment(post_id, author_id, content)


@comments_router.put("/{comment_id}")
async def update_comment(
    comment_id: int, content: str, db: AsyncSession = Depends(get_db)
):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    await service.update_comment(comment_id, content)
    return {"detail": "Comment updated"}


@comments_router.delete("/{comment_id}")
async def delete_comment(comment_id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    await service.delete_comment(comment_id)
    return {"detail": "Comment deleted"}
