from random import randint

def build_standard_deck() -> list[dict]:
    suite = ["H", "C", "D", "S"]
    result = []
    for suit in suite:
        for num in range(2, 11):
            result.append({"rank": str(num), "suite": suit})
        for rank in ["J", "Q", "K", "A"]:
            result.append({"rank": str(rank), "suite": suit})
    return result

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    while swaps > 0:
        i = randint(0, len(deck) - 1)
        j = randint(0, len(deck) - 1)
        if i != j:
            deck[i], deck[j] = deck[j], deck[i]
            swaps -= 1
    return deck