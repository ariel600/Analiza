import game, utils

if __name__ == "__main__":
    player_score1 = 0
    player_score2 = 0
    counter = 0

    def play_game():
        global player_score1, player_score2, counter
        while True:
            print("Player 1's turn")
            print("Your score is:", player_score1, "The opponent's score is:", player_score2)
            player1 = utils.turn_decision()
            if player1 == "R":
                dices = utils.roll_two_d6()
                player_score1 += dices[0]
                player_score1 += dices[1]
                print(
                    "The results:", dices[0], dices[1],
                    "sum", dices[0] + dices[1], "\n"
                    "Your total score", player_score1
                    )
                counter = 0
                if game.is_exact_100():
                    print(
                        "Victory!", "\n",
                        "Your score is equal to 100."
                    )
                    return
                if utils.is_bust():
                    print(
                        "Victory to the opponent!", "\n",
                        "Your score exceeded 100.",  "\n", 
                        "Your total score is:", player_score1
                    )
            else:
                counter += 1

            print("Player 2's turn")
            print("Your score is:", player_score2, "The opponent's score is:", player_score1)
            player2 = utils.turn_decision()
            if player2 == "R":
                dices = utils.roll_two_d6()
                player_score2 += dices[0]
                player_score2 += dices[1]
                print(
                    "The results:", dices[0], dices[1],
                    "sum", dices[0] + dices[1], "\n"
                    "Your total score", player_score2
                    )
                counter = 0
                if game.is_exact_100():
                    print(
                        "Victory!", "\n",
                        "Your score is equal to 100."
                    )
                    return
                if utils.is_bust():
                    print(
                        "Victory to the opponent!", "\n",
                        "Your score exceeded 100.",  "\n", 
                        "Your total score is:", player_score2
                    )
            else:
                counter += 1
                
            # אם יש 2 Pass רצוף המשחק מסתיים
            if counter >= 2:
                result = utils.closer_to_target(player_score1, player_score2)
                if result == None:
                    winner = game.tie_breaker()
                    print(
                        "Distances to 100:", "\n",
                        "player 1:", (100 - player_score1), "\n",
                        "player 2:", (100 - player_score2), "\n", 
                        "The winner is:", winner
                        ) 
                
                
play_game()