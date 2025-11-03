from random import randint
 
def create_card(rank:str,suite:str) -> dict:
    val = {"A":14, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
    cards = {"rank":rank, "suite":suite, "value":val[rank]}
    return cards

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] == p2_card["value"]:
        return "WAR"
    elif p1_card["value"] > p2_card["value"]:
        return "p1"
    return "p2"

def create_deck() -> list[dict]:
    rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suite = ["h", "c", "d", "s"]
    result = []
    for i in rank:
        for j in suite:
            result.append(create_card(i, j))
    return result
            
def shuffle(deck:list[dict]) -> list[dict]:
    i = 0
    while i != 1000:
        a = randint(0, 51)
        b = randint(0, 51)
        if a != b:
            deck[a], deck[b] = deck[b], deck[a]
            i += 1
    return deck

