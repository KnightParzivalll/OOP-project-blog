from typing import List

from app.domain.models import Comment
from app.domain.repositories import AbstractCommentRepository


class CommentService:
    def __init__(self, repo: AbstractCommentRepository):
        self.repo = repo

    async def get_comments(self, post_id: int) -> List[Comment]:
        return await self.repo.get_all_by_post(post_id)

    async def create_comment(
        self, post_id: int, author_id: int, content: str
    ) -> Comment:
        return await self.repo.create(
            Comment(id=0, post_id=post_id, author_id=author_id, content=content)
        )
