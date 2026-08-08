from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from .database import Base


class BlogPosts(Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime)


class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    blog_id = Column(
        Integer, ForeignKey("blog_posts.id"), index=True
    )  # Added index to blog ID
    author = Column(String, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime)
