from sqlalchemy.orm import Session
from models import BlogPosts
from schemas import BlogPostResponse, BlogPostCreate
from datetime import datetime

from fastapi import HTTPException

def get_all(db : Session) -> list[BlogPosts]:
    return db.query(BlogPosts).all()

def create_blog_post(db : Session, bp : BlogPostCreate) -> BlogPosts:
    db_blogpost = BlogPosts(title=bp.title, content=bp.content, created_at=datetime.now())

    db.add(db_blogpost)
    db.commit()
    db.refresh(db_blogpost)

    return db_blogpost

def update_blog_post(db : Session, id : int, bp : BlogPostCreate) -> BlogPosts:
    blogpost = db.query(BlogPosts).filter(id == BlogPosts.id).get()

    if blogpost is None:
        return {"message" : "No blogpost with such ID found!"}
    
    blogpost = BlogPosts(title=bp.title, content=bp.content, created_at=datetime.now())

    db.add(blogpost)
    db.refresh(blogpost)

    return blogpost

def delete_blog_post(db : Session, id : int) -> None:
    blogpost = db.query(BlogPosts).filter(id == BlogPosts.id).get()

    if blogpost is None:
        return {"message" : "No blogpost with such ID found!"}
    
    db.delete(blogpost)
    db.refresh()

    return None