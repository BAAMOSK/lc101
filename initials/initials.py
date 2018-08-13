def get_initials():
    fullname = input('What is your full name?')
    name = fullname.split()
    result = ''

    for n in name:
        result += n[0].upper()

    print(result)
    return result

def main():
    get_initials()

if __name__ == '__main__':
    main()
