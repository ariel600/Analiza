import game

todo_list = []

def main() -> None:
    while True:
        coice = game.get_user_choice()
        if coice == "1": 
            task = input("מה המשימה שתרצה להוסיף? ")
            game.add_task(todo_list, task)
            print("המשימה התווספה לרשימת המשימות.")
        elif coice == "2":
            game.show_all_tasks(todo_list)
        elif coice == "3": 
            game.show_all_tasks(todo_list)
            delete = int(input("בחר את המשימה שברצונך למחוק: "))
            game.delete_task(todo_list, delete)
        elif coice == "4":
            game.show_all_tasks(todo_list)
            delete = int(input("בחר את המשימה שברצונך לערוך: "))
            new = input("הכנס את המשימה החדשה: ")
            game.edit_task(todo_list, delete, new)
        elif coice == "5":
            if len(todo_list) == 0:
                print("רשימת המשימות ריקה.")
            else:
                search = input("הכנס את המילה שברצונך לחפש: ")
                print(game.search_tasks(todo_list, search))
        elif coice == "6":
            if len(todo_list) == 0:
                print("רשימת המשימות ריקה.")
            else:
                game.show_all_tasks(todo_list)
                done = int(input("בחר את המשימה שהושלמה: "))
                game.mark_task_as_done(todo_list, done)
        elif coice == "7":
            game.show_all_tasks(todo_list)
            nam = input("הכנס מספר לבדיקה: ")
            print(game.get_task_index_from_user(nam))
        elif coice == "8":
            break
        else:
            print("לא הצלחנו לזהות את הבקשה.")
            
        
if __name__ == "__main__":
    main()