# from data import words
display = []
guessed = {}
wrong_guesses = 0

def init_state(secret: str, max_tries: int) -> dict:
    return {
        "secret": secret,
        "display": ["_"] * len(secret),
        "guessed": set(),
        "wrong_guesses": 0,
        "max_tries": max_tries
        }
        
def validate_guess(ch: str, state: dict) -> tuple[bool, str]: 
    if len(ch) == 1 and ch.isalpha():
        if ch in state["guessed"]:
            return False, "You already guessed this letter."
        elif ch in state["secret"]:
            return True, "Correct guess!"
        else:
            return False, "The letter you entered is not in the word."
    return False, "Incorrect input, please enter only one letter without spaces or numbers."

def is_won(state: dict) -> bool:
    if "_" not in state["display"]:
        return True
    return False

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    False

def render_display(state: dict, ch: str) -> str:
    index = -1
    for i in state["secret"]:
        index += 1
        if i == ch:
            state["display"][index] = ch
    return state["display"]

def render_summary(state: dict) -> str:
    return f"""
        The secret word is {state["secret"]}
        The letters you guessed correctly are these: {state["guessed"]}
        """