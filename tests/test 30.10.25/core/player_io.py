def ask_player_action() -> str:
    loop = True
    while loop:
        input_ = input("H or S: ")
        if input_ == "S" or input_ == "H":
            loop = False
        else: print("The input is invalid.")
    return input_
