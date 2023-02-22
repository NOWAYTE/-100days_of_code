import random
from art import logo

LEVEL_EASY = 10
LEVEL_DIFFICULTY = 5


def difficulty_level():
    game_level = input("choose a difficulty. Type 'easy' or 'hard'").lower()
    if game_level == "easy":
        return LEVEL_EASY
    else:
        return LEVEL_DIFFICULTY


def compare(guess, computer_number, turns):
    if guess > computer_number:
        print("Too High")
        return turns - 1
    elif guess < computer_number:
        print("Too Low ")
        return turns - 1
    else:
        print(f"you have got it The number is {computer_number}")


def game():
    print(logo)
    print("Welcome to the number guessing game!\n I am thinking of a number between 1 and 100 ")

    computer_number = random.randint(1, 100)
    print(f"The number is {computer_number}")

    turns = difficulty_level()
    guess = 0

    while guess != computer_number:
        print(f"The number of attempts remaining is {turns}")
        guess = int(input("Make a guess"))
        turns = compare(guess, computer_number, turns)

        if turns == 0:
            print("you have run out of attempts")
            return
        elif guess != computer_number:
            print("guess again")


game()
