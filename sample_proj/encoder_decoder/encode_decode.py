

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def crypto(org_text, offset, encoder_decoder): # encoder = 1 , decoder =-1
    org_text = org_text.lower()

    new_string = []
    for letter in org_text:
        if letter == ' ':
            new_string.append(' ')
            continue

        index = abc.index(letter)

        new_string.append(abc[(index + (encoder_decoder * offset)) % len(abc)])  # 0-25

    return ''.join(new_string)



print(r'''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
''')

encode_decode = input('Would you like to encode or decode ?\n').lower()
original_text = input(f'Enter original code you would like to {encode_decode}\n')
offset = int(input(f'Enter the offset for {encode_decode[:-1]}ing you would like to do: \n'))

new_string = crypto(org_text=original_text, offset=offset, encoder_decoder= 1 if encode_decode == 'encode' else -1)

print(f"The {encode_decode}d text is : {new_string}")
