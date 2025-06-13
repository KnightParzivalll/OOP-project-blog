from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import app.domain.models as dm_models
from app.application.user_service import UserService
from app.factories.repository_factory import RepositoryFactory
from app.infrastructure.database.db_session import get_db

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.post("/", response_model=dm_models.User)
async def create_user(username: str, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    return await service.create_user(username)


@users_router.get("/{user_id}", response_model=dm_models.User)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.get("/", response_model=List[dm_models.User])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    return await service.get_all_users()


@users_router.put("/{user_id}")
async def update_user(user_id: int, username: str, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    await service.update_user(user_id, username)
    return {"detail": "User updated"}


@users_router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    await service.delete_user(user_id)
    return {"detail": "User deleted"}
