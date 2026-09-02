from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"],
)


@router.get("/", response_model=list[schemas.BlogPostResponse])
def get_all_blogs(db: Session = Depends(get_db)):
    return crud.get_all_blog_posts(db)


@router.get("/{id}", response_model=schemas.BlogPostResponse)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog_post = crud.get_blog_post_by_id(db, id)

    if blog_post is None:
        raise HTTPException(
            status_code=404,
            detail="Blog post not found",
        )

    return blog_post


@router.post("/", response_model=schemas.BlogPostResponse, status_code=201)
def create_blog(
    body: schemas.BlogPostCreate,
    db: Session = Depends(get_db),
):
    return crud.create_blog_post(db, body)


@router.put("/{id}", response_model=schemas.BlogPostResponse)
def update_blog(
    id: int,
    body: schemas.BlogPostCreate,
    db: Session = Depends(get_db),
):
    blog_post = crud.update_blog_post(db, id, body)

    if blog_post is None:
        raise HTTPException(
            status_code=404,
            detail="Blog post not found",
        )

    return blog_post


@router.delete("/{id}", status_code=204)
def delete_blog(
    id: int,
    db: Session = Depends(get_db),
):
    blog_post = crud.delete_blog_post(db, id)

    if blog_post is None:
        raise HTTPException(
            status_code=404,
            detail="Blog post not found",
        )


@router.get(
    "/{blog_id}/comments",
    response_model=list[schemas.CommentResponse],
)
def get_blog_comments(
    blog_id: int,
    db: Session = Depends(get_db),
):
    blog_post = crud.get_blog_post_by_id(db, blog_id)

    if blog_post is None:
        raise HTTPException(
            status_code=404,
            detail="Blog post not found",
        )

    return crud.get_comments_by_blog_id(db, blog_id)
