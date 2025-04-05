import random

COLORS = ["R", "G","B","Y","W","O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))
    return code


def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != CODE_LENGTH:
            print(f"You Must Guess {CODE_LENGTH} Colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid Color: {color}. Try Again!")
                break

        else:
            break
    return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome To MasterMind, You Have {TRIES} Tries To Guess The Code...")
    print("The Valid Colors Are: ", *COLORS)
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        if correct_pos == CODE_LENGTH:
            print(f"You Guessed The Code In {attempts} Tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect positions: {incorrect_pos}")
    else:
        print("You Ran Out Of Tries... The Code Was: ", *code)

if __name__ == "__main__":
    game()
