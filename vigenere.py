import string
from helpers import alphabet_position, rotate_character

def encrypt(text, crypt):
    alphabets = string.ascii_letters
    encryption = ''
    rot = 0
    indexCounter = 0
    cryptList = []
    #Insert encryption key portion here
    for letter in crypt:
        rot = alphabet_position(letter)
        cryptList.append(rot)

    for character in text:
        rot = cryptList[indexCounter]
        if character not in alphabets:
            encryption += character
        else:
            encryption += rotate_character(character, rot)
            indexCounter += 1
        if indexCounter == len(cryptList):
            indexCounter = 0
    return encryption

""" def encrypt(text, crypt):
    alphabet = string.ascii_letters
    crypt_key = {}

    for char in crypt:
        rot_num = alphabet_position(char)
        crypt_key[char] = rot_num
    encryption = ''
    for character in text:
        if character not in alphabet:
            encryption += character
            counter += 1
            if counter == len(crypt):
                counter = 0
        else:
            for key in crypt:
                encryption += rotate_character(character, key)
                continue
    return encryption """

def main():
    input_text = str(input("Type a message: "))
    encryption_key = str(input("Encryption key: "))
    print(encrypt(input_text, encryption_key))

if __name__ == '__main__':
    main()




""" print(alphabet_position("c"))
print(rotate_character("a", 13))
print(rotate_character("a", 0))
print(rotate_character("c", 26))
#print(encrypt("LaunchCode", 13))
print(encrypt("The crow", "boom")) """