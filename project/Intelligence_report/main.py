from binascii import Error
from models import agents, reports, terrorists, init
from sqlmodel import Field, SQLModel, create_engine
import mysql.connector

def sql_free():
    input("Enter your SQL command: ")



def menu():
    return input("""
1 - Run Free SQL
2 - Create an Intelligence Report
3 - Delete an Intelligence Report
4 - Search a Report by Word
5 - Search for "Dangerous" Terrorists
6 - Search for "Super Dangerous" Terrorists
7 - Log Out of the System
Select the desired option: """)

if __name__ == "__main__":
    while user is None:
        match agents.menu_login():
            case "1":
                user = agents.login()
            case "2":
                user = agents.add_agent()
    while user is not None:
        match menu():
            case "1": # הרצת SQL חופשית
                if user["level"] == "admin":
                    sql_free()
                else:
                    print("Access denied. Only admins can run free SQL commands.")
            case "2": # יצירת דוח מודיעיני
                pass
            case "3": # מחיקת דוח מודיעיני
                pass
            case "4": # חיפוש דוח לפי מילה
                pass
            case "5": # חיפוש טרוריסטים "מסוכנים"
                pass
            case "6": # חיפוש טרוריסטים "מסוכנים מאוד"
                pass
            case "7": # התנתקות מהמערכת
                user = None