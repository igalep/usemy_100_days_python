import random

number_to_guess = -1

WELL_DONE = 'Well done !\n'

def get_random():
    global number_to_guess

    number_to_guess = random.randint(1,100)


def compare_to_input(user_input):
    if user_input > number_to_guess:
        return 'Too high.\n'
    elif user_input < number_to_guess:
        return 'Too low.\n'
    else:
        return WELL_DONE
