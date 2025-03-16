

available_drinks = ['espresso','latte','cappuccino']

def get_user_request():
    user_request = input('What you would like to order ? (espresso , latte, cappuccino)\n').lower()
    if user_request == 'report' or user_request == 'stop':
        return user_request


    if user_request not in available_drinks:
        user_request = get_user_request()
    else:
        return user_request

    return user_request


def get_payment():
    payment = {}
    print('Please insert coins\n')

    quarters = int(input('How many quarters ?\n'))
    payment.update({'quarter': quarters})

    dimes = int(input('How many dimes ?\n'))
    payment.update({'dime': dimes})

    nickles = int(input('How many nickles ?\n'))
    payment.update({'nickle': nickles})

    pennies = int(input('How many pennies ?\n'))
    payment.update({'penny': pennies})

    return payment

def return_change(change):
    print(f'Here is ${change} in change\n')

def serve_drink(drink):
    print(f'Here is your {drink} , Enjoy !\n')


def print_report(report):
    print(report)
