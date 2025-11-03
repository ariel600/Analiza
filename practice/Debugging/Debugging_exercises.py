# שאלה 1
def greet(username):
    return f"Hello, {username}!"
print(greet("ariel"))

# שאלה 2
counts = {"a":1, "b":2, "c":3}
for k in list(counts):
    if counts[k] % 2 == 0:
        del counts[k]    
print(counts)

# שאלה 3
text = "debugging"
print(text+"!")

# שאלה 4
nums = [1, 2, 3]
for i in range(0, len(nums)):
    print(nums[i] + 1)

# שאלה 5
config = {"username": "", "host": "localhost", "port": 5432}
print(config["username"])

# שאלה 6
age = 12
print(age + 5)

# שאלה 7
user_input = "12.5"
print(user_input)

# שאלה 8
def ratio(a, b):
    if b == 0:
        return "Error! Number cannot be divided by 0"
    return a / b
print(ratio(10, 0))

# שאלה 9
import json
print(json.dumps({"ok": True}))

# שאלה 10
def down(n):
    if n == 0:
        return 0
    return down(n - 1)
print(down(5))

# שאלה 11
x = 5
while x > 0:
    print(x)
    x -= 1

# שאלה 12
def add_item(item, bucket=None):
    if bucket == None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))

# שאלה 13
funcs = []
for i in range(3):
    funcs.append(lambda i=i : print(i))

for f in funcs:
    f()  # Expected 0,1,2; what happens?

# שאלה 14
items = [1, 2, 3, 4, 5]
for x in list(items):
    if x % 2 == 0:
        items.remove(x)
print(items)

# שאלה 15
a = [1, 4, 9]
b = [2, 3, 6, 8]
i, j = 0, 0
merged = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1
merged.append(a[i])
print(merged)

# עד כאן ביצעתי

'''
# שאלה 16
import logging
logging.debug("Start")   # Why no output?

# שאלה 17
for i in range(3):
    j = 0
    j += 1
    print(j)

# שאלה 18
name = "Avi"
print(f"User: {full_name}")

# שאלה 19
data = [10, 20, 30, 40]
total = 0
for i in range(len(data) - 1):
    total += data[i]
print("Total:", total)  # Why is 40 missing?
'''