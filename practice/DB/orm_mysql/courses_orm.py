from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, engine_from_config, Session, select

class Course(SQLModel, table=True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name: str
    hours: int
    is_active: bool = True
    engine = create_engine("mysql+mysqlconnector://root@127.0.0.1:3306/courses_orm?use_pure=true", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(Course.engine)

def add_course(name: str, hours: int, is_active: bool = True):
    course = Course(name=name, hours=hours, is_active=is_active)
    with Session(Course.engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)
        print(f"Added course with id {course.id}")

def add_course(name: str, hours: int, is_active: bool = True):
    course = Course(name=name, hours=hours, is_active=is_active)
    with Session(Course.engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)
        print(f"Added course with id {course.id}")
        
def get_active_courses():
    with Session(Course.engine) as session:
        statement = select(Course).where(Course.is_active == True)
        results = session.exec(statement)
        courses = results.all()
        return courses