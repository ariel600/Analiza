from unittest import result


def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    pass

def show_all_tasks(tasks: list) -> None:
    if len(tasks) == 0:
        print("עדיין לא הוספת משימה.")
    else:
        index = 0
        for task in tasks:
            index += 1
            print(f"{index}. {task}")
    pass

def get_user_choice() -> str:
    choice = input(
    """
    1. הוספת משימה
    2. הצגת המשימות
    3. מחיקת משימה
    4. עריכת משימה
    5. חיפוש משימה
    6. סימון משימה כהושלמה ✓
    7. בדיקת אינדקס של משימה
    8. יציאה
    בחר את האפשרות הרצויה: """
    )
    return choice

def delete_task(tasks: list, index: int) -> None:
    if index > len(tasks):
        print("לא מצאנו את המשימה שברצונך למחוק.")
        return
    if tasks.pop(index - 1):
        print("המשימה נמחקה.")
    return

def edit_task(tasks: list, index: int, new_task: str):
    if index > len(tasks):
        print("לא ניתן לערוך את המשימה, המשימה לא נמצאה.")
        return
    show_all_tasks(tasks)
    tasks[index - 1] = new_task
    print("המשימה שונתה בהצלחה.")
    return

def get_task_index_from_user(nam: int) -> int:
    if nam <= 0:
        return "לא מצאנו את המשימה."
    return nam - 1

def search_tasks(tasks: list, keyword: str) -> list | str:
    if len(tasks) > 0:
        result = []
        index = -1
        for task in tasks:
            index += 1
            if keyword in task:
                result.append((task, index))
        return result
    return "המילה שחיפשת לא נמצאה ברשימת המשימות."

def mark_task_as_done(tasks: list, index: int) -> bool:
    if index > len(tasks) < index:
        print("לא מצאנו את המשימה שברצונך לסמן כהושלמה.")
        return False
    tasks[index - 1] = tasks[index - 1] + " ✓ "
    print("המשימה סומנה כהושלמה.")
    return True