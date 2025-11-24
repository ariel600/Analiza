import mysql.connector
from mysql.connector import Error

class DB_connector:
    def __init__(self, host, user, db_name, password=""):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": db_name
        }
        self.connection = None

    def exec_query(self, query: str, params = None):
        results = None
        try:
            self.connection = mysql.connector.connect(**self.config, use_pure=True)
            if(self.connection.is_connected()):
                cursor = self.connection.cursor(dictionary=True)
                cursor.execute(query, params=params)
            query_type = query.strip().upper().split()[0]
            if query_type in ["INSERT", "UPDATE", "DELETE", "CREATE", "ALTER", "DROP"]:
                self.connection.commit()
                results = cursor.rowcount
            else:
                results = cursor.fetchall()
        except Error as e:
            print(e.msg)
        finally:
            if(self.connection and self.connection.is_connected()):
                cursor.close()
                self.connection.close()
        return results
    
if __name__ == "__main__":
    db_school = DB_connector(
        host = "localhost",
        user = "root",
        db_name = "classicmodels",
        password = ""
        )
    start = True
    while start:
        queries = input("""
1 - query employees
2 - query products
3 - query offices
4 - exit
Select the desired option: """)
        if queries == "1":
            for i in db_school.exec_query("SELECT * FROM employees"):
                print(i)
        elif queries == "2":
            for i in db_school.exec_query("SELECT * FROM products"):
                print(i)
        elif queries == "3":
            for i in db_school.exec_query("SELECT * FROM offices"):
                print(i)
        elif queries == "4":
            start = False
        else:
            print("Invalid option, please try again.")