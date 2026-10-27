from fastapi import FastAPI,Depends,Session
from db import get_db
from models import Blog
from schema import PydenticBlog
from typing import List


app = FastAPI(title="my app")

# @app.get("/all-blogs",response_model=List[PydenticBlog])
# def get_blogs(request: PydenticBlog, db: Session=Depends(get_db)):
#     try:
#         blogs = db.query(Blog).all()
#         if not blogs:
            


import time

@app.middleware
async def logging_middleware(request,call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-"] = f""
    return response