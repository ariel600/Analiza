from sqlmodel import SQLModel, Field, select, Session
from orm import Sqlite_orm

class User(SQLModel, table = True):
    __tablename__ = "users"
    id: int = Field()
    username: str = Field()