from abc import ABC, abstractmethod
from typing import List

from .models import Comment, Post, User


class AbstractPostRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Post]:
        pass

    @abstractmethod
    async def create(self, post: Post) -> Post:
        pass


class AbstractUserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int) -> User | None:
        pass


class AbstractCommentRepository(ABC):
    @abstractmethod
    async def get_all_by_post(self, post_id: int) -> List[Comment]:
        pass

    @abstractmethod
    async def create(self, comment: Comment) -> Comment:
        pass
