from xml.etree.ElementPath import prepare_parent

from sample_proj.coffee_machine.data.coffee_data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coin_value = {
    'quarter' : 0.25,
    'dime' : 0.1,
    'nickle' : 0.05,
    'penny' : 0.01
}

PROFIT = 0

def check_available_resources(drink):
    '''
    :param drink: check the resources for requested drink
    :return: True if current amount of the resources is sufficient for the required drink
    '''
    required_resources = MENU.get(drink)['ingredients']

    for resource in required_resources.keys():
        if required_resources[resource] > resources[resource]:
            print(f'Not enough {resource}')
            return False

    return True

def calculate_payment(payment):
    '''
    :param payment: required payment dict with all the available coins
    :return: required payment ammoutn
    '''
    total_sum = 0
    for coin in payment.keys():
        total_sum += coin_value.get(coin) * payment[coin]

    return total_sum

def check_payment(payment, drink):
    '''
    :param payment: payment dictionary with all the required coins for payment user insert
    :param drink: required drink
    :return: True if the inserted amount of coins >= drink's price, False otherwise
    '''
    drink_cost = MENU.get(drink)['cost']

    users_total_val = calculate_payment(payment=payment) #exact amount user insert

    return users_total_val - drink_cost

def update_resources(drink):
    '''
    :param drink: required drink
    :return: none
    '''

    required_resources = MENU.get(drink)['ingredients']

    for ingredient , amount in required_resources.items():
        resources[ingredient] -= amount

def update_profit(drink):
    global PROFIT
    drink_cost = MENU.get(drink)['cost']
    PROFIT += drink_cost