import string

def alphabet_position(char):
    alphabet = string.ascii_lowercase
    #alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    alphaDict = {}
    char = char.lower()
    for letter_key in alphabet:
        alphaDict[letter_key] = counter
        counter += 1
    if char in alphaDict:
        return alphaDict[char]

def rotate_character(char, rot):
    alphabet = string.ascii_lowercase
    #alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    alphaDict = {}
    origin_char = char
    char = char.lower()
    for letter_key in alphabet:
        alphaDict[letter_key] = counter
        counter += 1
    letter = alphabet_position(char)
    new_letter_position = (letter + rot) % 26
    new_letter = "a"
    for letter_key in alphabet:
        if alphaDict[letter_key] == new_letter_position:
            new_letter = letter_key
            if origin_char.islower() == True:
                return new_letter.lower()
            elif origin_char.isupper() == True:
                return new_letter.upper()
