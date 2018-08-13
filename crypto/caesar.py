from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    text = list(text)

    hashed = ''.join([rotate_character(letter, rot) for letter in text])

    return hashed

def main():
    word = input('Type a message:\n')
    rotate = int(input('Rotate by:\n'))
    print(encrypt(word, rotate))

if __name__ == '__main__':
    main()
