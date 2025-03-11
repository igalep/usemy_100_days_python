def calc_score_per_word(word , name):
    score = sum(word.count(letter) for letter in name)

    return score



def calculate_love_score(name1, name2):
    word_a = 'true'
    word_b = 'love'

    name_combined = (name1.lower() + name2.lower()).replace(' ','')

    score_a = calc_score_per_word(word=word_a, name=name_combined)
    score_b = calc_score_per_word(word=word_b, name=name_combined)

    return score_a * 10 + score_b

total_score = calculate_love_score(name1='Kanye West', name2='Kim Kardashian')
print(f'The love score is: {total_score}')