

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiple(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    if n2 == 0:
        return ZeroDivisionError

    return  n1 / n2

math_operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiple,
    '/' : divide
}