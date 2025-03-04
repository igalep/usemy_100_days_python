total_bill = float(input('What was the total bill ?\n'))
tip_amount = int(input('How much tip you would like to add ? (10 / 12 / 15)\n'))
num_of_ppl = input('How many people to split the bill ?\n')

total_with_tip = total_bill * ((tip_amount / 100) + 1)
bill_per_person = total_with_tip / int(num_of_ppl)

print(f'Each person should pay {round(bill_per_person, 2)}')