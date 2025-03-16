import user_interface.user_prompts as up
import machine_internals.internal_logic as logic


def machine_on():
    flag = True
    while flag:
        user_request = up.get_user_request()

        if user_request == 'stop':
            flag = False
            continue

        if user_request == 'report':
            print(f'''Current machine status is:
        water: {logic.resources['water']}
        milk: {logic.resources['milk']}
        coffee: {logic.resources['coffee']}
        profit: ${logic.PROFIT}
        ''')
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







machine_on()