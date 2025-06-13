from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models import Comment, Post, User
from app.domain.repositories import (
    AbstractCommentRepository,
    AbstractPostRepository,
    AbstractUserRepository,
)

from .models import CommentDB, PostDB, UserDB


class SQLPostRepository(AbstractPostRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Post]:
        result = await self.db.execute(select(PostDB))
        db_posts = result.scalars().all()
        return [
            Post(id=p.id, title=p.title, content=p.content, author_id=p.author_id)
            for p in db_posts
        ]

    async def get_by_id(self, post_id: int) -> Post | None:
        result = await self.db.execute(select(PostDB).where(PostDB.id == post_id))
        p = result.scalar_one_or_none()
        if p:
            return Post(
                id=p.id, title=p.title, content=p.content, author_id=p.author_id
            )
        return None

    async def create(self, post: Post) -> Post:
        db_post = PostDB(
            title=post.title, content=post.content, author_id=post.author_id
        )
        async with self.db.begin():
            self.db.add(db_post)
        await self.db.refresh(db_post)
        return Post(
            id=db_post.id,
            title=db_post.title,
            content=db_post.content,
            author_id=db_post.author_id,
        )

    async def update(self, post_id: int, title: str, content: str) -> None:
        async with self.db.begin():
            await self.db.execute(
                update(PostDB)
                .where(PostDB.id == post_id)
                .values(title=title, content=content)
            )

    async def delete(self, post_id: int) -> None:
        async with self.db.begin():
            await self.db.execute(delete(PostDB).where(PostDB.id == post_id))


class SQLUserRepository(AbstractUserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[User]:
        result = await self.db.execute(select(UserDB))
        db_users = result.scalars().all()
        return [User(id=u.id, username=u.username) for u in db_users]

    async def get_by_id(self, user_id: int) -> User | None:
        result = await self.db.execute(select(UserDB).where(UserDB.id == user_id))
        db_user = result.scalars().first()
        if db_user:
            return User(id=db_user.id, username=db_user.username)
        return None

    async def create(self, user: User) -> User:
        db_user = UserDB(username=user.username)
        async with self.db.begin():
            self.db.add(db_user)
        await self.db.refresh(db_user)
        return User(id=db_user.id, username=db_user.username)

    async def update(self, user_id: int, username: str) -> None:
        async with self.db.begin():
            await self.db.execute(
                update(UserDB).where(UserDB.id == user_id).values(username=username)
            )

    async def delete(self, user_id: int) -> None:
        async with self.db.begin():
            await self.db.execute(delete(UserDB).where(UserDB.id == user_id))


class SQLCommentRepository(AbstractCommentRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Comment]:
        result = await self.db.execute(select(CommentDB))
        db_comments = result.scalars().all()
        return [
            Comment(
                id=c.id, content=c.content, post_id=c.post_id, author_id=c.author_id
            )
            for c in db_comments
        ]

    async def get_by_id(self, comment_id: int) -> Comment | None:
        result = await self.db.execute(
            select(CommentDB).where(CommentDB.id == comment_id)
        )
        c = result.scalar_one_or_none()
        if c:
            return Comment(
                id=c.id, content=c.content, post_id=c.post_id, author_id=c.author_id
            )
        return None

    async def get_all_by_post(self, post_id: int) -> List[Comment]:
        result = await self.db.execute(
            select(CommentDB).where(CommentDB.post_id == post_id)
        )
        db_comments = result.scalars().all()
        return [
            Comment(
                id=c.id, content=c.content, post_id=c.post_id, author_id=c.author_id
            )
            for c in db_comments
        ]

    async def create(self, comment: Comment) -> Comment:
        db_comment = CommentDB(
            content=comment.content,
            post_id=comment.post_id,
            author_id=comment.author_id,
        )
        async with self.db.begin():
            self.db.add(db_comment)
        await self.db.refresh(db_comment)
        return Comment(
            id=db_comment.id,
            content=db_comment.content,
            post_id=db_comment.post_id,
            author_id=db_comment.author_id,
        )

    async def update(self, comment_id: int, content: str) -> None:
        async with self.db.begin():
            await self.db.execute(
                update(CommentDB)
                .where(CommentDB.id == comment_id)
                .values(content=content)
            )

    async def delete(self, comment_id: int) -> None:
        async with self.db.begin():
            await self.db.execute(delete(CommentDB).where(CommentDB.id == comment_id))
