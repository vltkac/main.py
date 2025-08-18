# import asyncio
#
# async def do_task(task_num, task_delay):
#     await asyncio.sleep(task_delay)
#     return f'Task {task_num} --- awaiting time {task_delay}'
#
#
# async def main():
#     tasks = await asyncio.gather(
#         do_task(1, 2),
#         do_task(2, 4),
#         do_task(3, 6),
#         do_task(4, 8)
#     )
#
#     for task in tasks:
#         print(task)
#
#
# asyncio.run(main())


import asyncio



async def download(url, delay):
    await asyncio.sleep(delay)
    return print(f'Data downloaded from {url} in {delay} seconds')


# async def main():
#     urls = [
#         "https://example.com",
#         "https://openai.com",
#         "https://github.com",
#         "https://stackoverflow.com",
#         "https://python.org",
#         "https://news.ycombinator.com",
#         "https://reddit.com",
#         "https://wikipedia.org",
#         "https://medium.com",
#         "https://techcrunch.com"
#     ]
#     await asyncio.gather(
#         download(urls[0], 2),
#         download(urls[1], 4),
#         download(urls[2], 6),
#         download(urls[3], 8),
#         download(urls[4], 10),
#         download(urls[5], 12),
#         download(urls[6], 14),
#         download(urls[7], 16),
#         download(urls[8], 18),
#         download(urls[9], 10),
#     )
#
#
# asyncio.run(main())

# students = ["Аня", "Борис", "Влад", "Даша"]
# grades = [5, 4, 5, 3]
#
# def show_student_and_grade(list_s, list_g):
#     list_zipped = zip(list_s, list_g)
#
#     return dict(list_zipped)
#
#
# print(show_student_and_grade(students, grades))


# students = ["Аня", "Борис", "Влад", "Даша", "Егор"]
# grades = [5, 4, 5, 3, 4]
#
#
# def get_dict(input_key, input_value):
#     marks = dict(zip(input_key, input_value))
#
#     marks.update([("Женя", 5)])
#
#     marks.pop("Даша")
#
#     print(f'Все ученики: {list(marks.keys())}')
#
#     print(f'Средняя оценка: {sum(marks.values()) / len(list(marks))}')
#
#
# get_dict(students, grades)


# friends = ["Аня", "Борис", "Влад"]
# favorite_drinks = ["Кофе", "Чай", "Сок"]
# cities = ["Москва", "Киев", "Минск"]
# colors = ["Синий", "Зелёный", "Красный"]
#
# info = dict()
#
# for i in range(len(friends)):
#     info[friends[i]] = {
#         'favorite drink': favorite_drinks[i],
#         'city': cities[i],
#         'color': colors[i]
#     }
#
# for i in range(len(friends)):
#     print(f'{friends[i]} любит {info[friends[i]].get('color')}')


# to-do

# import datetime
#
# tasks = {}
#
#
# def add_task(task_name, deadline):
#     if not isinstance(task_name, str) or not task_name:
#         return 'Впишите задачу'
#
#     if not isinstance(deadline, str) or not deadline:
#         return 'Впишите дедлайн в формате "ДД.ММ.ГГГГ"'
#
#     day = deadline[0:2]
#     month = deadline[3:5]
#     year = deadline[6:]
#
#     iso_format = year + '-' + month + '-' + day
#
#     try:
#         date_obj = datetime.date.fromisoformat(iso_format)
#     except ValueError:
#         return 'Неправильный формат даты'
#
#     date_output = str(date_obj)[-2:] + '.' + str(date_obj)[-5:-3] + '.' + str(date_obj)[0:4]
#
#     return tasks.update({task_name: date_output})
#
#
# add_task('поплакать', '05.09.2025')
# add_task('покакать', '28.02.2025')
#
#
# def show_tasks():
#     if not tasks:
#         print('Задач пока нет')
#
#     task_indexes = []
#
#     for i in range(1, len(tasks) + 1):
#         task_indexes.append(str(i) + '.')
#
#     counter_i = 0
#
#     for key, value in tasks.items():
#         print(task_indexes[counter_i], key, '-', value)
#         counter_i += 1
#
# show_tasks()
#
# print(list(tasks.items()))

# tasks = {
#     "сделать домашку": 3,
#     "вынести мусор": 7,
#     "прочитать книгу": 5
# }
#
# def sort_tasks_by_priority(diction):
#     diction = list(diction.items())
#
#     diction.sort(key= lambda x: x[1])
#
#     for i in range(len(diction)):
#         print(f'{i+1}. {diction[i][0]} - приоритет {diction[i][1]}')
#
#
# sort_tasks_by_priority(tasks)

