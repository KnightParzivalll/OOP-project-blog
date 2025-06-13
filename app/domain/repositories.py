from abc import ABC, abstractmethod
from typing import List

from .models import Comment, Post, User


class AbstractPostRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Post]:
        pass

    @abstractmethod
    async def get_by_id(self, post_id: int) -> Post | None:
        pass

    @abstractmethod
    async def create(self, post: Post) -> Post:
        pass

    @abstractmethod
    async def update(self, post_id: int, title: str, content: str) -> None:
        pass

    @abstractmethod
    async def delete(self, post_id: int) -> None:
        pass


class AbstractUserRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[User]:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def update(self, user_id: int, username: str) -> None:
        pass

    @abstractmethod
    async def delete(self, user_id: int) -> None:
        pass


class AbstractCommentRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Comment]:
        pass

    @abstractmethod
    async def get_by_id(self, comment_id: int) -> Comment | None:
        pass

    @abstractmethod
    async def get_all_by_post(self, post_id: int) -> List[Comment]:
        pass

    @abstractmethod
    async def create(self, comment: Comment) -> Comment:
        pass

    @abstractmethod
    async def update(self, comment_id: int, content: str) -> None:
        pass

    @abstractmethod
    async def delete(self, comment_id: int) -> None:
        pass
