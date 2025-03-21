from pandas.errors import NullFrequencyError


def add(*args,a):
    acc = 0
    for i in args:
        acc += i

    print(acc*a)

add(1,2,3,4,5,6,7,8,9,10,a=10)


def foo1(*args):
    print(args)

foo1(1,2,3)

def foo(**kwargs):
    try:
        for key,val in kwargs.items():
            print(f'key = {key} and val = {val}')
            if val > 1:
                raise Exception('General Error')
    except KeyError:
        print(1)
    else:
        print(22)
    finally:
        raise TypeError('My Error')


foo(a=3,b=2)