# Напиши функцию count_occurrences(lst), которая принимает список слов и возвращает словарь, где ключ — слово,
# а значение — сколько раз оно встретилось.

# words = ["кот", "пёс", "кот", "мышь", "пёс", "кот"]
#
# def count_occurrences(lst):
#     dict_template = {}
#
#     checked_elements = []
#
#     for element in lst:
#         if element not in checked_elements:
#             checked_elements.append(element)
#
#         dict_template.update({element:lst.count(element)})
#
#     return dict_template
#
#
# print(count_occurrences(words))


# favorite_colors = {
#     "Аня": "Синий",
#     "Борис": "Зелёный",
#     "Влад": "Красный",
#     "Даша": "Синий",
#     "Егор": "Зелёный"
# }
#
# def reverse_dict(diction):
#     result = {}
#     names_list = []
#     for key, value in diction.items():
#         if (key, value):
#             names_list.append(key)
#
#             result.update({value: names_list})
#
#
#     return result
#
#
# print(reverse_dict(favorite_colors))

# def power2(lst):
#     result = []
#
#     for element in lst:
#         if element % 2 == 0:
#             result.append(element**2)
#
#     return result
#
#
# print(power2([1, 2, 3, 4, 5]))


# Напиши функцию, которая принимает список чисел и возвращает словарь,
# где ключ — это само число, а значение — True, если число простое, и False, если нет.

# def check_simple(number):
#     division_counter = 0
#
#     for divider in range(1, number + 1):
#         if number % divider == 0:
#             division_counter += 1
#
#     if division_counter == 2:
#         return True
#     else:
#         return False
#
# def main(lst):
#     result = {}
#
#     for num in lst:
#         result.update({num: check_simple(num)})
#
#     return result
#
#
# print(main([2, 3, 4, 5, 6]))

# def check_perfect_num(num):
#     dividers = []
#
#     for divider in range(1, num):
#         if num % divider == 0:
#             dividers.append(divider)
#
#     if sum(dividers) == num:
#         return True
#     else:
#         return False
#
#
# def main(lst):
#     result = {}
#
#     for element in lst:
#         result.update({element: check_perfect_num(element)})
#
#     return result
#
# print(main([6, 10, 28, 12, 496, 8128, 97, 33550336, 100, 500]))


# def show_counter(num):
#     counter = 1
#
#     if num < 1:
#         return print('Введите число больше 1')
#
#     while counter != num + 1:
#         print(counter)
#         counter += 1
#
#
# show_counter(-1)

# def counter_digits(num):
#     if not isinstance(num, int):
#         return 'Введите целое число'
#
#     digits = []
#
#     num = str(num)
#
#     for sym in num:
#         if sym.isdigit():
#             digits.append(int(sym))
#
#     return sum(digits)
#
#
# print(counter_digits(1232144))

# def get_smallest_div(num):
#     divider = 2
#
#     while num % divider != 0:
#         divider += 1
#
#     return divider
#
# print(get_smallest_div(139))

# def countdown(num):
#     while num >= 1:
#         print(num)
#
#         num -= 1
#
#
# countdown(10)

# def summa(num):
#     result = 0
#
#     counter = 1
#
#     while counter <= num:
#         result += counter
#         counter += 1
#
#     return result
#
#
# print(summa(12000))


# def reverse_num(num):
#     new_num = []
#
#     while num > 0:
#         left = num % 10
#
#         num = num // 10
#
#         new_num.append(str(left))
#
#     return int(''.join(new_num))
#
# print(reverse_num(123))

# def count_even(num):
#     counter = 0
#
#     while num > 0:
#         left = num % 10
#
#         if left % 2 == 0:
#             counter += 1
#
#         num = num // 10
#
#     return counter
#
#
# print(count_even(122134))

# Условие:
# Напиши функцию, которая принимает строку и возвращает True, если все символы в строке уникальны, и False в противном случае.

# пока каунт какого-то символа не станет равен 2

# def check_uniqueness(string):
#     i = 0
#
#     while i <= len(string) - 1:
#         if string.count(string[i]) == 1:
#             i += 1
#         else:
#             return False
#
#     return True
#
#
# print(check_uniqueness('пукни'))


# def get_fibonacci(num):
#     if not isinstance(num, int) or num <= 0:
#         'Введите целое число больше 0'
#
#     fibonacci = [
#         (0, 0),
#         (1, 1)
#     ]
#
#     for i in range(num - 1):
#         fibonacci.append(
#             (
#                 fibonacci[-1][0] + 1, fibonacci[-2][-1] + fibonacci[-1][-1]
#                                           )
#         )
#
#     return fibonacci[-1][1]
#
# print(get_fibonacci(10))


