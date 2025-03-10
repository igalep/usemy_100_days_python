import random



random_num = random.random() * 10
print(random_num)

random_int = random.randint(1,12)
print(random_int)

random_float = random.uniform(21,45)
print(random_float)


h_t = random.randint(0,1)
if h_t == 0:
    print('Head')
else:
    print('Tail')

