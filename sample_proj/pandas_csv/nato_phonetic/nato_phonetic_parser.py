import pandas
from helper.io import get_file_path as path


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

def game_on():
    loop = True
    csv = read_data()
    phonetic_map = map_phonetic(csv_content=csv)

    while loop:
        user_name = input('Insert a word for conversion to phonetic:\n').upper()
        if user_name == 'stop'.upper():
            loop = False
            continue

        char_list = list(user_name)
        try:
            phonetic_list = [phonetic_map[item] for item in char_list]
            phonetic_list = pandas.Series(phonetic_list).dropna().to_list()

            print(phonetic_list)
        except KeyError as e:
            print(f'No special characters are allowed for example - "{e.args[0]}"')



def main():
    game_on()


if __name__ == '__main__':
    main()



