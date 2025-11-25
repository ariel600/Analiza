# import sqlite3

# class aplite_connector:
#     def __init__(self):
#         pass
    
#     def exec_query(self, query: str, params = None):
#         result = None
#         try:
#             self.connection = sqlite3.connect("tutorial.db")
#             cursor = self.connection.cursor()
#             cursor.execute(query, params or '')
#             query_type = query.strip().upper().split()[0]
#             if query_type in ["INSERT", "UPDATE", "DELETE", "CREATE", "ALTER", "DROP"]:
                
                
#                 self.connection.commit()
#                 results = cursor.rowcount
#             else:
#                 results = cursor.fetchall()
#         except Error as e:
#             print(e.msg)
#         finally:
#             if(self.connection and self.connection.is_connected()):
#                 cursor.close()
#                 self.connection.close()
#         return results

from orm import Sqlite_orm
from users import User

db = Sqlite_orm()
user = User(username = input("name"), phone = input("phone"))
print(db.get_all(User))
db.insert_one(user)
print(User.model_dump())