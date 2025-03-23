'''  Basic PIG
PIG is a game for 2 to 6 players.

Players take turns with a die.
On a player’s turn he/she can roll a die as many times as they like.
If a roll is a 2, 3, 4, 5, or 6, the player adds that many points to their score for the turn.
A player may choose to end their turn at any time and “bank” their points.
If a player rolls a 1, they lose all their unbanked points and their turn is over.
Beginner’s Game: The first player to score 50 or more points wins.
Advanced Game: The first player to score 100 or more points wins. '''

from random import randrange, seed


def roll():
    dice = randrange(1, 7)
    return dice

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Invalid Input!")
    else:
        print("Invalid Input!")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer Number ", player_idx + 1, " turn has just started!")
        print("Your total score is: ", player_scores[player_idx], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your current score is: ", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player Number {winning_idx + 1}, is the winner with the score of {max_score}")
