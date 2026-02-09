from pydantic import BaseModel
import datetime

class BlogPost(BaseModel):
    def __init__(self):
        self.id = int
        self.title = str
        self.content = str
        self.created_at = datetime

class Comment(BaseModel):
    def __init__(self):
        self.id = int
        self.blog_id = int
        self.author = str
        self.content = str
        self.created_at = datetime