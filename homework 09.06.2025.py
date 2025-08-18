# 1

# while True:
#     user_input = input('Введите слова через пробел и число в конце: ').strip()
#     print()
#
#     words_and_num = user_input.split(' ')
#
#     num = words_and_num[-1]
#
#     words_and_num.pop(-1)
#
#     words_and_num.sort()
#
#     if num.isdigit():
#         num = int(num)
#         sorteds = words_and_num[:num]
#         break
#     else:
#         print('Введите целое положительное число в конце')
#         print()
#         continue
#
# sorteds_str = ', '.join(sorteds)
#
# print(f'Первые {num} слов(-a) в алфавитном порядке: {sorteds_str}')

# 2

# user_input = input('Введите слова через пропуск: ')
#
# words = user_input.split()
#
# words[0] += '@gmail.com'
#
# for i in range(len(words) - 1):
#     i += 1
#     words[i] += '@gmail.com'
#
# print()
#
# print(words)

# 3

# option 1
# print('Варианты ответа: негативно, скорее негативно, нейтрально, скорее позитивно, позитивно')
# print()
# print('Чтобы остановить ввод, впишите END')
# print()
#
# options = ['негативно', 'скорее негативно', 'нейтрально', 'скорее позитивно', 'позитивно']
# votes = [0, 0, 0, 0, 0]
#
# while True:
#     user_vote = input('Введите вариант ответа: ')
#     if user_vote == 'негативно':
#         votes[0] += 1
#     elif user_vote == 'скорее негативно':
#         votes[1] += 1
#     elif user_vote == 'нейтрально':
#         votes[2] += 1
#     elif user_vote == 'скорее позитивно':
#         votes[3] += 1
#     elif user_vote == 'позитивно':
#         votes[4] += 1
#     elif user_vote == 'END':
#         print('Подсчет результатов')
#         print()
#         break
#     else:
#         print('Введён неправильный вариант ответа')
#         print()
#         continue
#
# print('Результаты:')
#
# for i in range(-1, len(options) - 1):
#     i += 1
#     print(f'{votes[i]} - {options[i]}')
#
# option 2
# print('Варианты ответа: негативно, скорее негативно, нейтрально, скорее позитивно, позитивно')
# print()
# print('Чтобы остановить ввод, впишите END')
# print()
#
# votes = []
# options_template = ['негативно', 'скорее негативно', 'нейтрально', 'скорее позитивно', 'позитивно']
#
#
# while True:
#     user_vote = input('Введите вариант ответа: ')
#
#     if user_vote in options_template:
#         votes.append(user_vote)
#     elif user_vote == 'END':
#         print('Подсчет результатов')
#         print()
#         break
#     else:
#         print('Введён неправильный вариант ответа')
#         print()
#         continue
#
# for i in range(-1, len(options_template) - 1):
#     i += 1
#     print(f'{votes.count(options_template[i])} - {options_template[i]}')