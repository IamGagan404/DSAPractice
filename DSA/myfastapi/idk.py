from fastapi import FastAPI, Depends, Path, HTTPException,status
from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base,sessionmaker,Mapped,mapped_column,Session
from sqlalchemy.exc import IntegrityError
from typing import Annotated, List
from pydantic import BaseModel, ConfigDict


app = FastAPI()

Base = declarative_base()

engine = create_engine("",connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session,Depends(get_db)]

class UserDB(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: str
    email: str


class User(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)

class Req_User(BaseModel):
    name:str
    email:str

@app.get('/users',response_model=List[User])
def users(db: SessionDep):

    stmt = select(UserDB)
    results = db.execute(stmt)

    users = results.scalar().all()

    return users

@app.get('/user/{user_id}',response_model=User)
def get_user_by_id(db:SessionDep,user_id: Annotated[int,Path(ge=1)]):
    stmt = select(UserDB).where(user_id == UserDB.id)
    result = db.execute(stmt)

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user not found {user_id}")
    
    return user

@app.post('/user',response_model=User,status_code=status.HTTP_201_CREATED)
def new_user(db:SessionDep,user:Req_User):
    new_user = UserDB(
        name=user.name,
        email=user.email
    )

    db.add(new_user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    db.refresh(new_user)

    return new_user
    



