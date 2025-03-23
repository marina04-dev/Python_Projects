import random   # For randint.
import json     # For saving the highest score.
import time     # To calculate the time spent on each question.

# Dummy score when the game has not been played at all.
dummy_score = {'Player Name': 'Anonymous', 'Score': 0}

filename = 'highest_score.json'

# Read into the high score file to print the high score and high scorer's name.
try:
    with open(filename) as highest_score:
        high_score = json.load(highest_score)

    highest_score.close()

    # The try ... except block is used when the game is yet to be played and the high score file has not been created.
    # When the high score has not been created, the dummy score is used.
except FileNotFoundError:
    high_score = dummy_score

# Print High Score.
# '\033[7;32;40m' - Green background and black text.
print('\033[7;32;40m' + 'High score' '\033[0;0m\n' + high_score['Player Name'] + ': ' + str(high_score['Score']) + '\n')

player_name = input("Name: ").title()

# List of operators used in the game
operators = ['*', '/', '+', '-']
random_operator = operators[random.randint(0, 3)]

player_lives = 3
player_score = 0

# '\033[0;31;40m' - Black background, red text.
print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')


def operation(random_op1, random_op2, game_seconds):
    """Checks if the player's answer is correct within the given time."""

    # To change the global variable, the 'global' keyword is used.
    global player_lives
    global player_score
    start_time = time.time()
    player_answer = ""

    print('You have ' + str(game_seconds) + ' seconds')

    while player_answer == "":
        # try ... except to catch ValueError
        try:
            # This prints out the algebraic operation to the screen
            print(str(random_op1) + str(random_operator) + str(random_op2))
            player_answer = int(input("Answer: "))
        except ValueError:
            print('\033[0;31;40m' + 'Invalid input! Input an integer.' + '\033[0;0m')
            continue

    # Check if the question was answered before the time elapsed.
    time_used = int(time.time() - start_time)
    remaining_sec = game_seconds - time_used

    if remaining_sec <= 0:
        print('Time up!\n')
        player_lives = player_lives - 1
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    # MULTIPLICATION
    elif random_operator == operators[0]:
        if player_answer == random_op1 * random_op2:
            player_score = player_score + (remaining_sec * 10)
            print('Player score:', player_score, '\n')

        else:
            print('Wrong! The answer is ' + str(random_op1 * random_op2) + '\n')
            player_lives = player_lives - 1
            print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    # DIVISION
    elif random_operator == operators[1]:
        if player_answer == random_op1 / random_op2:
            player_score = player_score + (remaining_sec * 10)
            print('Player score:', player_score, '\n')

        else:
            print('Wrong! The answer is ' + str(int(random_op1 / random_op2)) + '\n')
            player_lives = player_lives - 1
            print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    # ADDITION
    elif random_operator == operators[2]:
        if player_answer == random_op1 + random_op2:
            player_score = player_score + (remaining_sec * 10)
            print('Player score:', player_score, '\n')

        else:
            print('Wrong! The answer is ' + str(random_op1 + random_op2) + '\n')
            player_lives = player_lives - 1
            print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    # SUBTRACTION
    elif random_operator == operators[3]:
        if player_answer == random_op1 - random_op2:
            player_score = player_score + (remaining_sec * 10)
            print('Player score:', player_score, '\n')

        else:
            print('Wrong! The answer is ' + str(random_op1 - random_op2) + '\n')
            player_lives = player_lives - 1
            print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')


# The game continues so long the player's life does not deplete to 0.
while player_lives > 0:

    # LEVEL: Very Easy
    game_sec1 = 10

    while player_score < 1500 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand1 = random.randint(0, 9)
        random_operand2 = random.randint(1, 9)  # This starts from 1 to avoid ZeroDivisionError.

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers).
        if (random_operator == operators[1]) and (random_operand1 % random_operand2 != 0):
            continue

        # Calling the operation function.
        operation(random_operand1, random_operand2, game_sec1)

    # LEVEL: Easy
    if player_score > 1500:
        player_lives = player_lives + 2
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    while player_score >= 1500 and player_score < 3500 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand3 = random.randint(0, 99)
        random_operand4 = random.randint(1, 20)  # This starts from 1 to avoid ZeroDivisionError.
        game_sec2 = 15

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers).
        if (random_operator == operators[1]) and (random_operand3 % random_operand4 != 0):
            continue

        # Calling the operation function.
        operation(random_operand3, random_operand4, game_sec2)

    # LEVEL: Medium
    if player_score > 3500:
        player_lives = player_lives + 2
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    while player_score >= 3500 and player_score < 10000 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand5 = random.randint(0, 99)
        random_operand6 = random.randint(1, 50)  # This starts from 1 to avoid ZeroDivisionError.
        game_sec3 = 20

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers).
        if (random_operator == operators[1]) and (random_operand5 % random_operand6 != 0):
            continue

        # Calling the operation function.
        operation(random_operand5, random_operand6, game_sec3)

    # LEVEL: Hard
    if player_score > 10000:
        player_lives = player_lives + 3
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    while player_score >= 10000 and player_score < 25000 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand7 = random.randint(0, 999)
        random_operand8 = random.randint(1, 100)  # This starts from 1 to avoid ZeroDivisionError.
        game_sec4 = 25

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers).
        if (random_operator == operators[1]) and (random_operand7 % random_operand8 != 0):
            continue

        # Calling the operation function
        operation(random_operand7, random_operand8, game_sec4)

    # LEVEL: Very Hard
    if player_score > 25000:
        player_lives = player_lives + 5
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    while player_score > 25000 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand9 = random.randint(0, 999)
        random_operand10 = random.randint(1, 400)  # This starts from 1 to avoid ZeroDivisionError.
        game_sec5 = 30

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers).
        if (random_operator == operators[1]) and (random_operand9 % random_operand10 != 0):
            continue

        # Calling the operation function.
        operation(random_operand9, random_operand10, game_sec5)

if player_lives == 0:
    print('Game Over!\n')
    print('\033[0;33;40m' + 'Your score: ' + str(player_score) + '\033[0;0m')

# Check if the player’s score is greater than the high score
if player_score > high_score['Score']:
    high_score['Score'] = player_score
    high_score['Player Name'] = player_name

    with open(filename, 'w') as highest_score:
        json.dump(high_score, highest_score)

    highest_score.close()

    print('\033[30;32;40m' + 'New High Score!' + '\033[0;0m')

# TODO: Break out of the question if the time elapses before the player enters an answer.
