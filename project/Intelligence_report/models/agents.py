from sqlmodel import Session, select
from init import Agent

def menu_login():
    return input(" 1 - Login \n 2 - Register ")

def input_login():
    return {"id": input("Enter your ID: "),
            "password": input("Enter your password: ")}
    
def input_agent():
    return {"id": input("Enter your ID: "),
            "first_name": input("Enter your first name: "),
            "last_name": input("Enter your last name: "),
            "phone": input("Insert your phone: "),
            "password": input("Insert your password: ")}

def login():
    user = input_login()
    with Session(Agent.engine) as session:
        statement = select(Agent).where(Agent.id == user["id"], Agent.password == user["password"])
        results = session.exec(statement)
        agent = results.first()
        if agent:
            print(f"Welcome, {agent.first_name} {agent.last_name}!")
            return agent
        else:
            print("Invalid ID or password.")
            return None

def add_agent():
    user = input_agent()
    agent = Agent(user["id"], user["first_name"], user["last_name"], user["phone"], user["password"])
    with Session(Agent.engine) as session:
        session.add(agent)
        session.commit()
        session.refresh(agent)
        print(f"Added agent with id: {agent.id}.")
        return agent