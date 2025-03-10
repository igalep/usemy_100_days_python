import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')


def print_choice(index_to_print):
    if index_to_print == 0:
        print(rock)
    elif index_to_print == 1:
        print(paper)
    else:
        print(scissors)

player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

print_choice(index_to_print=player)

computer = random.randint(0,2)
print('Computer chose:\n')
print_choice(index_to_print=computer)

if player == computer:
    print('Its a tie , try again')
elif (player == 0 and computer == 2) or\
     (player == 1 and computer == 0) or\
     (player == 2 and computer == 1):
    print('You Win !!')
else:
    print('You lose :( ')






