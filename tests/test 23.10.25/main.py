from game_logic import game

if __name__ == "__main__":
    result_p1 = 0
    result_p2 = 0
    users = game.init_game()
    player_1 = users["player_1"]
    player_2 = users["player_2"]
    for i in range(26):
        result = game.play_round(player_1, player_2)
        if result[0] == "p1":
            result_p1 += result[1]["value"]
            result_p1 += result[2]["value"]
        elif result[0] == "p2":
            result_p2 += result[1]["value"]
            result_p2 += result[2]["value"]
        else:
            pass
    if result_p1 > result_p2:
        print("The winner is:", "player 1")
    elif result_p2 > result_p1:
        print("The winner is:", "player 2")
    else:
        print("draw")
