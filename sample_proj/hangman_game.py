import random

word_list = [
    "ant",
    "tree",
    "blue",
    "plant",
    "frog",
    "light",
    "road",
    "stone",
    "song",
    "dream",
    "world",
    "eyes",
    "space",
    "heart",
    "wind",
    "beach",
    "desk",
    "table",
    "keys",
    "books"
]
game_stages = [r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

def play_game():
    word_to_guess = random.choice(word_list)
    word_length = len(word_to_guess)
    masked_word = '_' * word_length

    correct_letters = set()

    #print(word_to_guess)
    print(f'{masked_word}\n')

    game_over = False
    num_of_tries = 6 #configurable
    stage = 1

    while not game_over and num_of_tries > 0:
        new_string = ''
        correct_char = False
        char = input('Guess a letter\n').lower()

        if char in correct_letters:
            print('This letter was already discovered')
            continue

        for letter in word_to_guess:
            if letter == char:
                new_string += char
                correct_letters.add(letter)
                correct_char = True

            elif letter in correct_letters:
                new_string += letter
            else:
                new_string += '_'

        print(new_string)

        if '_' not in new_string:
            game_over = True
            print('You win !')

        if not correct_char:
            print(game_stages[abs(num_of_tries - len(game_stages))])
            num_of_tries -= 1
            print(f'****************************{num_of_tries}/{num_of_tries + stage} LIVES LEFT****************************')
            stage +=1

        if num_of_tries == 0:
            print('You lose !')




def main():
    welcome = (r'''
                  | |                                            
                  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                  | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
                  | | | | (_| | | | | (_| | | | | | | (_| | | | |
                  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                      __/ |                      
                                     |___/' ''')

    initial_state = r'''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''

    print(f'{welcome}\n')
    # print(initial_state)
    play_game()


if __name__ == '__main__':
    main()