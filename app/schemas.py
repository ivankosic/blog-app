from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BlogPostCreate(BaseModel):
    title: str
    content: str


class BlogPostResponse(BlogPostCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


class CommentCreate(BaseModel):
    author: str
    content: str


class CommentResponse(CommentCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    blog_id: int
    created_at: datetime
