
from sqlalchemy import Column,Integer,String,DateTime
from db import Base

class Blog(Base):
    __tablename__="blog"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String,nullable=False)
    author = Column(String)
    content = Column(String)
    created_at = Column(DateTime)
    




