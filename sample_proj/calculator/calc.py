from math_operations import math_operations as operations





def calc(n1 , n2, op):
    return operations.get(op)(n1=n1 , n2=n2)

math_op = ['+' , '-', '*' , '/']

def play():
    first_arg = int(input('What is your first arg ?\n'))
    use_prev = True

    while use_prev:
        user_op = input('''What you would like to do ? (+ , - , * , /) ?
        *default will be (+)*\n''')

        if user_op not in math_op:
            user_op = math_op[0]

        second_arg = int(input('What is your second arg ?\n'))

        result = calc(n1=first_arg, n2=second_arg, op=user_op)

        print(f'The result of {first_arg} {user_op} {second_arg} is : {result}')

        user_input = input('''Would you like to calculate with previous result (y) or start a new calculation (c) ? 
                             *default is to use previous result*\n''')

        first_arg = result

        if user_input == 'c':
            play()




logo = (r'''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

print(logo)
play()