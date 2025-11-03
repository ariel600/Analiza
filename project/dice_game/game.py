import utils

def is_exact_100(score: int) -> bool:
    return score == 100

def tie_breaker(roller = None) -> int:
    if roller == None:
        player1 = utils.roll_two_d6()
        player1 = player1.count
        player2 = utils.roll_two_d6()
        player2 = player2.count
        if player1 > player2:
            return 1
        else:
            return 2
    return roller


tie_breaker()