def delete_punctuation(some_string):
    forbidden_symbols = ",.?!;:"

    string_without_punctuation = []

    for sym in some_string:
        if sym not in forbidden_symbols:
            string_without_punctuation.append(sym)

    new_string = ''.join(string_without_punctuation)

    return new_string


def vowels_count(some_string):
    vowels = "aeiou"

    vowels_counter = 0

    for sym in some_string:
        if sym.lower() in vowels:
            vowels_counter += 1

    return vowels_counter


def is_palindrome(some_string):
    opposite_symbol_index = -1

    for i in range(len(some_string) // 2):
        if some_string[i] == some_string[opposite_symbol_index]:
            opposite_symbol_index -= 1
        else:
            return 'не палиндром'

    return 'палиндром'


if __name__ == '__main__':
    print('Чтобы остановить тестировку, впишите END при вводе функции')

    while True:
        function_name = input('Введите название функции: ')

        if function_name.lower() == 'end':
            break

        parametr_value = input('Введите параметр функции: ')

        if function_name == 'delete_punctuation':
            result = delete_punctuation(parametr_value)

        elif function_name == 'vowels_count':
            result = vowels_count(parametr_value)

        elif function_name == 'is_palindrome':
            result = is_palindrome(parametr_value)

        else:
            print('Такой функции не существует')

        print(result)