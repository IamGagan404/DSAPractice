"""A small, self-contained FastAPI CRUD example using in-memory storage.

Run from the repository root with:
    uvicorn DSA.fastapi_crud:app --reload

Data is kept only while the process is running. Replace ``blogs`` with a
database-backed repository for persistent storage.
"""

from typing import Dict

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(title="FastAPI CRUD Example")


class BlogCreate(BaseModel):
    title: str
    author: str
    content: str


class Blog(BlogCreate):
    id: int
    is_favorite: bool = False


# Simple in-memory store, keyed by blog ID.
blogs: Dict[int, Blog] = {}
next_blog_id = 1


@app.post("/blogs", response_model=Blog, status_code=status.HTTP_201_CREATED)
def create_blog(blog_data: BlogCreate) -> Blog:
    """Create a blog and assign it a unique ID."""
    global next_blog_id

    blog = Blog(id=next_blog_id, **blog_data.model_dump())
    blogs[next_blog_id] = blog
    next_blog_id += 1
    return blog


@app.get("/blogs", response_model=list[Blog])
def list_blogs() -> list[Blog]:
    """Return all blogs."""
    return list(blogs.values())


@app.get("/blogs/{blog_id}", response_model=Blog)
def get_blog(blog_id: int) -> Blog:
    """Return one blog by ID."""
    blog = blogs.get(blog_id)
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog


@app.put("/blogs/{blog_id}", response_model=Blog)
def update_blog(blog_id: int, blog_data: BlogCreate) -> Blog:
    """Replace a blog's title, author, and content."""
    if blog_id not in blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

    updated_blog = Blog(
        id=blog_id,
        is_favorite=blogs[blog_id].is_favorite,
        **blog_data.model_dump(),
    )
    blogs[blog_id] = updated_blog
    return updated_blog


@app.delete("/blogs/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int) -> None:
    """Delete a blog by ID."""
    if blogs.pop(blog_id, None) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")


@app.put("/blogs/{blog_id}/favorite", response_model=Blog)
def mark_blog_as_favorite(blog_id: int) -> Blog:
    """Mark this blog as the only favorite, clearing any previous favorite."""
    blog = blogs.get(blog_id)
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

    for existing_id, existing_blog in blogs.items():
        blogs[existing_id] = existing_blog.model_copy(
            update={"is_favorite": existing_id == blog_id}
        )

    return blogs[blog_id]
