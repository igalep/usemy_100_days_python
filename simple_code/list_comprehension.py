# Get item from dict
def get_name_by_id(name):
    user = [
        {'id': 0, 'name':'A'},
        {'id': 1, 'name':'B'},
        {'id': 2, 'name':'C'},
        {'id': 3, 'name':'D'},
        {'id': 4, 'name':'F'}
    ]
    new_dict = {item['name']:item['id'] for item in user}

    print(new_dict.get(name))
get_name_by_id('B')


# Generate a List of Squares
def list_of_squares(org_list):
    n_list = [i**2 for i in org_list]
    print(n_list)
list_of_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


#Filter Even Numbers
def get_even(org_list):
    n_list = [i for i in org_list if i % 2 == 0]
    print(n_list)
get_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


#Convert Celsius to Fahrenheit
def convertion_c_f(org_list):
    #(C * 9/5) + 32

    n_list = [(item * (9/5) + 32) for item in org_list]
    print(n_list)
convertion_c_f([0, 10, 20, 30, 40])


#Get First Letter of Each Word
def get_first(org_list):
    n_list = [word[:1] for word in org_list]
    print(n_list)
get_first(["apple", "banana", "cherry", "date"])


#Remove Vowels from a List of Strings
def remove_vowels(org_list):
    vowels = 'aeiouAEIOU'

    new_word = [''.join([c for c in word if c not in vowels]) for word in org_list]

    print(new_word)
remove_vowels(["hello", "world", "python"])

#Create a List of Word Lengths
def word_len(org_list):
    n_list = [len(word) for word in org_list]
    print(n_list)
word_len(["hi", "hello", "world"])

#Find Words Containing a Specific Letter (e)
def specific_letter(org_list):
    letter = 'e'

    n_list = [word for word in org_list if letter in word]
    print(n_list)
specific_letter(["apple", "banana", "cherry", "date", "fig", "grape"])

#Replace Negative Numbers with Zero
def replace_negative(org_list):
    n_list = ['xx' if i < 0 else i for i in org_list]
    print(n_list)
replace_negative([4, -3, 2, -1, 0, -7, 8])

#Extract Digits from a String
def extract_digits(org_list):
    n_list = [c for c in org_list if c.isdigit()]
    print(n_list)
extract_digits("abc123def45gh6")

#Find Common Elements in Two Lists
def find_common(first_l, second_l):
    n_list = [x for x in first_l if x in second_l]
    print(n_list)
find_common(first_l=[1, 2, 3, 4, 5], second_l=[3, 4, 5, 6, 7])


# Capitalize the First Letter of Each Word
def capitalize(org_list):
    n_list = [w.capitalize() for w in org_list]
    print(n_list)
capitalize(["hello", "world", "python", "is", "fun"])


#Flatten a 2D List (Matrix) into a 1D List
def flatten(org_list):
    n_list = [i for row in org_list for i in row]
    print(n_list)
flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# Square of Numbers as Dictionary
def dict_square(org_list):
    n_list = {i:i**2 for i in org_list}
    print(n_list)
dict_square([1,2,3,4,5,6,7,8,9,10])

#Create a Dictionary from Two Lists
def dict_from_list(first_l, second_l):
    n_dict = {k:v for k,v in zip(first_l,second_l)}
    print(n_dict)
dict_from_list(first_l=['a', 'b', 'c', 'd', 'e'], second_l=[1, 2, 3, 4, 5])


#Filter Dictionary by Values
def filter_by_val(org_dict):
    n_dict = {name:score for name,score in org_dict.items() if score >80}
    print(n_dict)
filter_by_val({"Alice": 85, "Bob": 60, "Charlie": 90, "David": 45})

#Reverse Key-Value Pairs
def reverse(org_dict):
    n_dict = {val:key for key,val in org_dict.items()}
    print(n_dict)
reverse({"a": 1, "b": 2, "c": 3})


# Count Character Occurrences in a String
def count_char(word):
    n_dict = {c:word.count(c) for c in set(word)}
    print(n_dict)
count_char('hello')