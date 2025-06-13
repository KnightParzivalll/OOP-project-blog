from dataclasses import dataclass


@dataclass
class Post:
    id: int
    title: str
    content: str
    author_id: int


@dataclass
class User:
    id: int
    username: str


@dataclass
class Comment:
    id: int
    post_id: int
    author_id: int
    content: str
