from datetime import datetime, timezone

from sqlalchemy.orm import Session

from . import models, schemas


def get_all_blog_posts(db: Session):
    return db.query(models.BlogPosts).all()


def get_blog_post_by_id(db: Session, id: int):
    return db.query(models.BlogPosts).filter(models.BlogPosts.id == id).first()


def create_blog_post(db: Session, body: schemas.BlogPostCreate):
    post = models.BlogPosts(
        title=body.title, content=body.content, created_at=datetime.now(tz=timezone.utc)
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


def update_blog_post(db: Session, id: int, body: schemas.BlogPostCreate):
    post = db.query(models.BlogPosts).filter(models.BlogPosts.id == id).first()

    if post is None:
        return None
    post.title = body.title
    post.content = body.content
    post.created_at = datetime.now(tz=timezone.utc)

    db.commit()
    db.refresh(post)

    return post


def delete_blog_post(db: Session, id: int):
    post = get_blog_post_by_id(db, id)

    if post is None:
        return None

    db.delete(post)
    db.commit()

    return post


def get_all_comments(db: Session):
    return db.query(models.Comments).all()


def get_comment_by_id(db: Session, id: int):
    return db.query(models.Comments).filter(models.Comments.id == id).first()


def get_comments_by_blog_id(db: Session, blog_id: int):
    return db.query(models.Comments).filter(models.Comments.id == blog_id).all()


def create_comment(db: Session, body: schemas.CommentCreate):
    comment = models.Comments(
        blog_id=body.blog_id,
        author=body.author,
        content=body.content,
        created_at=datetime.now(tz=timezone.utc),
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def update_comment(db: Session, id: int, body: schemas.CommentCreate):
    comment = get_comment_by_id(db, id)

    if comment is None:
        return None

    comment.author = body.author
    comment.content = body.content
    comment.created_at = datetime.now(tz=timezone.utc)

    db.commit()
    db.refresh(comment)

    return comment


def delete_comment(db: Session, id: int):
    comment = get_comment_by_id(db, id)

    if comment is None:
        return None

    db.delete(comment)
    db.commit()

    return comment
