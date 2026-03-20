from pydantic import BaseModel
import datetime

class BlogPost(BaseModel):
    id : int
    title : str
    content : str
    created_at : datetime

class Comment(BaseModel):
    id : int
    blog_id : int
    author : str
    content : str
    created_at : datetime