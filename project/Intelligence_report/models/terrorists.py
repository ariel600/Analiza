from sqlmodel import Session, select
from init import Terorist

def input_reports():
    return {"id_terorist": input("Enter the terrorist ID: "),
            "text": input("Enter the report text: ")}

def input_terrorist():
    return {"id": input("Enter the terrorist's ID: "),
            "first_name": input("Enter the terrorist's first name: "),
            "last_name": input("Enter the terrorist's last name: ")}

def add_report():
    terrorist = input("Enter the terrorist ID: ")
    with Session(Terorist) as session:
        statement = select(Terorist).where(Terorist.id == terrorist)
    if statement:
        report = input("Enter the report text: ")
        