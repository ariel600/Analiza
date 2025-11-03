def prompt_guess() -> str:
    return input("Enter a letter: ")

def print_status(state: dict) -> None:
    print(f"""
    Your word status: {state["display"]}
    All the letters revealed so far: {state["guessed"]}
    The total number of attempts you have left is {state["max_tries"] - state["wrong_guesses"]} out of {state["max_tries"]} attempts.
    """)
    pass

def print_result(state: dict) -> None:
    a = """
        """
    if "_" not in state["display"]:
        print("You won!")
    else:
        print("You failed!")
    print(f"""
        The secret word: {state["secret"]}
        The letters revealed: {state["guessed"]}
        The sum of the mistakes you had is {len(state["guessed"])}
        """)
    pass