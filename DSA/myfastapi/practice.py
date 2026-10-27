from fastapi import FastAPI, Query, Depends, Path
from typing import Optional, Annotated
from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker

Base = declarative_base()

engine = create_engine("sqlite//:")
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base.metadata.create_all(bind=engine)

# # https://<url>/inventory?q=<query>&offset=<num>&limit=<num>
app = FastAPI()

class User(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: str
    name: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[SessionLocal,Depends(get_db)]

@app.get('/users')
async def get_users(db: SessionDep):
    stmt = select(User)
    result = db.execute(stmt)

    users = result.scalers().all()
    return users

    

@app.get('/user/{user_id}')
def ge_user_id(db:SessionDep, user_id: Annotated[int,Path(ge=1)]):
    stmt = select(User).where(id=user_id)
    result = db.execute(stmt).one_or_none()

    user = result.scaler_one_or_none()
    return user


















# class CommonPramasClass:
#     def __init__(self,
#         q: Optional[str] = Query("",description="Query to be performed"),
#         offset: Optional[int] = Query(4,ge=0,le=10),
#         limit: Optional[int] = Query(23,le=100)
#     ):
    
#         self.q = q
#         self.offset = offset
#         self.limit = limit
    
# CommonParams = Annotated[CommonPramasClass,Depends()]


# @app.get('/inventory')
# def get_inventory(commonParams: CommonParams):
#     return {"q":commonParams.q,"limit":commonParams.limit}


# @app.get('/another_route')
# def another_route(commonParams: CommonParams):
#     return {"offset":commonParams.offset}


