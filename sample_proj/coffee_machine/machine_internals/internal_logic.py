from sample_proj.coffee_machine.data.coffee_data import MENU

class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

        self.coin_value = {
            'quarter' : 0.25,
            'dime' : 0.1,
            'nickle' : 0.05,
            'penny' : 0.01
        }

        self.PROFIT = 0

    def check_available_resources(self,drink):
        '''
        :param drink: check the resources for requested drink
        :return: True if current amount of the resources is sufficient for the required drink
        '''
        required_resources = MENU.get(drink)['ingredients']

        for resource in required_resources.keys():
            if required_resources[resource] > self.resources[resource]:
                print(f'Not enough {resource}')
                return False

        return True

    def print_report(self):
        print(f'''Current machine status is:
               water: {self.resources['water']}ml
               milk: {self.resources['milk']}ml
               coffee: {self.resources['coffee']}gr
               profit: ${self.PROFIT}
               ''')


    def calculate_payment(self, payment):
        '''
        :param payment: required payment dict with all the available coins
        :return: required payment amount
        '''
        total_sum = 0
        for coin in payment.keys():
            total_sum += self.coin_value.get(coin) * payment[coin]

        return total_sum

    def check_payment(self, payment, drink):
        '''
        :param payment: payment dictionary with all the required coins for payment user insert
        :param drink: required drink
        :return: True if the inserted amount of coins >= drink's price, False otherwise
        '''
        drink_cost = MENU.get(drink)['cost']

        users_total_val = self.calculate_payment(payment=payment) #exact amount user insert

        return users_total_val - drink_cost

    def update_resources(self, drink):
        '''
        :param drink: required drink
        :return: none
        '''

        required_resources = MENU.get(drink)['ingredients']

        for ingredient , amount in required_resources.items():
            self.resources[ingredient] -= amount

    def update_profit(self, drink):
        drink_cost = MENU.get(drink)['cost']
        self.PROFIT += drink_cost