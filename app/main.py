from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import blogs, database, models, schemas

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/blogs", response_model=list[schemas.BlogPostResponse])
def get_all_blogs(db: Session = Depends(get_db)):
    return blogs.get_all(db)


@app.get("/blogs/{id}", response_model=schemas.BlogPostResponse)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    return blogs.get_by_id(id)


@app.post("/blogs", response_model=schemas.BlogPostResponse)
def create_blog(blog: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    return blogs.create_blog_post(db, blog)


@app.put("/blogs/{id}", response_model=schemas.BlogPostResponse)
def update_blog_post(
    id: int, bp: schemas.BlogPostCreate, db: Session = Depends(get_db)
):
    blog_post = db.query(models.BlogPosts).filter(models.BlogPosts.id == id).first()

    if not blog_post:
        return {"status_code": 404, "details": "Blog post not found"}

    blog_post = blogs.update_blog_post(blog_post.id, bp, db)

    if not blog_post:
        return {"details": "Failed to update blog post"}

    return blog_post


@app.delete("/blogs/{id}", response_model=None)
def delete_blog_post(id: int, db: Session = Depends(get_db)):
    blog_post = db.query(models.BlogPosts).filter(models.BlogPosts.id == id).first()

    if not blog_post:
        return {"status_code": 404, "details": "Blog post not found"}

    blogs.delete_blog_post(blog_post.id, db)

    if not blog_post:
        return {"details": "Failed to delete blog post"}

    return {"status": 200, "body": None, "details": "Blog post deleted successfully"}
