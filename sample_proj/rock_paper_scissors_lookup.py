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

items_mapping = {
    0 : 'rock',
    1 : 'paper',
    2 : 'scissors'
}

winning_map = {
    'rock' : 'scissors',
    'scissors' : 'paper',
    'paper' : 'rock'
}

items_printing = [rock, paper, scissors]






def print_choice(index_to_print):
  print(items_printing[index_to_print])

player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

print_choice(index_to_print=player)
players_item = items_mapping.get(player)

computer = random.randint(0,2)
print('Computer chose:\n')
print_choice(index_to_print=computer)
computers_item = items_mapping.get(computer)

if player == computer:
    print('Its a tie , try again')
elif winning_map.get(players_item) == computers_item:
    print('You Win !!')
else:
    print('You lose :( ')





