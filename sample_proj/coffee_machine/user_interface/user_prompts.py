class UserPrompts:
    def __init__(self):
        self.available_drinks = ['espresso','latte','cappuccino']

    def get_user_request(self):
        user_request = input('What you would like to order ? (espresso , latte, cappuccino)\n').lower()
        if user_request == 'report' or user_request == 'stop':
            return user_request


        if user_request not in self.available_drinks:
            user_request = self.get_user_request()
        else:
            return user_request

        return user_request


    def get_payment(self):
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

    def return_change(self,change):
        print(f'Here is ${change} in change\n')

    def serve_drink(self,drink):
        print(f'Here is your {drink} , Enjoy !\n')
