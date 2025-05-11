import time

def speed_calc_decorator(func):
    def inner_func():
        start_time = time.time()
        result = func()
        end_time = time.time()

        print(f'Function {func.__name__} run time was {end_time - start_time}s')

        return result

    return inner_func


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()

print('------------------')


def logging_decorator(func):
    def wrapper(*args):
        print(f'You called {func.__name__}{args}')
        result = func(*args)
        print(f'It returned: {result}')
        return result

    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)