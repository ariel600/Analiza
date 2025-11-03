from random import randint, seed

def roll_two_d6(seed = None) -> tuple[int, int]:
    if seed != None:
        seed(seed)
    return randint(1, 6), randint(1, 6)

def is_bust(score: int) -> bool:
    return score > 100

def closer_to_target(player1: int, player2: int) -> int | None:
    if player1 == player2:
        return None
    if player1 > player2:
        return 1
    return 2

def turn_decision(input_fn = None) -> str:
    while True:
        input_fn = input("The input must be R-(roll) or P-(pass)")
        if input_fn == "R" or input_fn == "P":
            return input_fn
