logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP""" """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""" """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


def caesar(tex, shi, dir):
    if (dir == "encode"):
        t = list(tex)
        length = len(t)
        word = ""
        for i in range(0, length):
            character = t[i]
            if character in alphabet:
                position = alphabet.index(character)
                num = position + shi
                if (num <= 26):
                    word += alphabet[num]
                else:
                    num = num % 26
                    word += alphabet[num]
            else:
                word += character
        print(word)

    elif (dir == "decode"):
        word = " "
        for letter in tex:
            if letter in alphabet:
                position = alphabet.index(letter)
                num = position - shi
                if (num < 0):
                    num = 26 + num
                    word += alphabet[num]
                else:
                    word += alphabet[num]
            else:
                word += letter
        print(word)
    else:
        print("Invalid :(")


should_continue = True
while (should_continue):
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    con = input(
        "Do you want to continue encoding and decoding?type yes or no: ")
    if (con == "no"):
        should_continue = False
        print("Goodbye!!")