# grades = [10, 7, 5, 6, 10, 4, 9, 8, 6, 10, 3, 5, 7, 9]
#
# def analyze_list(lst):
#     print(f'Number of students: {len(lst)}')
#
#     print(f'Average grade: {round((sum(lst) / len(lst)), 1)}')
#
#     print(f'The most frequent grade: {max(lst, key=lambda grade: lst.count(grade))}')
#
#     sorted_grades = []
#
#     for grade in lst:
#         if grade not in sorted_grades:
#             sorted_grades.append(grade)
#
#     sorted_grades.sort()
#
#     print(f'All unique grades sorted: {sorted_grades}')
#
#
# analyze_list([10, 7, 5, 6, 10, 4, 9, 8, 6, 10, 3, 5, 7, 9])


# words = ["кот", "автомобиль", "пёс", "программист", "мышь"]
#
# def find_longest(lst):
#     return max(lst, key=lambda word: len(word))
#
#
# print(find_longest(words))


# sentences = [
#     "Кошка сидит на подоконнике.",
#     "Программисты любят Python.",
#     "Солнце светит ярко.",
#     "Это предложение содержит больше всего слов из всех здесь представленных."
# ]
#
# def analyze_str(lst):
#     longest_str = max(lst, key=lambda s: len(s))
#
#     print(f'Самое длинное предложение (по количеству символов): {longest_str}')
#
#     the_least_words = min(lst, key=lambda s: s.count(' '))
#
#     print(f'Самое короткое предложение (по количеству слов): {the_least_words}')
#
#     vowels = ['a', 'e', 'o', 'i', 'y', 'u', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
#
#     lst.sort(key=lambda s: sum(s.count(v.lower()) for v in vowels))
#
#     print(f'Отсортированные предложения по количеству гласных: {lst}')
#
# analyze_str(sentences)

# Дан список чисел. Отфильтруй из него только те, которые делятся на 3 и больше 10.
#
# Напиши функцию, которая возвращает такой отфильтрованный список.

# numbers = [4, 9, 12, 7, 15, 22, 33, 8, 27, 3, 18, 5]
#
# def filter_nums(lst):
#     return list(filter(lambda n: n % 3 == 0 and n > 10, lst))
#
#
# print(filter_nums(numbers))

# strings = ["Apple", "bAnana", "pear", "Apricot", "kiwi"]
#
# def filter_str(lst):
#     return list(filter(lambda word: len(word) > 5 and word.lower().count('a') > 0, lst))
#
#
# print(filter_str(strings))

# Функция принимает список строк, возвращает список с длинами строк.

# words = ["дом", "машина", "программирование", "кот", "слово"]
#
# def get_str_len(lst):
#     return list(map(lambda string: len(string), lst))
#
#
# print(get_str_len(words))

# nums = [1, 5, 10, 20]
#
# def add5(lst):
#     return list(map(lambda num: num + 5, lst))
#
#
# print(add5(nums))


# Есть список чисел. Напиши функцию, которая:
#
# Удалит из списка все числа, которые делятся на 3.
#
# Остальные числа возведёт в квадрат.
#
# Отсортирует получившийся список по возрастанию.
#
# Вернёт результат.


# def process_nums(lst):
#     filtered_nums = filter(lambda num: num % 3 != 0, lst)
#
#     squared_nums = list(map(lambda num: num ** 2, filtered_nums))
#
#     squared_nums.sort()
#
#     return squared_nums
#
#
# print(process_nums([1, 3, 4, 6, 7]))


# def process_list(lst):
#     only_palindromes = list(filter(lambda word: word.lower()[0] == word.lower()[-1], lst))
#
#     only_palindromes.sort(key=len)
#
#     new_str = list(map(lambda string: str(string) + ' ' + str(len(string)), only_palindromes))
#
#     return new_str
#
#
# print(process_list(["level", "test", "Anna", "world", "noon", "Python"]))

# vowels = 'aeyuoi'
#
# words = ["hello", "education", "sky", "rhythm", "automobile", "queue", "strength", "beautiful", "world", "opportunity"]
#
# def alter_str(lst):
#     vowels3 = list(filter(lambda word: sum(word.lower().count(v) for v in vowels) > 3, lst))
#
#     vowels3 = list(map(lambda word: word[0].upper() + word[1:], vowels3))
#
#     vowels3.sort(key=len)
#
#     vowels3.reverse()
#
#     return vowels3
#
#
# print(alter_str(words))



