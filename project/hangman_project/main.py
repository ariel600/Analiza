from random import choice
from data import words
from hangman import game, io

def play(words: list[str], max_tries: int = 10) -> None:
    word = choice(words)
    state = game.init_state(word, max_tries)
    print(state["display"])
    while state["wrong_guesses"] < max_tries and game.is_won(state) == False:
        input_ch = io.prompt_guess()
        exem = game.validate_guess(input_ch, state)
        print(exem[1])
        if exem[1] == "You already guessed this letter.":
            continue
        if exem[0]:
            state["display"] = game.render_display(state, input_ch)
            state["guessed"].add(input_ch)
            io.print_status(state)
        if exem[0] == False:
            state["guessed"].add(input_ch)
            state["wrong_guesses"] += 1
            io.print_status(state)
    io.print_result(state)

if __name__ == "__main__":
    play(words.words)