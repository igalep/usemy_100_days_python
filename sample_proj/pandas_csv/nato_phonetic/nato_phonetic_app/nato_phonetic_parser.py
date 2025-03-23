import pandas
from sample_proj.pandas_csv.nato_phonetic.nato_phonetic_app.helper.io import get_file_path as path


CSV = None
PHONETIC_MAP = []

def read_data():
    file_name = 'nato_alphabet.csv'
    csv_content = pandas.read_csv(path(file_name=file_name))

    # print(csv_content)

    return csv_content


def map_phonetic(csv_content):
    # for (index, row) in csv_content.iterrows():
    #     print(f'{row.letter} --> {row.code_word}')

    mapping = {row.letter:row.code_word for (index, row) in csv_content.iterrows()}

    # print(mapping)

    return mapping


def boot_strup():
    global CSV
    CSV = read_data()
    global PHONETIC_MAP
    PHONETIC_MAP = map_phonetic(csv_content=CSV)

def parser(user_input):
    n_list = []
    try:
        phonetic_list = [PHONETIC_MAP[item] for item in user_input]
        phonetic_list = pandas.Series(phonetic_list).dropna().to_list()

        return phonetic_list
    except KeyError as e:
        return f'No special characters are allowed for example - "{e.args[0]}"'

def game_on():
    loop = True
    boot_strup()

    while loop:
        user_name = input('Insert a word for conversion to phonetic:\n').upper()
        if user_name == 'stop'.upper():
            loop = False
            continue

        char_list = list(user_name)

        parser_return = parser(user_input= char_list)

        print(parser_return)

def main():
    game_on()


if __name__ == '__main__':
    main()



