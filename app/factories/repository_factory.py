from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repositories import (
    AbstractCommentRepository,
    AbstractPostRepository,
    AbstractUserRepository,
)
from app.infrastructure.database.repositories import (
    SQLCommentRepository,
    SQLPostRepository,
    SQLUserRepository,
)


class RepositoryFactory:
    @staticmethod
    def create_post_repository(db: AsyncSession) -> AbstractPostRepository:
        return SQLPostRepository(db)

    @staticmethod
    def create_user_repository(db: AsyncSession) -> AbstractUserRepository:
        return SQLUserRepository(db)

    @staticmethod
    def create_comment_repository(db: AsyncSession) -> AbstractCommentRepository:
        return SQLCommentRepository(db)
