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

list = [rock,paper,scissors]

import random

you = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors."))
if you >= 3 or you <= 0:
  print("You typed in an invalid number, you lose!")
else:
  print("You chose")
  print(list[you])
  computer = random.randint(0,2)
  print("Computer chose")
  print(list[computer])

  if you == computer:
    print("Tie!")
  elif you - computer == 1 or you - computer == -2 :
    print("You win!")
  else:
    print("You lose!")
