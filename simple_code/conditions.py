num = int(input('Enter number :\n'))

if num % 2 == 0:
    print('You entered an even number')
else:
    print('You entered an odd number\n\n')




age = int(input('What is your age ?\n'))
height = int(input('What is your height ?\n'))


if age < 10:
    print('You are too small')
elif height > 150:
    print('You are to high :(')
elif height > 140:
    print('You can go')
elif height > 120:
    print('You can go with your parents')
else:
    print('You cannot go')