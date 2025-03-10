pizza_size = input('What size of pizza ? ( S / M / L )\n')
paperoni = input('Do you want paperoni ? (Y/N)\n')
extra_cheese = input('Do you want extra cheese? (Y/N)\n')
pizza_price = 0


if extra_cheese == 'Y':
    pizza_price += 1

if pizza_size == 'S':
    pizza_price = 15
elif pizza_size == 'M':
    pizza_price = 20
else:
    pizza_price = 25

if paperoni == 'Y':
    if pizza_size == 'S':
        pizza_price += 2
    else:
        pizza_price += 3

print(f'Final pizza cost is : {pizza_price}')

