from app.domain.models import User
from app.domain.repositories import AbstractUserRepository


class UserService:
    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo

    async def create_user(self, username: str) -> User:
        return await self.repo.create(User(id=0, username=username))

    async def get_user(self, user_id: int) -> User | None:
        return await self.repo.get_by_id(user_id)
