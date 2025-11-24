def connent(host, user, db_name, password=""):
    config = {
        "host": host,
        "user": user,
        "password": password,
        "database": db_name
    }
    connection = None
    
if connent(
    input("host: "), 
    input("user: "), 
    input("password: "), 
    input("database: ")
    ):
    print("Connected successfully")
else: print("Error")