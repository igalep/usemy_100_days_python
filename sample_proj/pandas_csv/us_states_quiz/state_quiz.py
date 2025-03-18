from view.view import View
from logic.states_data import StateData

def main():
    v = View()
    game_logic = StateData()


    game_on = True
    correct_states = 0
    user_input = None
    while game_on:
        user_input_exists = False
        while not user_input_exists:
            user_input = v.get_state_from_user(correct=correct_states)

            if user_input.lower() == 'stop':
                game_on = False
                user_input_exists = True
                continue

            user_input_exists = game_logic.validate_input_state(input_state=user_input)

        state_data = game_logic.find_state_coordinate(user_input=user_input)
        v.mark_on_map(coordinate=state_data)
        correct_states += 1

        if correct_states == 50:
            game_on = False


    v.exit()




if __name__ == '__main__':
    main()