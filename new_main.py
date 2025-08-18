# Калькулятор возраста
# Условие:
#
# Напиши программу, которая:
#
# Принимает дату рождения пользователя в формате дд.мм.гггг (например: 26.06.2000).
#
# Выводит:
#
# текущий возраст в годах,
#
# сколько дней осталось до следующего дня рождения,
#
# в какой день недели родился пользователь (например: Monday).
from typing import final

from numpy.ma.core import append


# import datetime
#
# def show_age_info():
#     while True:
#         user_input = input('Введите свою дату рождения в формате дд.мм.гггг ').strip()
#
#         if len(user_input) == 10 and user_input[:2].isdigit() and user_input[2] == '.' and user_input[3:5].isdigit() and user_input[5] == '.' and user_input[6:].isdigit() and 1 < int(user_input[:2]) < 31 and 1 < int(user_input[3:5]) < 31 and 1900 < int(user_input[6:]):
#             user_day_ob = int(user_input[:2])
#
#             user_month_ob = int(user_input[3:5])
#
#             user_year_ob = int(user_input[6:])
#         else:
#             print('Использован неверный формат даты')
#             continue
#
#         date_obj = datetime.date(user_year_ob, user_month_ob, user_day_ob)
#
#         if date_obj > datetime.date.today():
#             print('Введите дату раньше сегодняшней')
#             continue
#
#         user_age = datetime.date.today().year - date_obj.year
#
#         if datetime.date.today().month < date_obj.month:
#             user_age -= 1
#         elif datetime.date.today().month == date_obj.month:
#             if datetime.date.today().day < date_obj.day:
#                 user_age -= 1
#
#
#         next_dob_date = datetime.date(datetime.date.today().year + 1, date_obj.month, date_obj.day)
#
#         if datetime.date.today().month < date_obj.month:
#             next_dob_date = datetime.date(datetime.date.today().year, date_obj.month, date_obj.day)
#         elif datetime.date.today().month == date_obj.month:
#             if datetime.date.today().day < date_obj.day:
#                 next_dob_date = datetime.date(datetime.date.today().year, date_obj.month, date_obj.day)
#
#         next_dob_in = next_dob_date - datetime.date.today()
#
#         next_dob_in = next_dob_in.days
#
#
#         weekday_of_dob = date_obj.weekday()
#
#         weekdays = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
#
#         weekday_of_dob = weekdays[weekday_of_dob]
#
#         return f'Вам {user_age} лет/года\nДо следующего дня рождения {next_dob_in} дней/дня\nВы родились в {weekday_of_dob}'
#
#
# print(show_age_info())


# try:
#     date_obj = datetime.datetime.strptime(user_input, "%d.%m.%Y").date()
# except ValueError:
#     print("Неверная дата — проверь число, месяц или год.")
#     continue


# Перемешанный список слов
# Условие:
#
# У тебя есть список из 10 разных слов (можешь задать свои, или программа пусть их создаёт).
#
# Программа перемешивает их случайным образом.
#
# Затем показывает пользователю перемешанный список, и просит ввести оригинальный порядок слов (через пробел).
#
# Если пользователь ввёл правильно — поздравляем.
#
# Если ошибся — показываем, сколько слов он угадал на правильных местах, и в каких позициях были ошибки.

# def game():
#     import random
#     # import time
#     # import os
#
#     words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'orange']
#
#     initial_words_str = ', '.join(words)
#
#     new_words = []
#
#     while len(words) > 0:
#         randomized = random.choice(words)
#
#         new_words.append(randomized)
#
#         words.remove(randomized)
#
#     words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'orange']
#
#     new_words_str = ', '.join(new_words)
#
#     print(new_words_str)
#
#     while True:
#         user_answer = input('Попробуйте угадать начальный список (введите слова через пробел): ')
#         print()
#
#         user_answer_list = user_answer.split()
#
#         for word in user_answer_list:
#             if word not in words:
#                 print('Введите все слова из перемешанного списка\n')
#                 return game()
#
#         correct_index = []
#
#         wrong_index = []
#
#         for word in user_answer_list:
#             if user_answer_list.index(word) == words.index(word):
#                 correct_index.append(word)
#             else:
#                 wrong_index.append(word)
#
#         correct_index_str = ', '.join(correct_index)
#
#         wrong_index_str = ', '.join(wrong_index)
#
#         return print(f'Вы угадали позиции {correct_index_str}, но не угадали {wrong_index_str}\nНачальный список: {initial_words_str}')
#
#
# game()


