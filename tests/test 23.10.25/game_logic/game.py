from utils.deck import *

def create_player(name:str = "AI") -> dict:
    dicti = {"name":name, "hand":[], "won_pile":[]}
    return dicti

def init_game()->dict:
    p1 = create_player("Ariel")
    p2 = create_player()
    cards = create_deck()
    cards = shuffle(cards)
    p1["hand"] = cards[:26]
    p2["hand"] = cards[26:]
    game_dict = {"deck":cards, "player_1":p1, "player_2":p2}
    return game_dict

def play_round(p1:dict,p2:dict):
    a = p1["hand"][0]
    p1["hand"].pop(0)
    b = p2["hand"][0]
    p2["hand"].pop(0)
    winner = compare_cards(a, b)
    if winner == "p1":
        p1["won_pile"].append(a)
        p1["won_pile"].append(b)
        
    elif winner == "p2":
        p2["won_pile"].append(a)
        p2["won_pile"].append(b)
    else:
        pass
    return None
