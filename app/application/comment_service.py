from typing import List

from app.domain.models import Comment
from app.domain.repositories import AbstractCommentRepository


class CommentService:
    def __init__(self, repo: AbstractCommentRepository):
        self.repo = repo

    async def get_comments(self, post_id: int) -> List[Comment]:
        return await self.repo.get_all_by_post(post_id)

    async def get_comment(self, comment_id: int) -> Comment | None:
        return await self.repo.get_by_id(comment_id)

    async def get_all_comments(self) -> List[Comment]:
        return await self.repo.get_all()

    async def create_comment(
        self, post_id: int, author_id: int, content: str
    ) -> Comment:
        return await self.repo.create(
            Comment(id=0, post_id=post_id, author_id=author_id, content=content)
        )

    async def update_comment(self, comment_id: int, content: str) -> None:
        await self.repo.update(comment_id, content)

    async def delete_comment(self, comment_id: int) -> None:
        await self.repo.delete(comment_id)