# Задача 1: Удаление дубликатов из списка слов
# У тебя есть список строк. Нужно вернуть новый список, где слова не повторяются, и сохранить порядок появления.


# def delete_duplicates(words):
#     if not words:
#         return 'Введите список слов'
#     else:
#         no_duplicates_words = []
#
#         for word in words:
#             if word not in no_duplicates_words:
#                 no_duplicates_words.append(word)
#
#     return no_duplicates_words
#
# print(delete_duplicates(['apple', 'banana', 'apple', 'cherry', 'banana']))

# Калькулятор среднего балла студента

# def calculate_avg():
#     students_grades = input('Введите оценки через запятую: ')
#
#     students_grades_correct = students_grades.replace(',', '')
#
#     grades = students_grades_correct.split()
#
#     grades_correct = []
#
#     for element in grades:
#         try:
#             grades_correct.append(float(element))
#         except ValueError:
#             print("Ошибка: введите только числа\n")
#             return calculate_avg()
#
#     avg_value = sum(grades_correct) / len(grades_correct)
#
#     avg_value = round(avg_value, 2)
#
#     return print(f'Среднее значение: {avg_value}')
#
#
# calculate_avg()


# "Длина слов"
# Попроси пользователя ввести слова через пробел. Затем:
#
# Преобразуй каждое слово в число — посчитай его длину.
#
# Если пользователь по ошибке ввёл числа (например: 123), отлови это с помощью try/except и скажи, что нужно ввести именно слова, а не цифры.
#
# Покажи пользователю:
#
# Список длин слов;
#
# Самое длинное слово;
#
# Среднюю длину слов (округлённую до 2 знаков).


# def get_words_len():
#     user_input = input('Введите слова через пробел: ')
#
#     unverified_elements = user_input.split()
#
#     verified_elements = []
#
#     for element in unverified_elements:
#         if not element.isalpha():
#             print('Введите только слова')
#             return get_words_len()
#         else:
#             verified_elements.append(element)
#
#     words_length = []
#
#     for word in verified_elements:
#         words_length.append(len(word))
#
#     longest_word = verified_elements[words_length.index(max(words_length))]
#
#     avg_length = sum(words_length) / len(words_length)
#
#     return print(f'Длины слов: {words_length}\nСамое длинное слово: {longest_word}\nСредняя длина: {avg_length:.2f}')
#
#
# get_words_len()


# Задача: Случайный пароль и проверка длины
# Сгенерируй случайный пароль из букв и цифр длиной от 6 до 12 символов.
#
# Попроси пользователя ввести число — желаемую длину пароля.
#
# Используй try/except, чтобы обработать ошибки, если пользователь ввёл не число или число вне диапазона 6–12.
#
# Если ввод правильный — создай пароль именно такой длины и выведи его.
#
# Если ошибка — выведи сообщение и попроси повторить ввод.


# def generate_password():
#     import random
#
#     user_input = input('Введите число от 6 до 12, чтобы сгенерировать пароль: ')
#
#     try:
#         password_length = int(user_input)
#         if not 6 <= password_length <= 12:
#             raise ValueError
#     except ValueError:
#         print('Введите число от 6 до 12')
#         return generate_password()
#
#     pass_sym = []
#
#     letters_and_dig = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
#
#     for _ in range(password_length):
#         pass_sym.append(random.choice(letters_and_dig))
#
#     password = ''.join(pass_sym)
#
#     return password
#
# print(generate_password())


# Задача: Анализ списка слов (без словарей)
# Пользователь вводит несколько слов через пробел.
#
# Проверяем, что все — слова (только буквы).
#
# Выводим:
# • Количество уникальных слов (используй список и проверку, чтобы не считать повторы).
# • Самое часто встречающееся слово (найди, какое слово встречается чаще всего).
# • Среднюю длину слов (округлить до 2 знаков).


