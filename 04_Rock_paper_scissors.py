rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

computer_choose = random.randint(0,2)
user_choose = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor.\n"))

if user_choose > 2:
    print("Please choose valid input.")
else:
    if user_choose == 0:
        print(rock)
    elif user_choose == 1:
        print(paper)
    else:
        print(scissors)

    if computer_choose == 0:
        print("Computer choose:\n", rock)
    elif computer_choose == 1:
        print("Computer choose:\n", paper)
    else:
        print("Computer choose:\n", scissors)

    if computer_choose == 0:
        if user_choose == 1:
            print("You win!")
        elif user_choose == 2:
            print("You lose!")
        else:
            print("It's Draw!")
    elif computer_choose == 1:
        if user_choose == 2:
            print("You win!")
        elif user_choose == 0:
            print("You lose!")
        else:
            print("It's Draw!")
    else:
        if user_choose == 0:
            print("You win!")
        elif user_choose == 1:
            print("You lose!")
        else:
            print("It's Draw!")
