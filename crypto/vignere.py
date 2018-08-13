from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    text = list(text)
    key = list(key)
    counter = 0
    result = ''
    rot_amount = [alphabet_position(letter) for letter in key]

    for i in text:
        if counter >= len(key):
            counter = 0
        if i.isalpha():
            result += rotate_character(i, rot_amount[counter])
            counter += 1
        else:
            result += i

    return result

def main():
    user = input('Type a message:\n')
    pw = input('Encryption key:\n')
    print(encrypt(user, pw))

if  __name__ == '__main__':
    main()
