from user_interface.user_prompts import UserPrompts
from machine_internals.internal_logic import CoffeeMachine


def machine_on():
    up = UserPrompts()
    logic = CoffeeMachine()

    on = True
    while on:
        user_request = up.get_user_request()

        if user_request == 'stop':
            on = False
            continue

        if user_request == 'report':
            logic.print_report()
        else:
            required_resources = logic.check_available_resources(drink=user_request)

            if not required_resources:
                print('Please try again')
                continue
            else:
                payment = up.get_payment()

                change = logic.check_payment(payment=payment, drink=user_request)

                if change >= 0: #user insert enough money
                    up.serve_drink(drink=user_request)
                    logic.update_resources(drink=user_request)
                    logic.update_profit(drink=user_request)
                    if change > 0:
                        print(f'Your change is {round(change,2)}')

                    up.serve_drink(user_request)
                else:
                    print(f'''Sorry not enough money to purchase {user_request}, you are missing ${round(change * -1,2)}
                    Money refunded.
                    ''')






def main():
    machine_on()


if __name__=="__main__":
    main()