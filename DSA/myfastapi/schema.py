
from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class PydenticBlog(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    content: Optional[str] = None
    created_at: Optional[datetime] = None









