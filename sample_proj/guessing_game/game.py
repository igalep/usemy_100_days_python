from game_logic import *


def play(num_of_tries):
    try_again = True
    guess = 0
    while try_again and num_of_tries > 0:
        user_input = int(input('Make a guess :\n'))
        guess += 1
        num_of_tries -= 1

        current_guess = compare_to_input(user_input)

        if current_guess == WELL_DONE:
            try_again = False

        print(f'you made {guess} guesses out of {num_of_tries + guess}')
        print(current_guess)

    if num_of_tries == 0:
        print('You lost !!')



logo = (r'''
  ______                                                                                                   __                           
 /      \                                                                                                 |  \                          
|  $$$$$$\ __    __   ______    _______   _______         ______         _______   __    __  ______ ____  | $$____    ______    ______  
| $$ __\$$|  \  |  \ /      \  /       \ /       \       |      \       |       \ |  \  |  \|      \    \ | $$    \  /      \  /      \ 
| $$|    \| $$  | $$|  $$$$$$\|  $$$$$$$|  $$$$$$$        \$$$$$$\      | $$$$$$$\| $$  | $$| $$$$$$\$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\
| $$ \$$$$| $$  | $$| $$    $$ \$$    \  \$$    \        /      $$      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$    $$| $$   \$$
| $$__| $$| $$__/ $$| $$$$$$$$ _\$$$$$$\ _\$$$$$$\      |  $$$$$$$      | $$  | $$| $$__/ $$| $$ | $$ | $$| $$__/ $$| $$$$$$$$| $$      
 \$$    $$ \$$    $$ \$$     \|       $$|       $$       \$$    $$      | $$  | $$ \$$    $$| $$ | $$ | $$| $$    $$ \$$     \| $$      
  \$$$$$$   \$$$$$$   \$$$$$$$ \$$$$$$$  \$$$$$$$         \$$$$$$$       \$$   \$$  \$$$$$$  \$$  \$$  \$$ \$$$$$$$   \$$$$$$$ \$$      
                                                                                                                                      
''')

print(logo)

level = int(input('Guess game , hard (1) or easy (2) ? *default is easy* '))
if  level == 1:
    level = 5
else:
    level = 10

get_random()
play(num_of_tries=level)











