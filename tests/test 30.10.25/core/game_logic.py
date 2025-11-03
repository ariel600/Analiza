from .player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    result = 0
    for i in hand:
        if i["rank"].isdigit():
            result += int(i["rank"])
        elif i["rank"] == "A":
            result += 1
        else:
            result += 11
    return result

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop()),
    player["hand"].append(deck.pop()),
    dealer["hand"].append(deck.pop()),
    dealer["hand"].append(deck.pop())
    print("player:", calculate_hand_value(player["hand"]))
    print("dealer:", calculate_hand_value(dealer["hand"]))
    return

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) <= 17:
        dealer["hand"].append(deck.pop())
    if calculate_hand_value(dealer["hand"]) > 21:
        print("dealer:", calculate_hand_value(dealer["hand"]))
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    while ask_player_action() == "H":
        player["hand"].append(deck.pop())
        print("player:", calculate_hand_value(player["hand"]))
        if calculate_hand_value(player["hand"]) > 21:
            break
    dealer_play(deck, dealer)
    sum_player = calculate_hand_value(player["hand"])
    sum_dealer = calculate_hand_value(dealer["hand"])
    if sum_player < sum_dealer:
        print("The winner is the dealer")
    elif sum_player > sum_dealer:
        print("The winner is the player")
    else:
        print("draw")
    return
