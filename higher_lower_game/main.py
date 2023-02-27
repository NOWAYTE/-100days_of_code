import random

from art import logo, vs
from game_data import data

# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     }
# ]
print(logo)

score = 0

game_continue = False

while not game_continue:
    def compare(compare):
        account_name = compare["name"]
        account_description = compare["description"]
        account_country = compare["country"]

        return f"{account_name} , a {account_description} , {account_country}"


    def followers(choice, a_follower_count, b_follower_count):
        if a_follower_count > b_follower_count:
            return choice == "a"
        else:
            return choice == "b"


    compare_A = random.choice(data)
    compare_B = random.choice(data)

    if compare_A == compare_B:
        compare_A = random.choice(data)

    print(f" Compare A {compare(compare_A)}")
    print(vs)
    print(f"Against B {compare(compare_B)}")

    choice = input("who has more followers, Type 'A' or 'B' ").lower()

    a_follower_count = compare_A["follower_count"]
    b_follower_count = compare_B["follower_count"]

    answer = followers(choice, a_follower_count, b_follower_count)
    print(answer)

    if answer:
        score += 1
        print(f"That is correct Your current score is {score}")
    else:
        print(f"Sorry that is not correct , your score is {score}")
