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