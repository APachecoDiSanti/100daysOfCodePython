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

#Write your code below this line 👇
import random

moves = [rock, paper, scissors]
choice = int(input("What do you choose?\n0: Rock\n1: Paper\n2: Scissors\n"))

if choice > 2 or choice < 0:
    print("INVALID MOVE! YOU LOSE!")
else:
    print("Your move:")
    print(moves[choice])

    pc_choice = random.randint(0, 2)
    print("PC's move:")
    print(moves[pc_choice])

    if (pc_choice == choice):
        print("YOU DRAW!")
    elif pc_choice == ((choice + 1) % 3):
        print("YOU LOSE!")
    else:
        print("YOU WIN!")        
