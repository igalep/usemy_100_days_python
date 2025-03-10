import random

abc_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
abc_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','@','#','$','%','^','&','*','+']


#by default , one capital
num_of_letters = int(input('How many letters for the password ?\n'))
num_of_digits = int(input('How many digits for the password ?\n'))
num_of_symbols = int(input('How many symbols for the password ?\n'))

password = [random.choice(abc_cap)]
password.extend(random.choices(abc_low, k=(num_of_letters -1)))
password.extend(random.choices(digits, k=num_of_digits))
password.extend(random.choices(symbols, k=num_of_symbols))

random.shuffle(password)

user_pass = ''.join(map(str,password))
print(f'The password for you is : {user_pass}')



