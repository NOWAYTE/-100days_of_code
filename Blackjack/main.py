import random
# from replit import clear
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # clear()
    play_game()

# import random
#
#
# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
#
# deal_card()
#
#
# def calculator_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards):
#         cards.remove(11)
#         cards.append(1)
#
#     return sum(cards)
#
#
# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return "Draw"
#     elif computer_score == 0:
#         return "You lose, opponent has a blackjack"
#     elif user_score == 0:
#         return "Win with a blackjack"
#     elif user_score > 21:
#         return "your score is above 21. ypu lose"
#     elif computer_score > 21:
#         return "opponent score is above 21. you win"
#     elif user_score > computer_score:
#         return "You win"
#     else:
#         return "You lose"
#

#
# def play_game():
#     user_cards = []
#     computer_cards = []
#     is_game_over = False
#
#     for i in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#
#     while not is_game_over:
#         user_score = calculator_score(user_cards)
#         computer_score = calculator_score(computer_cards)
#
#         print(f"Your cards are : {user_cards} and current_score : {user_score}")
#         print(f"Computer first card is {computer_cards}")
#
#         if user_cards == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_continue = input("type y to continue and n to pass")
#
#             if user_should_continue == "y":
#                 user_cards.append(deal_card())
#
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculator_score(computer_cards)
#
#     print(compare(user_score, computer_score))
#     while input("do you want to play the blackjack") == "y":
#         play_game()
