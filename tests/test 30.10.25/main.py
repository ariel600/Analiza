from core.deck import build_standard_deck ,shuffle_by_suit
from core.game_logic import run_full_game

if __name__ == "__main__":
    package = build_standard_deck()
    shuffle_by_suit(package)
    player = {"hand": [ ] }
    dealer = {"hand": [ ] }
    run_full_game(package, player, dealer)