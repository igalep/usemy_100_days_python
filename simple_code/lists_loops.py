# state_of_america = ['CA', 'NJ', 'AL', 'Fl','VI']
#
# state_of_america.sort()
#
# print(state_of_america)
# print(state_of_america[:-1])
#
# state_of_america.append('GE')
# print(state_of_america)

import random as r

name_list = ['Alice' , 'Bob', 'David', 'Emanuel', 'Linda']

name = r.choice(name_list)
print(name)

r_name = name_list[r.randint(0, len(name_list) - 1)]
print(r_name)



num_list = [1,2,3,4,5,6,7,8,9,423,234232,423,423,543,34,546,876,3467,8809]

print(sum(num_list))
print(min(num_list))
print(max(num_list))
max = -1
for num in num_list:
    if max < num:
        max = num
print(max)

total = 0
for i in range(1, 101):
    total += i
print(total)
