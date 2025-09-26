import random, string, argparse


def generate_password(length: int, use_digits=True, use_uppercase=True, use_special_symbols=True):
    if length <= 0:
        print('Length of the password must be more than 0. Please try again.\n')
        return None

    this_password_chars = string.ascii_lowercase

    if use_digits:
        this_password_chars += string.digits
    if use_uppercase:
        this_password_chars += string.ascii_uppercase
    if use_special_symbols:
        this_password_chars += string.punctuation

    password = ''

    for _ in range(length):
        password += random.choice(this_password_chars)

    return password


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--length', type=int, required=True, help='Password length')
    parser.add_argument('--use_digits', action='store_true', help='Use digits')
    parser.add_argument('--use_uppercase', action='store_true', help='Use uppercase')
    parser.add_argument('--use_special_symbols', action='store_true', help='Use special symbols')

    arguments = parser.parse_args()

    password = generate_password(length=arguments.length,
                                 use_digits=arguments.use_digits,
                                 use_uppercase=arguments.use_uppercase,
                                 use_special_symbols=arguments.use_special_symbols
                                 )

    print(password)


if __name__ == '__main__':
    main()