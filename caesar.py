import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    alphabet = string.ascii_letters
    encryption = ''
    for character in text:
        if character not in alphabet:
            encryption += character
        else:
            encryption += rotate_character(character, rot)
    return encryption



""" print(alphabet_position("c"))
print(rotate_character("a", 13))
print(rotate_character("a", 0))
print(rotate_character("c", 26))
print(encrypt("LaunchCode", 13))
print(encrypt("Hello, World!", 5)) """