# def analyze_words():
#     user_input = input('Введите слова через пробел: ')
#
#     unverified_elements = user_input.split()
#
#     verified_elements = []
#
#     for element in unverified_elements:
#         if not element.isalpha():
#             print('Введите только слова')
#             return analyze_words()
#         else:
#             verified_elements.append(element)
#
#     no_duplicates = []
#
#     for element in verified_elements:
#         if element not in no_duplicates:
#             no_duplicates.append(element)
#
#     all_symbols_no_duplicates = ''.join(no_duplicates)
#
#     avg_length = len(all_symbols_no_duplicates)/len(no_duplicates)
#
#     elements_counts = []
#
#     for element in verified_elements:
#         elements_counts.append(verified_elements.count(element))
#
#     most_frequent = verified_elements[elements_counts.index(max(elements_counts))]
#
#     return (f'Количество уникальных слов: {len(no_duplicates)}\nСамое частое слово: {most_frequent}\nСредняя длина слова (из уникальных слов): {round(avg_length, 2)}')
#
#
# print(analyze_words())

# Задача: Анализ текста и статистика по словам
# Что нужно сделать:
#
# Пользователь вводит строку с текстом (может быть несколько предложений).
#
# Нужно разбить текст на слова (через пробелы и знаки препинания).
#
# Проверить, что слова состоят только из букв (иначе игнорировать такие "слова").
#
# Подсчитать:
#
# сколько всего уникальных слов,
#
# вывести самое длинное слово,
#
# посчитать среднюю длину уникальных слов (округлить до 2 знаков),
#
# вывести три самых часто встречающихся слова (если есть несколько с одинаковой частотой — любые три).

# def analyze_text():
#     input_user = input('Введите текст: ')
#
#     user_text_symbols = []
#
#     for symbol in input_user:
#         if symbol.isalpha() or symbol == ' ':
#             user_text_symbols.append(symbol)
#
#     str_no_punctuation = ''.join(user_text_symbols)
#
#     final_words = str_no_punctuation.split()
#
#     unique_words = []
#
#     len_of_words = []
#
#     for word in final_words:
#         if word not in unique_words:
#             unique_words.append(word)
#
#         len_of_words.append(len(word))
#
#     unique_words_num = len(unique_words)
#
#     longest_word = final_words[len_of_words.index(max(len_of_words))]
#
#     unique_words_all_sym = ''.join(unique_words)
#
#     unique_words_avg_length = round((len(unique_words_all_sym) / len(unique_words)), 2)
#
#     all_words_amount = []
#
#     checked_most_frequent_word = []
#
#     for word in final_words:
#         all_words_amount.append(final_words.count(word))
#
#     while len(checked_most_frequent_word) < 3:
#         for word in final_words:
#             if word not in checked_most_frequent_word:
#                 # checked_most_frequent_word.append(final_words[all_words_amount.index(max(all_words_amount))])
#                 checked_most_frequent_word.append(word)
#
#     print(checked_most_frequent_word)
#
#     print(len(checked_most_frequent_word))
#
#     return f'Сколько всего уникальных слов: {unique_words_num}\nСамое длинное слово: {longest_word}\nСредняя длина уникальных слов: {unique_words_avg_length}'
#
#
# print(analyze_text())
#

# Задача: Проверка пароля на безопасность
# Условие:
# Попроси пользователя ввести пароль. Затем проверь, насколько он безопасен.
# Пароль считается безопасным, если:
#
# длина от 8 символов
#
# содержит хотя бы одну заглавную букву
#
# содержит хотя бы одну строчную букву
#
# содержит хотя бы одну цифру
#
# содержит хотя бы один специальный символ (например: !@#$%^&*()-_=+[]{};:,.<>?)
#
# ✅ Твоя задача:
# Получить строку от пользователя.
#
# Проверить все условия выше.
#
# Если не проходит — сказать, что именно не так.
#
# Если всё ок — написать, что пароль надёжный.


# def check_pass():
#     while True:
#         user_password_try = input('Введите пароль: ')
#
#         upper_count = 0
#
#         lower_count = 0
#
#         digit_count = 0
#
#         special_symbol_count = 0
#
#         specials = '!@#$%^&*()-_=+[]{};:,.<>?'
#
#         user_password_try_symbols = []
#
#         for sym in user_password_try:
#             user_password_try_symbols.append(sym)
#
#         if len(user_password_try_symbols) < 8:
#             print('Пароль должен быть длинее 8 символов')
#             continue
#
#         for sym in user_password_try_symbols:
#             if sym.isupper():
#                 upper_count += 1
#             elif sym.islower():
#                 lower_count += 1
#             elif sym.isdigit():
#                 digit_count += 1
#             elif sym in specials:
#                 special_symbol_count += 1
#
#         if upper_count >= 1 and lower_count >= 1 and digit_count >= 1 and special_symbol_count >= 1:
#             print('Пароль безопасный')
#             return
#         else:
#             print('Пароль не безопасный')
#             continue
#
#
# check_pass()

