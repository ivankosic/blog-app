from pydantic import BaseModel
import datetime

class BlogPostResponse(BaseModel):
    id : int
    title : str
    content : str
    created_at : datetime

class BlogPostCreate(BaseModel):
    title : str
    content : str



class CommentResponse(BaseModel):
    id : int
    blog_id : int
    author : str
    content : str
    created_at : datetime

class CommentCreate(BaseModel):
    blog_id : int
    author : str
    content : str