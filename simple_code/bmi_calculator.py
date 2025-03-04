weight = 75
height = 1.74


bmi = weight / height ** 2
print(f'The BMI is {bmi}')
print(f'Round (floor) BMI is {int(bmi)}')
print(f'Round (ceiling) BMI is {round(bmi)}')

print(f'Round (ceiling + n_digit) BMI is {round(bmi, 2)}')