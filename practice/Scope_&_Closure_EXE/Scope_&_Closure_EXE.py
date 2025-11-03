# שאלה 1
x = 10

def show():
    global x
    x = 5
    print("Inside:", x)
    
show()
print("Outside:", x)

"""
היות וה-X היה משתנה מקומי
אז בראשון הוא הדפיס את המקומי
ובשני הוא הדפיס את הגלובלי
"""
    
# שאלה 2
count = 0

def add():
    global count
    count += 1
    print(count)
    
add()

"""
בגלל שלא הגדרתי את count זה נכשל
"""
    
# שאלה 3
msg = "Hi"

def ouret():
    msg = "Hello"
    def inner():
        print(msg)
    inner()

ouret()

"""
השם msg מגיע מ messeg
המשתנה המקומי מודפס
"""

# שאלה 4
def counter():
    num = 0
    def add_one():
        nonlocal num
        num += 1
        print(num)
    add_one()
    
counter()

"""
המשתנה הוא לא גלובלי הוא נמצא בתוך פונקציה
"""

# שאלה 5
name = "Tom"

def greet():
    global name
    name = "Ben"
    print("Hi", name)

greet()
print("Bye", name)

"""
בגלל שהפלט הראשון משתמש עם המשתנה המקומי הוא ידפיס "Ben"
ובפרינט השני הוא ידפיס "Tom" כי בפונקציה הוא לא שינה את הגלובלי
"""
