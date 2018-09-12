def alphabet_position(letter):
    a = list(map(chr, range(97, 123)))

    result = a.index(letter.lower())
    return result

def rotate_character(char, rot):
    if type(char) == int:
        return char
    elif not char.isalpha():
        return char

    a = list(map(chr, range(97, 123)))

    index = alphabet_position(char)

    rot_char = int(index) + rot

    if char == char.upper() and rot_char < 26:
        return a[rot_char].upper()
    elif rot_char > 25:
        rot_char = rot_char % 26

        if char == char.upper():
            return a[rot_char].upper()

        return a[rot_char]

    return a[rot_char]
