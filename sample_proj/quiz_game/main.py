from game.game_logic import GameLogic

def main():
    game = GameLogic()
    while game.has_question():
        game.ask_next_question()

    print(f'You answered correctly on {game.get_score()} questions')



if __name__== "__main__":
    main()


