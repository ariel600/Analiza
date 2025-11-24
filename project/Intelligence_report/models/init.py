from sqlmodel import Field, SQLModel, Session, create_engine

engine = create_engine("mysql+mysqlconnector://root@localhost/intelligence_report", echo=True)

class Agent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    phone: int 
    password: str
    level: str | None = None

class Terorist(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    risk_level: str = "dangerous"
    life:bool = True

class Reports(SQLModel, table=True):
    event_number: int = Field(default=None, primary_key=True)
    free_text: str
    agent_id: int | None = Field(default = None, foreign_key = "agent.id")
    terorist_id: int | None = Field(default = None, foreign_key = "terorist.id")