#  Проверка email-адреса
# Напиши программу, которая:
#
# Просит пользователя ввести email-адрес.
#
# Проверяет:
#
# Есть ли в строке символ "@".
#
# Есть ли "." после "@" (например, user@example.com — ок).
#
# Не начинается ли email с символа "@" или ".".
#
# Нет ли пробелов в email.
#
# Если email валидный — вывести: Email принят: <email>
#
# Иначе — вывести, что неверный email, и снова запросить ввод

# def check_email():
#     while True:
#         user_input = input('Please enter e-mail: ')
#
#         if '@' in user_input and not user_input.startswith('.') and not user_input.startswith('@') and '.' in user_input[user_input.index('@'):] and not ' ' in user_input:
#             print(f'E-mail valid: {user_input}')
#             return
#         else:
#             print('E-mail not valid')
#             continue
#
# check_email()

# Удалить подряд идущие дубликаты
# Условие:
# Пользователь вводит строку слов через пробел.
# Нужно удалить подряд идущие одинаковые слова, оставив только одно из них.
# Порядок слов сохранить.

# def delete_duplicates_sequence():
#     user_input = input('Введите слова через пробел: ')
#
#     initial_words = user_input.split()
#
#     no_duplicates_sequences = [initial_words[0]]
#
#     for i in range(1, len(initial_words)):
#         if initial_words[i] != initial_words[i - 1]:
#             no_duplicates_sequences.append(initial_words[i])
#
#     str_output = ' '.join(no_duplicates_sequences)
#
#     return str_output
#
# print(delete_duplicates_sequence())

# Задача для тренировки (попроще):
# У тебя есть список чисел. Найди все пары чисел, сумма которых чётная.

# nums = [1, 2, 3, 4]
#
# even_couples = []
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if (nums[i] + nums[j]) % 2 == 0:
#             even_couples.append([nums[i], nums[j]])
#
# print(even_couples)

# Найти пары чисел с разностью, кратной 3
# У тебя есть список чисел. Нужно найти все пары, разность которых делится на 3 без остатка, и записать их в виде пар [a, b].

# nums = [5, 7, 10, 13, 16]
#
# divided_by_3 = []
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if (nums[i] - nums[j]) % 3 == 0 or (nums[j] - nums[i]) % 3 == 0:
#             divided_by_3.append([nums[i], nums[j]])
#
# print(divided_by_3)

# Подсчитать количество слов, которые начинаются и заканчиваются на одну и ту же букву
# Описание:
# Дан список слов. Нужно вернуть количество слов, у которых первая и последняя буква совпадают.

# def get_f_a_l_letter_same(words):
#     words_count = 0
#
#     for word in words:
#         if word[0] == word[-1]:
#             words_count += 1
#
#     return words_count
#
#
# print(get_f_a_l_letter_same(['apple', 'anna', 'kayak', 'level', 'test', 'deed', 'open', 'pop', 'stop']))

# Обратная строка
# Описание:
# Напиши функцию, которая принимает строку и возвращает её в обратном порядке.

# def reverse_str(string):
#     str_symbols = []
#
#     for symbol in string:
#         str_symbols.append(symbol)
#
#     str_symbols.reverse()
#
#     new_str = ''.join(str_symbols)
#
#     return new_str
#
#
# print(reverse_str('Напиши функцию, которая принимает строку и возвращает количество гласных букв в ней (a, e, i, o, u — только латиница, в любом регистре).'))

# def reverse_str(string):
#     return string[::-1]

# Подсчёт гласных и согласных
# Описание:
# Напиши функцию, которая принимает строку и возвращает два числа:
# количество гласных и количество согласных в этой строке. Игнорируй пробелы, цифры и знаки препинания. Регистр не имеет значения.

def get_consonant_vowels(string):
    if not isinstance(string, str):
        return 'Передайте строку как параметр'


    vowels = 'aeiouаеёиоуыэюя'

    consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'

    vowels_count = 0

    consonants_count = 0

    for element in string:
        if element.lower() in vowels:
            vowels_count += 1
        elif element.lower() in consonants:
            consonants_count += 1

    return f'Vowels: {vowels_count}\nConsonants: {consonants_count}'


print(get_consonant_vowels(1))































