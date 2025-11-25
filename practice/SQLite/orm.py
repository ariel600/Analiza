from sqlmodel import SQLModel, create_engine, Field, select, Session

class Sqlite_orm():
    def __init__(self):
        self.engine = create_engine("sqlite:///tutorial.db")
        SQLModel.metadata.create_all(self.engine)
        
    def get_all(self, table: SQLModel):
        with Session(self.engine) as session:
            results = session.exec(select(table)).all()
            return results
    
    def insert_one(self, row_data: SQLModel):
        with Session(self.engine) as session:
            session.add(row_data)
            session.commit()
            session.refresh(row_data)
            print(row_data.model_dump())
            return row_data
        
    def search_q(self, table: SQLModel, q: str):
        with Session(self.engine) as session:
            select(table)