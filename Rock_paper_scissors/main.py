import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [Rock, Paper, Scissors]

num = int(input("choose 0 for Rock 1 for paper and 2 for scissors\n"))
print(f"you choose {options[num]}")


computers_choice = random.randint(0, 2)
print("computer choose :")
print(options[computers_choice])

if num == 0 and computers_choice == 2:
    print("you win")
elif computers_choice == 0 and num == 2:
    print("you loose")
elif computers_choice > num:
    print("you loose")
elif num > computers_choice:
    print("you win")
elif computers_choice == num:
    print("its a draw")
else:
    print("you typed in an invalid number")
