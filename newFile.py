# Дано целое число num. Повторно складывай его цифры, пока результат не станет однозначным числом
# Input: 38
# → 3 + 8 = 11
# → 1 + 1 = 2
# Output: 2
# from operator import index
# from string import punctuation
import string
from dbm.sqlite3 import GET_SIZE
from re import match

from fontTools.merge.util import first, onlyExisting
from networkx.generators.classic import balanced_tree
from urllib3.filepost import writer

# from fontTools.misc.cython import returns


# import random
#
# num = random.randint(10, 99)
# print(num)
#
# while True:
#     num = str(num)
#
#     digit1 = int(num[0])
#     digit2 = int(num[1])
#
#     sum_to_check = digit1 + digit2
#
#     if sum_to_check not in range(1, 10):
#         num = sum_to_check
#         print(num)
#     else:
#         print(sum_to_check)
#         break

# Задача:
# Создай n-е число в последовательности "Count and Say".
#
# Начинаем с "1"
#
# Следующее — "one 1" → "11"
#
# Потом "two 1s" → "21"
#
# Потом "one 2, one 1" → "1211"
# И так далее.
#
# Пример:
#

# Input: n = 4
# Output: "1211"

# пока элемент равняется следующему, каунтим его

# words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# num = '1'
#
# num = num.split()
#
# for digit in num:
#     counter = 0
#     while num[0] == num[1]:
#         counter += 1
#     num.append(counter)
#     num.append(int(num))
#
# print(num)

# Задача 1
# Дана строка, состоящая из слов, разделённых пробелами.
# Нужно вернуть строку, где слова идут в обратном порядке.

# string = 'hello world this is fine'
#
# def reverse_string(some_str):
#     words = some_str.split()
#
#     words.reverse()
#
#     string_reversed = ' '.join(words)
#
#     return string_reversed
#
#
# print(reverse_string(string))

# Задача 2
# Дан список чисел. Верни новый список, где нет повторяющихся элементов, сохрани порядок первого появления.

# numbers = [4, 7, 2, 4, 9, 7, 2, 1, 5, 9, 3]
#
# def no_duplicates(some_list):
#     numbers_no_duplicates = []
#
#     for num in some_list:
#         if num not in numbers_no_duplicates:
#             numbers_no_duplicates.append(num)
#
#     return numbers_no_duplicates
#
#
# print(no_duplicates(numbers))

# Задача 3
# Проверь, является ли строка палиндромом (читается одинаково слева направо и справа налево).

# palindromes = [
#     "level",       # палиндром
#     "radar",       # палиндром
#     "hello",       # не палиндром
#     "world",       # не палиндром
#     "madam",       # палиндром
#     "python"       # не палиндром
#     "noon"         # палиндром
# ]
#
# word = 'python'
#
# def is_palindrome(some_word):
#     opposite_symbol_index = -1
#
#     for i in range(len(some_word) // 2):
#         if some_word[i] == some_word[opposite_symbol_index]:
#             opposite_symbol_index -= 1
#         else:
#             return 'не палиндром'
#
#     return 'палиндром'
#
#
# print(is_palindrome(word))


# Найти "средний" элемент списка
# Дан список с нечётным числом элементов. Нужно вернуть элемент, который будет посередине после сортировки списка.

# nums = [7, 2, 9, 4, 3, 99, -100, 120, 600, 222, 500, 1000, 13]
#
# def sort_list_and_get_med(numbers):
#     numbers.sort()
#
#     med_index = len(numbers) // 2
#
#     return numbers[med_index]
#
# print(sort_list_and_get_med(nums))


#  Подсчёт уникальных символов в строке
# Напиши функцию, которая принимает строку и возвращает количество уникальных символов в ней.

# string = 'abracadabra'
#
# def count_unique_symbols(some_string):
#     unique_sum = 0
#
#     unique_sym = []
#
#     for symbol in some_string:
#         if symbol not in unique_sym:
#             unique_sym.append(symbol)
#             unique_sum += 1
#
#     return unique_sum
#
#
# print(count_unique_symbols(string))

# Проверка, является ли одна строка перестановкой другой
# Напиши функцию, которая принимает две строки и возвращает True, если одна строка — это перестановка символов другой (то есть они содержат одинаковые символы в любом порядке), и False в противном случае.


# def compare_strings(str1, str2):
#     if len(str1) == len(str2):
#         str1_sym = []
#
#         str2_sym = []
#
#         str1_sym_num = []
#
#         str2_sym_num = []
#
#         for sym in str1:
#             str1_sym.append(sym)
#
#         for sym in str2:
#             str2_sym.append(sym)
#
#         for sym in str1_sym:
#             sym_num = (str1_sym.count(sym), sym)
#
#             if sym_num not in str1_sym_num:
#                 str1_sym_num.append(sym_num)
#
#         for sym in str2_sym:
#             sym_num = (str2_sym.count(sym), sym)
#
#             if sym_num not in str2_sym_num:
#                 str2_sym_num.append(sym_num)
#
#         str1_sym_num.sort()
#
#         str2_sym_num.sort()
#
#         if str1_sym_num == str2_sym_num:
#             return 'строки одинаковые'
#         else:
#             return 'строки разные'
#
#     else:
#         return 'строки имеют разную длину'
#
#
# print(compare_strings("listen", "silent"))  # строки одинаковые
# print(compare_strings("hello", "world"))    # строки разные
# print(compare_strings("test", "ttes"))      # строки одинаковые
# print(compare_strings("test", "ttez"))      # строки разные
# print(compare_strings("abc", "abcd"))       # строки имеют разную длину

# Удалить повторяющиеся символы, сохранив порядок

# def remove_duplicates(string):
#     str_letters = []
#
#     for sym in string:
#         str_letters.append(sym)
#
#     checked_sym = []
#
#     for sym in str_letters:
#         if sym not in checked_sym:
#             checked_sym.append(sym)
#
#     return ''.join(checked_sym)
#
#
# print(remove_duplicates("hello"))        # helo
# print(remove_duplicates("abracadabra"))  # abrcd
# print(remove_duplicates("aabbcc"))       # abc

# Самый частый символ

# def most_frequent_char(string):
#     symbol_counts = []
#
#     for symbol in string:
#         symbol_count = string.count(symbol)
#         symbol_counts.append([symbol_count, symbol])
#
#     max_num = max(symbol_counts)
#
#     return max_num[1]
#
#
# print(most_frequent_char('abracadabra'))
# print(most_frequent_char("hello"))
# print(most_frequent_char("aabbbcccc"))


# Дан список целых чисел. Найди сумму всех чисел, которые больше среднего арифметического этого списка.

# def get_sum(nums):
#     average = sum(nums) / len(nums)
#
#     more_than_avg = []
#
#     for num in nums:
#         if num > average:
#             more_than_avg.append(num)
#
#     return sum(more_than_avg)
#
# print(get_sum([1, 3, 5, 7, 9]))
# print(get_sum([10, 20, 30, 40, 50, 60]))


# Дан список целых чисел. Нужно вернуть новый список, где каждый элемент равен сумме самого себя и всех предыдущих элементов исходного списка.

# def get_new_list(nums):
#     summa = 0
#
#     new_list = []
#
#     for num in nums:
#         summa += int(num)
#
#         new_list.append(summa)
#
#     return new_list
#
#
# print(get_new_list([-2, 4, 6, -1, 0, 3, 8, -5, 2, 1, 7]))


# Дана строка из букв и цифр. Нужно вывести количество букв и количество цифр в отдельные переменные и напечатать их.

# def count_types(string):
#     letters_count = 0
#
#     digits_count = 0
#
#     for sym in string:
#         if sym.isalpha():
#             letters_count += 1
#         elif sym.isdigit():
#             digits_count += 1
#
#     return f'Letters: {letters_count}\nDigits: {digits_count}'
#
#
# print(count_types('abc1234d5'))


# Дан список чисел. Нужно найти максимальную разницу между двумя элементами списка, при этом больший элемент должен идти в списке после меньшего.


# list1 = [7, 1, 5, 3, 6, 4]
#
# def get_max_dif(nums):
#     if nums.index(max(nums)) > nums.index(min(nums)):
#         max_dif = abs(max(nums) - min(nums))
#
#     return max_dif
#
# print(get_max_dif(list1))


# Напиши функцию, которая получает строку и возвращает словарь символов, отсортированных по частоте в порядке убывания.


# def count_letters(data):
#     res = []
#
#     checked_symbols = []
#
#     for symbol in data:
#         if symbol not in checked_symbols:
#             res.append((symbol, data.count(symbol)))
#             checked_symbols.append(symbol)
#
#     res.sort(key=lambda pair:pair[-1], reverse=True)
#
#     result = {}
#
#     for pair in res:
#         result[pair[0]] = pair[1]
#
#     return result
#
#
# print(count_letters('banana'))


# Найди все числа, которые встречаются только один раз во всей структуре. Верни их отсортированными по возрастанию.

# import random
#
# # Установка сидов для повторяемости
# random.seed(42)
#
# data = [
#     [random.randint(1, 1000) for _ in range(10)]
#     for _ in range(1000)
# ]

# def get_unique(lst):
#     all_nums = []
#
#     for el in lst:
#         for num in el:
#             all_nums.append(num)
#
#     res = []
#
#     for num in all_nums:
#         if all_nums.count(num) == 1:
#             res.append(num)
#
#     res.sort()
#
#     return res
#
#
# print(get_unique(data))

# data1 = [
#     {"name": "Anna", "age": 22},
#     {"name": "Tom", "age": 19},
#     {"name": "Bob", "age": 25}
# ]
#
# def sort_by_age(data):
#     data.sort(key=lambda user: user['age'], reverse=True)
#
#     return data
#
#
# print(sort_by_age(users))


# Дан список имён:

# ["Alice", "Albert", "Bob", "Bella", "Charlie"]

# Верни словарь, где ключ — первая буква, значение — список имён на эту букву.


# def group_names_by_first_letter(data):
#     res = {}
#
#     for el in data:
#         res[el[0]] = list(filter(lambda name: name[0] == el[0], data))
#
#     return res
#
#
# print(group_names_by_first_letter(["Alice", "Albert", "Bob", "Bella", "Charlie"]))

# Напиши генератор, который принимает список чисел, отсортированных по возрастанию,
# и сгруппирует подряд идущие числа в диапазоны.
#
# Пример:
#
# [1, 2, 3, 6, 7, 10] → генератор выдаёт:
# "1-3", "6-7", "10"

# def create_str(r):
#     if len(r) > 1:
#         print(f'{r[0]} - {r[-1]}')
#     else:
#         print(f'{r[0]}')
#
#
# def generate_ranges(data):
#     ranges = [[data[0]]]
#
#     for i in range(1, len(data)):
#         if data[i] - data[i - 1] == 1:
#             ranges[-1].append(data[i])
#         else:
#             ranges.append([data[i]])
#
#     for r in ranges:
#         create_str(r)
#
#
# generate_ranges([1, 2, 3, 6, 7, 10])


# ["hello", "world", "python", "rocks"]
# → {"hello": 5, "world": 5, "python": 6, "rocks": 5}


# def get_word_len(data):
#     res = {}
#
#     for word in data:
#         res[word] = len(word)
#
#     return res
#
#
# print(get_word_len(["hello", "world", "python", "rocks"]))

# 3. Сгруппировать по типу
# Дан список из разных типов:

# ["hello", 123, 4.5, "world", 99]
# → {"str": ["hello", "world"], "int": [123, 99], "float": [4.5]}

# def sort_types(data):
#     res = {
#         'str': list(filter(lambda element: type(element) == str, data)),
#         'int': list(filter(lambda element: type(element) == int, data))
#            }
#
#     return res
#
#
# print(sort_types(["hello", 123, 4.5, "world", 99]))


# Напиши функцию compress, которая принимает список целых чисел и возвращает список кортежей вида (число, количество повторов подряд).

# nums = [5, 5, 2, 2, 2, 8, 9, 9, 9, 9, 1, 3, 3, 123, 666, 666]


# def compress(data):
#     res = []
#
#     i = 0
#
#     counter = 1
#
#     while True:
#         if i == len(data) - 1:
#             res.append((data[i], counter))
#             break
#
#         if data[i] == data[i + 1]:
#             counter += 1
#             i += 1
#         else:
#             res.append((data[i], counter))
#             counter = 1
#             i += 1
#
#     return res
#
#
# print(compress(nums))

# text = "Hello, hello! How are you? Are you okay? Hello!"
# # ➜ {'hello': 3, 'how': 1, 'are': 2, 'you': 2, 'okay': 1}
# def word_frequency(data):
#     import string
#
#     res = {}
#
#     to_remove = string.punctuation
#
#     no_punctuation_str = (''. join(list(filter(lambda sym: sym not in to_remove, data)))).lower()
#
#     words = no_punctuation_str.split()
#
#     for word in words:
#         res[word] = words.count(word)
#
#     return res
#
#
# print(word_frequency(text))


# def get_longest_unique_sub(data):
#     all_unique_subs = [[data[0]]]
#
#     index_of_sym = 0
#
#     index_of_sub = 0
#
#     while True:
#        if index_of_sym == len(data) - 1:
#            break
#
#        if data[index_of_sym + 1] in all_unique_subs[-1]:
#            all_unique_subs.append([data[index_of_sym + 1]])
#            index_of_sym += 1
#            index_of_sub += 1
#        else:
#            all_unique_subs[-1].append(data[index_of_sym + 1])
#            index_of_sym += 1
#
#
#     return max(map(lambda sub: len(sub), all_unique_subs))
#
#
# print(get_longest_unique_sub('abrkaabcdefghijjxxx'))


# def can_make_word(source, target):
#     source_letters = {}
#     target_letters = {}
#
#     source = source.lower()
#
#     target = target.lower()
#
#     for letter in source:
#         source_letters[letter] = 0
#
#     for letter in target:
#         target_letters[letter] = 0
#
#     for key in target_letters:
#         if key not in source_letters:
#             return False
#
#     for letter in source:
#         source_letters[letter] += 1
#
#     for letter in target:
#         target_letters[letter] += 1
#
#     for letter in target_letters:
#         if source_letters.get(letter) < target_letters.get(letter):
#             return False
#
#     return True
#
#
# print(can_make_word('hellO', 'hello'))


# def first_unique_char(data):
#     result = []
#
#     for char in data:
#         if data.count(char) == 1:
#             result.append(char)
#
#         if len(result) == 1:
#             return char
#
#     if not result:
#         return None
#
#
# print(first_unique_char('loveleetcode'))


# Напиши функцию reverse_integer(n), которая получает целое число n и возвращает его цифры в обратном порядке.
# Если результат выходит за пределы 32-битного знака (от −2³¹ до 2³¹−1), верни 0.


# def reverse_integer(n):
#     digits = []
#
#     x = n
#
#     while abs(x) > 0:
#         dig = abs(x) % 10
#         digits.append(dig)
#         x = abs(x) // 10
#
#     while digits[0] == 0:
#         digits.pop(0)
#
#     result = 0
#
#     zeroes = len(digits)
#
#     for digit in digits:
#         result += digit * 10 ** zeroes / 10
#         zeroes -= 1
#
#     if n < 0:
#         result = -1 * result
#
#     if -2 ** 31 > result or result > 2 ** 31 - 1:
#         return 0
#
#     return int(result)
#
#
# print(reverse_integer(123))


# intervals = [[1, 10], [2, 6], [3, 5], [7, 9]]
#
#
# def merge_intervals(data):
#     sorted_data = sorted(data, key=lambda interval: interval[0])
#
#     res = [[sorted_data[0]]]
#
#     index_interval = 0
#
#     index_sorted = 0
#
#     while True:
#         if index_sorted == len(sorted_data) - 1:
#             break
#
#         if sorted_data[index_sorted][1] >= sorted_data[index_sorted + 1][0]:
#             res[index_interval].append(sorted_data[index_sorted + 1])
#             index_sorted += 1
#         else:
#             res.append([sorted_data[index_sorted + 1]])
#             index_interval += 1
#             index_sorted += 1
#
#     merged = []
#
#     for element in res:
#         merged.append([element[0][0], element[-1][1]])
#
#     return merged
#
#
# print(merge_intervals(intervals))

# если сумма n-го элемента и одного из всех последующих элементов не равна цели, переходим к n+1 элементу

# def two_sum(data, target):
#     copied = data.copy()
#
#     while len(copied) >= 2:
#         compared_element = 0
#
#         compared_element += copied.pop(0)
#
#         for num in copied:
#             if compared_element + num == target:
#                 return [data.index(compared_element), data.index(num)]
#
#
# print(two_sum([11, 45, 98, 100, 34, 102, 54, 541, 1, 999], 198)) # [2, 3]


# def count_capitalized_words(text):
#     words = text.split()
#
#     caps_words = list(filter(lambda w: w[0].isupper(), words))
#
#     return len(caps_words)
#
# print(count_capitalized_words("Today is a Good Day to Learn Python"))

# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#
#     return len(list(
#         filter(lambda letter: letter in vowels, string)
#                ))
#
# print(count_vowels("Hello World!"))


# def all_unique_substrings(data):
#     result = []
#
#     counter_uniqueness = 1
#
#     while True:
#         for char in data:
#             result.append(data[:counter_uniqueness])
#
#         break
#     print(result)
#     print(counter_uniqueness)
#
#
# all_unique_substrings('bba')

# elements = ["Apple", "Banana", "Apricot", "blueberry", "cherry", "avocado"]
#
#
# def group_by_first_letter(words):
#     new_list = []
#
#     result = {}
#
#     for word in words:
#         new_list.append(word[0].lower() + word[1:])
#
#     for word in new_list:
#         result[word[0]] = []
#
#     for word in new_list:
#         result[word[0]].append(word)
#
#     return result
#
#
# print(group_by_first_letter(elements))


# def count_letters(data):
#     result = {}
#
#     data = data.lower()
#
#     letters = []
#
#     for letter in data:
#         if letter.isalpha() and not letter in letters:
#             letters.append(letter)
#
#     for letter in letters:
#         result[letter] = data.count(letter)
#
#     return result
#
#
# print(count_letters("Hello World!"))


# def count_words(data):
#     import string
#
#     result = {}
#
#     for symbol in data:
#         if symbol in string.punctuation:
#             data = data.replace(symbol, '')
#
#     words = data.lower().split()
#
#     for word in words:
#         if word not in result:
#             result[word] = 1
#         else:
#             result[word] += 1
#
#     return result
#
# print(count_words("Python is great? And PYTHON is fun!"))


# def is_isogram(data):
#     letters = []
#
#     for letter in data.lower():
#         if letter in letters:
#             return False
#
#         letters.append(letter)
#
#     return True
#
#
# is_isogram("Machine")       # ➜ True
# is_isogram("isogram")       # ➜ True
# is_isogram("Alphabet")      # ➜ False  # "a" повторяется
# is_isogram("hello")         # ➜ False
# is_isogram("Dermatoglyphics") # ➜ True


# def is_palindrome(data: str):
#     import string
#
#     lowered = data.lower()
#
#     for symbol in string.punctuation:
#         lowered = lowered.replace(symbol, '')
#
#     lowered = lowered.replace(' ', '')
#
#     for i in range(len(lowered)):
#         if lowered[i] != lowered[-(i + 1)]:
#             return False
#
#     return True
#
#
# print(is_palindrome("A man, a plan, a canal: Panama"))


# def most_frequent(data):
#     nums_count = {}
#
#     for num in data:
#         if num not in nums_count:
#             nums_count[num] = 1
#         else:
#             nums_count[num] += 1
#
#     nums_count = list(nums_count.items())
#
#     nums_count.sort(key=lambda pair: pair[1], reverse=True)
#
#     nums_count.sort(key=lambda pair: pair[0])
#
#     return nums_count[0][0]
#
#
# print(most_frequent([5, 4, 4, 3, 3, 5]))


# def sum_two_smallest_positives(numbers: list):
#     filtered_nums = list(filter(lambda num: num > 0, numbers))
#
#     if len(filtered_nums) < 2:
#         return None
#
#     sorted_nums = sorted(filtered_nums)
#
#     return sorted_nums[0] + sorted_nums[1]
#
# print(sum_two_smallest_positives([19, 5, 42, 2, 77]))
# print(sum_two_smallest_positives([10, -5, 0, 8, 3]))
# print(sum_two_smallest_positives([1]))
# print(sum_two_smallest_positives([-1, -2, -3, 0]))
# print(sum_two_smallest_positives([1, 1, 2, 3]))
# print(sum_two_smallest_positives([5, 5, 5, 5]))


# def has_unique_chars(data: str):
#     all_chars = []
#
#     for char in data:
#         if char in all_chars:
#             return False
#
#         all_chars.append(char)
#
#     return True
#
#
# print(has_unique_chars("abcdef"))     # True
# print(has_unique_chars("hello"))      # False
# print(has_unique_chars("Python!"))    # True
# print(has_unique_chars("123 321"))    # False


# def is_balanced(data: str):
#     only_parentheses = data
#
#     for char in only_parentheses:
#         if char not in '()':
#             only_parentheses = only_parentheses.replace(char, '')
#
#     if only_parentheses.count('(') != only_parentheses.count(')'):
#         return False
#
#     parentheses = []
#
#     for parenthesis in only_parentheses:
#         parentheses.append(parenthesis)
#
#     while parentheses:
#         if parentheses.index('(') < parentheses.index(')'):
#             parentheses.remove('(')
#             parentheses.remove(')')
#         else:
#             return False
#
#     return True
#
#
# print(is_balanced("(hello(world))"))        # True
# print(is_balanced("((())())"))              # True
# print(is_balanced(")()("))                    # False
# print(is_balanced("(()"))                   # False
# print(is_balanced("text (with (parentheses))"))  # True
# print(is_balanced("(a + b) * c")) # True
# print(is_balanced("()"))          # True
# print(is_balanced("(())"))        # True
# print(is_balanced("(()"))         # False
# print(is_balanced(")("))          # False
# print(is_balanced("(()())())"))   # False


# test4 = [0, 1, 2, 3, 4, 10, 11, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30]
#
# def longest_consecutive(nums):
#     sorted_nums = sorted(nums)
#
#     ranges = [[sorted_nums[0]]]
#
#     i = 0
#
#     range_index = 0
#
#     while i != len(sorted_nums) - 1:
#         if sorted_nums[i + 1] - sorted_nums[i] == 1:
#             ranges[range_index].append(sorted_nums[i + 1])
#             i += 1
#         else:
#             ranges.append([sorted_nums[i + 1]])
#             range_index += 1
#             i += 1
#
#     return len(max(ranges, key=lambda rang: len(rang)))
#
#
# print(longest_consecutive(test4))


# def count_unique_words(data):
#     import string
#
#     data_copy = data.lower()
#
#     for char in string.punctuation:
#         data_copy = data_copy.replace(char, '')
#
#     words_sep = data_copy.split()
#
#     words_set = set(words_sep)
#
#     return len(words_set)
#
#
# print(count_unique_words("Hello, hello! How are you? You look well."))


# def find_missing_number(data):
#     sorted_nums = sorted(data)
#
#     for i in range(len(sorted_nums) - 1):
#         if abs(sorted_nums[i] - sorted_nums[i + 1]) != 1:
#             return sorted_nums[i] + 1
#
#     if not 0 in sorted_nums:
#         return 0
#
#     return sorted_nums[-1] + 1
#
#
# print(find_missing_number([3, 0, 1]))
# print(find_missing_number([0, 1]))     # ➜ 2
# print(find_missing_number([9,6,4,2,3,5,7,0,1]))  # ➜ 8
# print(find_missing_number([0]))             # ➜ 1
# print(find_missing_number([1]))             # ➜ 0
# print(find_missing_number([0,2,3]))         # ➜ 1
# print(find_missing_number([4,3,2,0]))        # ➜ 1

# print(run_length_encoding("aaabbcaaa"))  # ➜ [('a', 3), ('b', 2), ('c', 1), ('a', 3)]
# print(run_length_encoding("wwwwaaadexxxxxx"))  # ➜ [('w', 4), ('a', 3), ('d', 1), ('e', 1), ('x', 6)]


# def run_length_encoding(data):
#     result = []
#
#     index_compared_char = 0
#
#     counter = 1
#
#     for i in range(1, len(data)):
#         if data[index_compared_char] == data[i]:
#             counter += 1
#         else:
#             result.append((data[index_compared_char], counter))
#             counter = 1
#             index_compared_char = i
#
#     result.append((data[index_compared_char], counter))
#
#     return result
#
# run_length_encoding('wwwwaaadexxxxxx')


# def unique_digit_numbers(data: list):
#     nums_str = []
#
#     result = []
#
#     for num in data:
#         nums_str.append(str(num))
#
#     for string in nums_str:
#         if len(str(string)) == len(''.join((list(set(string))))):
#             result.append(int(string))
#
#     return result
#
# print(unique_digit_numbers([123, 112, 456, 9876, 998]))
# print(unique_digit_numbers([123, 112, 456, 9876, 998, 0, 1210, 102345, 444, 890, 1001]))


# def full_reverse(data: str):
#     result = []
#
#     for i in range(len(data) - 1, -1, -1):
#         result.append(data[i])
#
#     return ''.join(result)
#
#
# print(full_reverse('Hello, world!'))

# "olleH, dlrow!
# def reverse_string_keep_punctuation(data: str):
#     import string
#
#     data_syms = []
#
#     for i in range(len(data) - 1, -1, -1):
#         data_syms.append(data[i])
#
#     result = []
#
#     for symbol in data:
#         if symbol in string.punctuation or symbol == ' ':
#             result.append(symbol)
#             data_syms.remove(symbol)
#         else:
#             result.append('_')
#
#     index_result = 0
#
#     index_letter = 0
#
#     while index_result <= len(result) - 1:
#         if result[index_result] == '_':
#             result[index_result] = data_syms[index_letter]
#             index_result += 1
#             index_letter += 1
#         else:
#             index_result += 1
#
#     return ''.join(result)
#
#
# print(reverse_string_keep_punctuation("Hello, world!"))

# def cap_first_letter(word):
#     return word[0].upper() + word[1:]
#
#
# def capitalize_sentences(data: str):
#     words_incl_punctuation = data.split()
#
#     words_cap = [cap_first_letter(words_incl_punctuation[0])]
#
#     for i in range(1, len(words_incl_punctuation)):
#         if words_incl_punctuation[i - 1].endswith(('!', '.', '?')):
#             words_cap.append(cap_first_letter(words_incl_punctuation[i]))
#         else:
#             words_cap.append(words_incl_punctuation[i])
#
#     return ' '.join(words_cap)
#
#
# print(capitalize_sentences("hello world. how are you? i'm fine! and you?"))
# # ➜ "Hello world. How are you? I'm fine!"


# # 1. Сжатие и восстановление строк
# # ⚙️ Run-Length Encoding (RLE)
# # Напиши пару функций:
# #
# # одна сжимает строку "aaaabbbcc" в "a4b3c2",
# #
# # другая восстанавливает обратно.
#
#
# def convert_letters_sequence(data: str):
#     sequences = [[data[0]]]
#
#     index_letter = 0
#
#     index_sequence = 0
#
#     while index_letter <= len(data) - 2:
#         if sequences[index_sequence][0] == data[index_letter + 1]:
#             sequences[index_sequence].append(data[index_letter + 1])
#             index_letter += 1
#         else:
#             sequences.append([data[index_letter + 1]])
#             index_sequence += 1
#             index_letter += 1
#
#     result = []
#
#     for sequence in sequences:
#         result.append((sequence[0], len(sequence)))
#
#     output = ''
#
#     for couple in result:
#         output += couple[0] + str(couple[1])
#
#     return output
#
#
# print(convert_letters_sequence("aaaaaaaaaaaaaaaaaaaaaaaabbbbccc"))
#
# word = 'A2b5'
#
# def restore_converted_sequences(data: str):
#     all_chars = []
#
#     for char in data:
#         all_chars.append(char)
#
#     print(all_chars)
#
#     alphabet = []
#
#     nums = []
#
#     for i in range(len(all_chars)):
#         if all_chars[i].isalpha():
#             alphabet.append(all_chars[i])
#         else:
#             nums.append(all_chars[i])
#             if i == len(all_chars) - 1:
#                 break
#
#             if not all_chars[i + 1].isdigit():
#                 nums.append(', ')
#
#
#     numbers = ''.join(nums)
#
#     numbers_split = numbers.split(', ')
#
#     output = ''
#
#     for i in range(len(alphabet)):
#         output += alphabet[i] * int(numbers_split[i])
#
#     print(output)
#
#
# restore_converted_sequences(word)


# 2. Анализ слов в тексте
# 📊 Функция получает текст и находит:
#
# самое частое слово,
#
# среднюю длину слов,
#
# 3 самых длинных слова (разные).

# def get_stats(text: str):
#     import string
#
#     if not text:
#         print('Поле пустое')
#         return
#
#     for char in string.punctuation:
#         text = text.replace(char, '')
#
#     text = text.strip().lower()
#
#     words_split = text.split()
#
#     words = {}
#
#     for word in words_split:
#         if word in words:
#             words[word] += 1
#         else:
#             words[word] = 1
#
#     avg_chars_per_word = len(''.join(words_split)) / len(words) # средняя длина уникальных слов
#
#     words_sorted_to_check_most_frequent = sorted(words, key=lambda each_word: words[each_word], reverse=True)
#
#     most_frequent_word = words_sorted_to_check_most_frequent[0] # самое часто слово
#
#     words_sorted_to_check_longest = sorted(words_sorted_to_check_most_frequent, key=lambda each_word: len(each_word), reverse=True)
#
#     top_3_longest_words = words_sorted_to_check_longest[0:3] # 3 самые длинные слова
#
#     print(f'Статистика текста:\n1) средняя длина слова - {avg_chars_per_word}\n2) самое часто слово - {most_frequent_word}\n3) топ-3 самых длинных слова: {', '.join(top_3_longest_words)}')
#
#
# get_stats('   Метод .get() чаще get всего Python используется в Python для работы со словарями (dict). Он позволяет безопасно получить значение по ключу, Python избегая ошибки, если ключ не существует. метод ')


# Список строк (отзывы пользователей):

# ✅ Функция должна:
# Очистить текст от пунктуации, привести к нижнему регистру.

# Разбить на слова и подсчитать частоты (один общий словарь для всех отзывов).

# Найти:
# 🔸 Топ-5 самых частых слов
# 🔸 Среднюю длину слова (по всем словам)
# 🔸 Уникальные слова, которые встречаются только один раз
# 🔸 Количество слов, встречающихся более 2 раз
# Вернуть словарь с результатами.

# reviews = [
#     "Продукт отличный отличный, пользуюсь каждый день! ",
#     "Очень плохое качество. Не рекомендую.",
#     "  Отличный сервис и быстрая доставка.",
#     "Качество товара хорошее, но упаковка была повреждена.      ",
#     "Хорошее соотношение цены и качества.",
#     "   Ужасная упаковка. Всё было вскрыто.",
#     "Очень доволен покупкой, спасибо!"
# ]
#
# def process_reviews(data: list):
#     import string
#
#     data_copy = []
#
#     for review in data:
#         for symbol in string.punctuation:
#             review = review.replace(symbol, '')
#         review = review.strip().lower()
#         data_copy.append(review)
#
#     all_words = {}
#
#     all_words_with_duplicates = []
#
#     for review in data_copy:
#         words = review.split()
#         for word in words:
#             all_words_with_duplicates.append(word)
#
#             if word in all_words:
#                 all_words[word] += 1
#             else:
#                 all_words[word] = 1
#
#     all_chars = ''.join(all_words_with_duplicates)
#
#     top_5_frequency = list(sorted(all_words, key=lambda key: all_words[key], reverse=True))[:5] # 5 самых частых слов
#
#     avg_word_length = len(all_chars) / len(all_words_with_duplicates) # средняя длина всех слов
#
#     only_1_appearance = list(filter(lambda key: all_words[key] == 1, all_words)) # слова, которые встречаются лишь 1 раз
#
#     more_than_2_appearances = list(filter(lambda key: all_words[key] > 2, all_words)) # слова, которые встречаются более 2 раз
#
#     return {
#         '5 самых частых слов': ', '.join(top_5_frequency),
#         'средняя длина всех слов': avg_word_length,
#         'слова, которые встречаются лишь 1 раз': ', '.join(only_1_appearance),
#         'слова, которые встречаются более 2 раз': ', '.join(more_than_2_appearances)
#     }
#
#
# print(process_reviews(reviews))


# from transformers import pipeline
#
# # Загружаем модель анализа тональности на русском
# classifier = pipeline("sentiment-analysis", model="blanchefort/rubert-base-cased-sentiment")
#
# # Отзывы
# reviews = [
#     "Продукт отличный отличный, пользуюсь каждый день! ",
#     "Очень плохое качество. Не рекомендую.",
#     "  Отличный сервис и быстрая доставка.",
#     "Качество товара хорошее, но упаковка была повреждена.      ",
#     "Хорошее соотношение цены и качества.",
#     "   Ужасная упаковка. Всё было вскрыто.",
#     "Очень доволен покупкой, спасибо!"
# ]
#
# # Словарь для сбора результатов
# results = {"POSITIVE": [], "NEUTRAL": [], "NEGATIVE": []}
#
# # Обработка отзывов
# for review in reviews:
#     review_clean = review.strip()
#     result = classifier(review_clean)[0]
#     label = result["label"]
#     score = round(result["score"], 3)
#     results[label].append((review_clean, score))
#
# # Вывод результата
# print("📊 Результаты анализа тональности:\n")
#
# for label, comments in results.items():
#     print(f"➡️ {label} ({len(comments)} отзывов):")
#     for comment, score in comments:
#         print(f"  - {comment} [уверенность: {score}]")
#     print()

# Чёт‑нечёт за одно выражение

# def even_odd(data: list):
#     return sorted(sorted(data), key=lambda num: num % 2 != 0)
#
#
# print(even_odd([5, 2, 8, 3, 45, 33, 12, 80]))


# Самое длинное слово
# ["Anna", "bella", "Charlie", "adam", "Bob", "alex", "Zoe", "zoe", "ALAN"]

# def max_len_word(data: list):
#     return max(sorted(data ,reverse=True), key=lambda word: len(word))
#
#
# print(max_len_word(["Anna", "bella", "Charlie", "adam", "Bob", "alex", "Zoe", "zoe", "ALAN", 'Ukraine']))


# Минимум по сумме цифр
# Есть список положительных чисел. Верни то, у которого наименьшая сумма цифр; при равенстве — самое меньшее число.

# numbers = [18, 29, 19, 42, 33, 91, 27, 81, 9, 123, 11, 20]
#
# def sum_of_dig(num: int):
#     result = 0
#
#     while num != 0:
#         result += num % 10
#         num = num // 10
#
#     return result
#
#
# def min_num_len(data: list):
#     list_of_sums = list(map(lambda num: sum_of_dig(num), data))
#
#     result_sum = min(list_of_sums)
#
#     if list_of_sums.count(result_sum) > 1:
#         return min(list(filter(lambda num: sum_of_dig(num) == result_sum, data)))
#
#     return result_sum
#
#
# print(min_num_len(numbers))


# Условие:
# Список словарей вида {"name": "Anna", "scores": [80, 98, 91]}.
# Задача:
# Отсортировать по убыванию среднего значения scores, при равенстве — по name в алфавитном порядке.

# students = [
#             {"name": "Anna", "scores": [100, 100, 90]},
#             {"name": "Borys", "scores": [100, 90, 100]},
#             {'name': 'Jhon', 'scores':  [100, 85, 60]}
# ]
#
# def sort_students(data: list):
#     return sorted(data, key= lambda name_score: (sum(name_score['scores']) / len(name_score['scores']), name_score['name']))
#
# print(sort_students(students))


# 📌 Задание
# Найти имя самого молодого человека по дате рождения.

# names = [
#     {"name": "Anna", "birth": "2001-03-15"},
#     {"name": "Borys", "birth": "1999-07-22"},
#     {"name": "Daria", "birth": "2003-01-10"},
#     {"name": "Igor", "birth": "2003-01-09"}
# ]
#
# def get_youngest(data: list):
#     from datetime import datetime
#
#     new_list = sorted(data, key= lambda name_dob: datetime.fromisoformat(name_dob['birth']), reverse= True)
#
#     return new_list[0]['name']
#
# print(get_youngest(names))


# 3. Фильтрация файлов по расширению
# Ввод: список имён файлов: ["data.csv", "photo.png", "script.py", "report.pdf"]
# Задача: оставить только .py и .csv, отсортировать по алфавиту

# def filter_files(data: list):
#     return sorted(list(filter(lambda file: file.endswith('.py') or file.endswith('.csv'), data)))
#
#
# print(filter_files(["data.csv", "photo.png", "script.py", "report.pdf"]))


# 🔹 4. Найти самую длинную строку, не содержащую цифр
# Ввод: список строк
# Задача: выбрать самую длинную, где нет цифр. При равенстве — первую по порядку.

# words = [
#     "hello123",
#     "world",
#     "Python",
#     "clean_string_example",
#     "test1234",
#     "onother_clean_example",
#     "short",
#     "12345",
#     'another_clean_example'
# ]
#
# def if_no_dig(word: str):
#     for char in word:
#         if char.isdigit():
#             return False
#
#     return True
#
#
# def get_longest_no_dig(data: list):
#     return max(list(filter(lambda log: if_no_dig(log), data)), key=len)
#
#
# print(get_longest_no_dig(words))


#  5. Самый частый элемент
# Ввод: список элементов (числа, строки — не важно)
# Вывод: тот элемент, который встречается чаще других. Если таких несколько — любой.

# words = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "banana", "banana", 'apple']
#
# def most_freq(data: list):
#     word_count = {}
#
#     for word in data:
#         word_count[word] = word_count.get(word, 0) + 1
#
#     return max(word_count.keys(), key=lambda key: word_count[key])
#
#
# print(most_freq(words))


# 🔹 7. Удалить повторяющиеся строки (без учёта регистра)
# Ввод: список строк
# Вывод: список уникальных строк (регистр игнорируется), порядок — как первое вхождение

# not_set = [
#     "Apple",
#     "banana",
#     "APPLE",
#     "Banana",
#     "Cherry",
#     "cherry",
#     "apple",
#     "BANANA"
# ]
#
# def get_set(data: list):
#     equalized_data = list(map(lambda word: word.lower().capitalize(), data))
#
#     return list(set(equalized_data))
#
#
# print(get_set(not_set))


# 🔹 6. Группировка по первой букве имени
# Ввод: список имён
# Вывод: словарь, где ключ — первая буква, значение — список имён на эту букву (в алфавитном порядке внутри)
#
# данные:

# names = [
#     "Anna",
#     "Albert",
#     "Borys",
#     "Beata",
#     "Aneta",
#     "Barbara",
#     "Igor",
#     "Irena",
#     "Ivan",
#     "Andrzej"
# ]
#
# def get_alpha(data: list):
#     output = {}
#
#     for word in data:
#         if word[0] not in output:
#             output[word[0]] = [word]
#         else:
#             output[word[0]].append(word)
#
#     for letter in output:
#         output[letter] = sorted(output[letter])
#
#     return output
#
#
# print(get_alpha(names))


# Задача:
#
# Оставить только активных пользователей.
#
# Посчитать, какие курсы встречаются чаще всего.
#
# Вернуть топ-3 самых популярных курса среди активных пользователей (в виде списка названий курсов).

# users = [
#     {"name": "Anna", "courses": ["Python", "SQL"], "active": True},
#     {"name": "Borys", "courses": ["Python", "HTML", "CSS"], "active": False},
#     {"name": "Daria", "courses": ["SQL", "Python"], "active": True},
#     {"name": "Igor", "courses": ["HTML", "CSS", "JavaScript"], "active": True},
#     {"name": "Oksana", "courses": ["Python", "JavaScript"], "active": True},
#     {"name": "Tom", "courses": ["C++", "Python"], "active": False},
#     {"name": "Lena", "courses": ["SQL", "Excel"], "active": True},
#     {"name": "Max", "courses": ["Excel", "Python", "Java"], "active": True},
#     {"name": "Sofia", "courses": ["Java", "Python", "HTML"], "active": True},
#     {"name": "Roman", "courses": ["Python", "CSS"], "active": True},
#     {"name": "Eva", "courses": ["SQL", "Python", "HTML"], "active": True},
#     {"name": "Yurii", "courses": ["Go", "Python"], "active": False},
#     {"name": "Nina", "courses": ["Excel", "Python", "SQL"], "active": True},
# ]
#
#
# def analyze_users_data(data: list):
#     active_users = list(filter(lambda user: user['active'], data))
#
#     courses_popularity = {}
#
#     for user in active_users:
#         for course in user['courses']:
#             courses_popularity[course] = courses_popularity.get(course, 0) + 1
#
#     courses_popularity = sorted(courses_popularity, key=lambda course: courses_popularity[course], reverse=True)
#
#     return courses_popularity[0:3] # топ три самых популярных курса среди активных пользоавтелей
#
# print(analyze_users_data(users))


# 🔷 ЗАДАЧА 2. Форматирование и группировка заказов
# Ввод: список кортежей вида (имя клиента, сумма, категория):

# Задача:
#
# Сгруппировать по имени клиента.
#
# Для каждого клиента составить словарь:
# {"total": общая сумма заказов, "categories": список уникальных категорий (в алфавитном порядке)}
#
# Вернуть общий словарь, где ключ — имя клиента, значение — этот словарь.


# orders = [
#     ("Anna", 120.50, "books"),
#     ("Borys", 540.00, "tech"),
#     ("Anna", 75.00, "books"),
#     ("Daria", 300.00, "clothing"),
#     ("Igor", 220.00, "tech"),
#     ("Anna", 45.00, "clothing"),
#     ("Borys", 120.00, "books"),
#     ("Daria", 90.00, "books"),
#     ("Oksana", 310.00, "tech"),
#     ("Igor", 150.00, "books"),
#     ("Tom", 80.00, "clothing"),
#     ("Sofia", 500.00, "tech"),
#     ("Anna", 60.00, "books"),
#     ("Oksana", 95.00, "clothing"),
#     ("Borys", 75.00, "clothing"),
#     ("Daria", 200.00, "tech"),
#     ("Tom", 120.00, "books"),
#     ("Max", 600.00, "tech"),
#     ("Sofia", 135.00, "books"),
#     ("Max", 75.00, "clothing"),
# ]
#
# def systematize_users(data: list):
#     users = {}
#
#     for log in data:
#         if log[0] not in users:
#             users[log[0]] = {'total': log[1], 'categories': [log[2]]}
#         else:
#             users[log[0]]['total'] += log[1]
#             users[log[0]]['categories'].append(log[2])
#
#     for user in users:
#         users[user] = {'total': users[user]['total'], 'categories': sorted(list(set(users[user]['categories'])))}
#
#     return users
#
#
# print(systematize_users(orders))


# 🔷 ЗАДАЧА 3. Фильтрация и преобразование логов
# Ввод: список строк — каждый элемент в формате "2024-07-18 12:30:45 - ERROR - something bad happened"
# Форматы уровней: "INFO", "WARNING", "ERROR", "DEBUG" и т.д.
#
# Задача:
#
# Оставить только записи с уровнем "ERROR" и "WARNING".
#
# Преобразовать в список словарей с ключами: timestamp, level, message.
# Пример:

# {
#     "timestamp": "2024-07-18 12:30:45",
#     "level": "ERROR",
#     "message": "something bad happened"
# }
# Отсортировать результат по времени (от самых старых к новым).


# log_lines = [
#     "2024-07-18 12:30:45 - ERROR - something bad happened",
#     "2024-07-18 12:31:01 - INFO - user logged in",
#     "2024-07-18 12:31:15 - DEBUG - checking user session",
#     "2024-07-18 12:32:03 - WARNING - disk space low",
#     "2024-07-18 12:32:45 - ERROR - file not found",
#     "2024-07-18 12:33:07 - INFO - new user registered",
#     "2024-07-18 12:33:58 - ERROR - database connection failed",
#     "2024-07-18 12:34:42 - DEBUG - query executed",
#     "2024-07-18 12:35:16 - INFO - email sent",
#     "2024-07-18 12:35:55 - WARNING - CPU usage high",
#     "2024-07-18 12:36:21 - ERROR - timeout occurred",
#     "2024-07-18 12:37:00 - INFO - cache cleared",
#     "2024-07-18 12:37:45 - DEBUG - config loaded",
#     "2024-07-18 12:38:30 - INFO - backup started",
#     "2024-07-18 12:39:12 - WARNING - unusual traffic detected",
#     "2024-07-18 12:39:50 - ERROR - permission denied",
#     "2024-07-18 12:40:33 - DEBUG - retrying operation",
#     "2024-07-18 12:41:17 - INFO - logout successful",
#     "2024-07-18 12:42:00 - WARNING - deprecated API used",
#     "2024-07-18 12:42:45 - ERROR - out of memory",
# ]
#
#
# def get_log_json(data: list):
#     import datetime
#
#     only_relevant = list(filter(lambda log: 'ERROR' in log or 'WARNING' in log, data))
#
#     output = []
#
#     for log in only_relevant:
#         output.append({'timestamp': log[0:19], 'level': log.split(' - ')[1], 'message': log.split(' - ')[-1]})
#
#     output.sort(key=lambda log: datetime.datetime.fromisoformat(log['timestamp']))
#
#     return output
#
#
# print(get_log_json(log_lines))


# Задача 1. Подсчёт средних значений в группах
# Ввод: список кортежей с именем и числовым значением, например:

# Задача: для каждого имени посчитать среднее значение и вернуть словарь с именами и средними.

# names = [
#     ("Anna", 10),
#     ("Borys", 15),
#     ("Anna", 20),
#     ("Daria", 25),
#     ("Borys", 5)
# ]
#
# def count_avg(data: list):
#     output = {}
#
#     for user in data:
#         if user[0] not in output:
#             output[user[0]] = [user[1]]
#         else:
#             output[user[0]].append(user[1])
#
#     for user in output:
#         output[user] = sum(output[user]) / len(output[user])
#
#     return output
#
#
# print(count_avg(names))


# Задача 2. Объединение словарей с подсчётом
# Ввод: список словарей, например:
#
# Задача: объединить все словари в один, суммируя значения по ключам.

# dicts = [
#     {"apple": 10, "banana": 5},
#     {"banana": 7, "cherry": 3},
#     {"apple": 3, "cherry": 8, "date": 1}
# ]
#
# def utilize_duplicates(data: list):
#     output = {}
#
#     for basket in data:
#         for fruit in basket:
#             if fruit not in output:
#                 output[fruit] = basket[fruit]
#             else:
#                 output[fruit] += basket[fruit]
#
#
#     return output
#
#
# print(utilize_duplicates(dicts))


# Задача 3. Проверка на анаграмму
# Ввод: две строки
#
# Задача: определить, являются ли строки анаграммами — то есть содержат одинаковый набор букв, но в любом порядке (без учёта регистра и пробелов).


# def is_anagram(data1: str, data2: str):
#     data1.lower().replace(' ', '')
#     data2.lower().replace(' ', '')
#
#     data1_letters = {}
#
#     for char in data1:
#         data1_letters[char] = data1_letters.get(char, 0) + 1
#
#     data2_letters = {}
#
#     for char in data2:
#         data2_letters[char] = data2_letters.get(char, 0) + 1
#
#     if data1_letters == data2_letters:
#         return True
#
#     return False
#
#
# print(is_anagram('hello', 'lolhe'))


# Задача 5. Фильтрация и преобразование списка строк
# Ввод: список строк с разными датами.
#
# Задача: оставить только корректные даты в формате YYYY-MM-DD и преобразовать их в объекты datetime.date.

# dates = [
#     "2023-05-12",
#     "not-a-date",
#     "2024-01-01",
#     "hello",
#     "2023-12-31"
# ]
#
# import datetime
#
# def is_iso_format(data: str):
#     try:
#         test = datetime.datetime.fromisoformat(data)
#     except ValueError:
#         return False
#
#     return True
#
#
# def get_iso_objects(data: list):
#     correct_data = list(filter(lambda iso: is_iso_format(iso), data))
#
#     return list(map(lambda iso: datetime.date(int(iso.split('-')[0]), int(iso.split('-')[1]), int(iso.split('-')[2])), correct_data))
#
#
# print(get_iso_objects(dates))


# Задача 6. Найти пересечение списков с уникальными элементами
# Ввод: два списка чисел.
#
# Задача: вернуть список с уникальными числами, которые есть в обоих списках (пересечение), без повторов.

# list1 = [1, 2, 2, 3, 4]
# list2 = [2, 3, 5, 3]
#
# def get_intersections(data1: list, data2: list):
#     return set(data1).intersection(set(data2))
#
#
# print(get_intersections(list1, list2))


# Задача 1. Частотный анализ текста
# Дан текст (строка). Подсчитай, сколько раз каждое слово встречается. Верни словарь, где ключ — слово, значение — количество.

# text = "apple banana apple cherry banana apple cherry"
#
# def count_uniques(data: str):
#     output = {}
#
#     for word in data.split():
#         output[word] = output.get(word, 0) + 1
#
#     return output
#
#
# print(count_uniques(text))


# Задача:
# Раздели слова по длине. Верни словарь, где ключ — длина слова, значение — список слов такой длины.

# words = ["dog", "cat", "house", "tree", "car", "book", "sky"]
#
# def separate_length(data: list):
#     output = {}
#
#     for word in data:
#         if len(word) not in output:
#             output[len(word)] = [word]
#         else:
#             output[len(word)].append(word)
#
#     return output
#
#
# print(separate_length(words))


# Задача:
# Оставь только те элементы, у которых info["status"] == "active".

# logs = [
#     {"name": "Anna", "info": {"status": "active"}},
#     {"name": "Borys", "info": {"status": "inactive"}},
#     {"name": "Daria", "info": {"status": "active"}},
#     {"name": "Ivan", "info": {"status": "blocked"}},
# ]
#
# def get_active(data: list):
#     return list(filter(lambda log: log['info']['status'] == 'active', data))
#
# print(get_active(logs))


# Задача:
# Верни пользователей, у которых общая сумма трат превышает threshold.

# transactions = [
#     ("Anna", 120.50, "books"),
#     ("Borys", 540.00, "tech"),
#     ("Anna", 75.00, "books"),
#     ("Daria", 300.00, "clothing"),
#     ("Borys", 100.00, "books"),
#     ("Anna", 55.50, "tech"),
# ]
#
# threshold = 200
#
# def get_overdrawn(users: list, edge: (int, float) = 200):
#     return list(filter(lambda user: user[1] > edge, users))
#
# print(get_overdrawn(transactions))


# Найди все уникальные слова без учёта регистра и знаков препинания.

# import string
#
# sentences = [
#     "Hello world!",
#     "Python is great.",
#     "Hello Python",
#     "WORLD of code"
# ]
#
#
# def all_uniques(data: list):
#     merged_strings = ' '.join(data).lower()
#
#     for char in string.punctuation:
#         merged_strings = merged_strings.replace(char, '')
#
#     return set(merged_strings.split())
#
#
# print(all_uniques(sentences))


# Задача 1. Выбор уникальных пользователей по последнему действию
#
# Оставь в списке только последнее действие каждого пользователя.

# logs = [
#     {"user": "Anna", "action": "login1"},
#     {"user": "Borys", "action": "logout1"},
#     {"user": "Anna", "action": "logout2"},
#     {"user": "Daria", "action": "login1"},
#     {"user": "Borys", "action": "login2"},
#     {"user": "Anna", "action": "login3"},
#     {"user": "Daria", "action": "login2"}
# ]
#
#
# def last_log(data: list):
#     logs_by_name = {}
#
#     for log in data:
#         if log['user'] not in logs_by_name:
#             logs_by_name[log['user']] = [log]
#         else:
#             logs_by_name[log['user']].append(log)
#
#     output = []
#
#     for name in logs_by_name:
#         output.append(logs_by_name[name][-1])
#
#     return output
#
#
# print(last_log(logs))


# Задача 2. Группировка по категориям

# Сгруппируй элементы по категории. Верни словарь: категория → список названий.

# items = [
#     {"name": "MacBook", "category": "tech"},
#     {"name": "Banana", "category": "food"},
#     {"name": "iPhone", "category": "tech"},
#     {"name": "Bread", "category": "food"},
#     {"name": "T-shirt", "category": "clothing"},
# ]
#
# def get_categorized(data: list):
#     output = {}
#
#     for item in data:
#         if item['category'] not in output:
#             output[item['category']] = [item['name']]
#         else:
#             output[item['category']].append(item['name'])
#
#     return output
#
#
# print(get_categorized(items))


# Задача 3. Выделение самых дорогих покупок

# Для каждого пользователя найди самую дорогую покупку. Верни словарь: имя → максимальная сумма.

# purchases = [
#     {"user": "Anna", "price": 540},
#     {"user": "Borys", "price": 540},
#     {"user": "Daria", "price": 190},
#     {"user": "Anna", "price": 320},
#     {"user": "Ivan", "price": 150},
# ]
#
#
# def get_most_expensive(data: list):
#     output = {}
#
#     data.sort(key=lambda purchase: purchase['price'])
#
#     for purchase in data:
#         output[purchase['user']] = purchase['price']
#
#     return output
#
#
# print(get_most_expensive(purchases))


# Задача 4. Отсортировать пользователей по сумме покупок
#
# Подсчитай общую сумму заказов на каждого и отсортируй пользователей по убыванию этой суммы.

# orders = [
#     ("Anna", 100),
#     ("Borys", 300),
#     ("Anna", 200),
#     ("Daria", 50),
#     ("Borys", 250),
#     ("Daria", 150),
# ]
#
#
# def sum_orders(data: list):
#     output = {}
#
#     for order in data:
#         if order[0] not in output:
#             output[order[0]] = order[1]
#         else:
#             output[order[0]] += order[1]
#
#     return sorted(list(output.items()), key=lambda user: user[1], reverse=True)
#
#
# print(sum_orders(orders))


# Задача 5. Подсчёт слов по первой букве

# Верни словарь, где ключ — первая буква слова, значение — количество слов, начинающихся с этой буквы.

# words = ["apple", "ant", "banana", "book", "car", "camera", "cat"]
#
# def get_first_letter_sum(data: list):
#     output = {}
#
#     for word in data:
#         output[word[0]] = output.get(word[0], 0) + 1
#
#     return output
#
#
# print(get_first_letter_sum(words))


#  Задача 1. Последовательные действия пользователей
# Условие:
# У тебя есть список логов с действиями пользователей. Нужно сгруппировать действия по пользователям и отсортировать их по времени.

# logs = [
#     {"user": "Anna", "action": "login", "timestamp": 3},
#     {"user": "Borys", "action": "logout", "timestamp": 8},
#     {"user": "Anna", "action": "view", "timestamp": 5},
#     {"user": "Daria", "action": "login", "timestamp": 2},
#     {"user": "Anna", "action": "logout", "timestamp": 9},
#     {"user": "Daria", "action": "view", "timestamp": 4},
# ]
#
# def group_actions_by_user(data: list):
#     output = {}
#
#     sorted_data = list(sorted(data, key=lambda log: log['timestamp']))
#
#     for log in sorted_data:
#         if log['user'] not in output:
#             output[log['user']] = [log['action']]
#         else:
#             output[log['user']].append(log['action'])
#
#     return output
#
#
# print(group_actions_by_user(logs))

# Задача 2. Слияние двух источников по ID
# Условие:
# Есть два списка словарей: один с пользователями, другой с заказами. Нужно объединить информацию: имя пользователя и его заказы.

# users = [
#     {"id": 1, "name": "Anna"},
#     {"id": 2, "name": "Borys"},
#     {"id": 3, "name": "Daria"}
# ]
#
# orders = [
#     {"user_id": 3, "product": "T-shirt"},
#     {"user_id": 1, "product": "Laptop"},
#     {"user_id": 1, "product": "Phone"},
#     {"user_id": 2, "product": "Book"},
#     {"user_id": 2, "product": "Shoes"},
# ]
#
#
# def merge_name_and_product(data1:list,  data2: list):
#     data2.sort(key=lambda id_product: id_product['user_id'])
#
#     output = {}
#
#     id_and_user = []
#
#     for user in data1:
#         id_and_user.append((user['id'], user['name']))
#
#     for order in data2:
#         if order['user_id'] not in output:
#             output[order['user_id']] = [order['product']]
#         else:
#             output[order['user_id']].append(order['product'])
#
#     output_items = list()
#
#     for id_items in output.items():
#         output_items.append(id_items)
#
#     result = {}
#
#     for i in range(len(output_items)):
#         result[id_and_user[i][1]] = output_items[i][1]
#
#     return result
#
#
# print(merge_name_and_product(users, orders))


# 🧩 Задача 3. Поиск аномалий
# Условие:
# В списке температур найти такие значения, которые отличаются от среднего более чем на threshold градусов.

# temperatures = [21.5, 20.8, 22.1, 30.0, 21.0, 35.5, 20.5]
# threshold = 5.0
#
# def get_deviant(temps: list, edge: (int, float)):
#     average = sum(temps) / len(temps)
#
#     return list(filter(lambda temp: abs(temp - average) > edge, temps))
#
#
# print(get_deviant(temperatures, threshold))

# Задача 4. Сортировка и группировка книг
# Условие:
# Есть список книг. Отсортируй их по году, а потом сгруппируй по автору.

# books = [
#     {"title": "Python 101", "author": "Anna", "year": 2020},
#     {"title": "Deep Dive", "author": "Anna", "year": 2022},
#     {"title": "Learn Java", "author": "Borys", "year": 2019},
#     {"title": "Web Dev", "author": "Anna", "year": 2018},
#     {"title": "React Guide", "author": "Borys", "year": 2021},
# ]
#
# def create_library(data: list):
#     data.sort(key=lambda book: book['year'])
#
#     result = {}
#
#     for book in data:
#         if book['author'] not in result:
#             result[book['author']] = [{'title': book['title'], 'year': book['year']}]
#         else:
#             result[book['author']].append({'title': book['title'], 'year': book['year']})
#
#     return result
#
#
# print(create_library(books))


# Задача 1. Группировка комментариев по постам
# Условие: у тебя есть список комментариев. Каждый содержит post_id, user, comment. Нужно сгруппировать комментарии по post_id, сохранив только текст комментариев.


# comments = [
#     {"post_id": 1, "user": "Anna", "comment": "Nice post!"},
#     {"post_id": 2, "user": "Borys", "comment": "Interesting..."},
#     {"post_id": 1, "user": "Daria", "comment": "Agree!"},
#     {"post_id": 3, "user": "Ivan", "comment": "Not bad"},
#     {"post_id": 2, "user": "Anna", "comment": "Well written"},
# ]
#
# def get_comments(data: list):
#     result = {}
#
#     for post in data:
#         if post['post_id'] not in result:
#             result[post['post_id']] = [post['comment']]
#         else:
#             result[post['post_id']].append(post['comment'])
#
#     return result
#
#
# print(get_comments(comments))


# Задача 2. Объединение клиентов и городов
# Условие: Есть два списка — клиенты и города. Нужно сопоставить каждому клиенту название города по city_id.

# clients = [
#     {"id": 1, "name": "Anna", "city_id": 2},
#     {"id": 2, "name": "Borys", "city_id": 1},
#     {"id": 3, "name": "Daria", "city_id": 3},
# ]
#
# cities = [
#     {"id": 1, "city": "Warsaw"},
#     {"id": 2, "city": "Krakow"},
#     {"id": 3, "city": "Gdansk"},
# ]
#
#
# def get_user_location(users: list, locations: list):
#     result = []
#
#     for user in users:
#         for city in locations:
#             if user['city_id'] == city['id']:
#                 result.append({'name': user['name'], 'city': city['city']})
#
#
#     return result


# print(get_user_location(clients, cities))


# Задача 3. Последние статусы заказов
# Условие: Есть список обновлений заказов. Нужно оставить для каждого order_id только последний статус по timestamp.

# updates = [
#     {"order_id": 1, "status": "processing", "timestamp": 11},
#     {"order_id": 1, "status": "shipped", "timestamp": 46},
#     {"order_id": 2, "status": "pending", "timestamp": 56},
#     {"order_id": 2, "status": "cancelled", "timestamp": 12},
#     {"order_id": 3, "status": "processing", "timestamp": 8},
# ]
#
# def get_latest(data: list):
#     sorted_data = sorted(data, key=lambda update: update["timestamp"], reverse=True)
#
#     added_id = []
#
#     result = []
#
#     for order in sorted_data:
#         if order['order_id'] not in added_id:
#             result.append(order)
#             added_id.append(order['order_id'])
#
#     return sorted(result, key=lambda order: order['order_id'])
#
#
# print(get_latest(updates))


# Задача 1. Индексация постов по авторам и ключевым словам
# Задача:
# У тебя есть список постов — каждый с id, author, text.
# Нужно сгруппировать посты по авторам, а для каждого поста — извлечь уникальные ключевые слова:
#
# без стоп-слов ({"the", "is", "and", "a", "on", "in", "to"}),
#
# в нижнем регистре,
#
# без пунктуации.

# posts = [
#     {"id": 1, "author": "Anna", "text": "Python is clean and powerful."},
#     {"id": 2, "author": "Borys", "text": "Learning Python in 2025."},
#     {"id": 3, "author": "Anna", "text": "To write clean code is a skill."},
#     {"id": 4, "author": "Daria", "text": "Python and AI are trending."},
# ]
#
# stop_words = ("the", "is", "and", "a", "on", "in", "to")
#
# from string import punctuation
#
# def clear_text_and_lower(data: str, ignore: tuple):
#     data = data.lower()
#
#     for char in string.punctuation:
#         data = data.replace(char, '')
#
#     split_words = data.split()
#
#     result = []
#
#     for word in split_words:
#         if word not in stop_words:
#             result.append(word)
#
#     return result
#
# print(clear_text_and_lower('Python and AI are trending.', stop_words))
#
# def get_full_words(data: list):
#     result = {}
#
#     for post in data:
#         if post['author'] not in result:
#             result[post['author']] = [{'id': post['id'], 'keywords': clear_text_and_lower(post['text'], stop_words)}]
#         else:
#             result[post['author']].append({'id': post['id'], 'keywords': clear_text_and_lower(post['text'], stop_words)})
#
#     return result
#
#
# print(get_full_words(posts))


# Задача 3. Траты пользователей
# Задача:
# У тебя есть список заказов с:
#
# user_id,
#
# amount,
#
# currency.
#
# Нужно:
#
# Конвертировать все суммы в USD по курсам из словаря rates;
#
# Сгруппировать траты по пользователю;
#
# Вернуть топ-3 пользователей по сумме трат, округлённой до 2 знаков.

# orders = [
#     {"user_id": 1, "amount": 100, "currency": "EUR"},
#     {"user_id": 2, "amount": 200, "currency": "USD"},
#     {"user_id": 3, "amount": 1000, "currency": "PLN"},
#     {"user_id": 1, "amount": 150, "currency": "USD"},
#     {"user_id": 3, "amount": 150, "currency": "EUR"},
#     {"user_id": 4, "amount": 800, "currency": "PLN"},
#     {"user_id": 5, "amount": 50, "currency": "USD"},
# ]
#
# rates = {
#     "USD": 1.0,
#     "EUR": 1.1,
#     "PLN": 0.25
# }
#
# def convert_currency(order: dict, summa: int, rate: dict):
#     if order['currency'] == 'EUR':
#         summa = summa * rate['EUR']
#     elif order['currency'] == 'PLN':
#         summa = summa * rate['PLN']
#
#     return summa
#
#
# def get_data(users: list):
#     result = {}
#
#     for user in users:
#         if user['user_id'] not in result:
#             result[user['user_id']] = convert_currency(user, user['amount'], rates)
#         else:
#             result[user['user_id']] += convert_currency(user, user['amount'], rates)
#
#     result_list = list(result.items())
#
#     return dict(sorted(result_list, key=lambda couple: couple[1], reverse=True)[0:3])
#
#
# print(get_data(orders))


# Задача 1. Самые популярные теги
# Задача:
# Есть список постов с полем tags (список тегов).
# Нужно найти топ-5 самых часто используемых тегов во всех постах.

# posts = [
#     {"id": 1, "tags": ["python", "ai", "ml"]},
#     {"id": 2, "tags": ["python", "data", "ml"]},
#     {"id": 3, "tags": ["data", "cloud"]},
#     {"id": 4, "tags": ["cloud", "python"]},
#     {"id": 5, "tags": ["ml", "ai", "data"]},
# ]
#
# def get_rating(data: list):
#     result = {}
#
#     for post in data:
#         for tag in post['tags']:
#             result[tag] = result.get(tag, 0) + 1
#
#     return dict(sorted(result.items(), key=lambda couple: couple[1], reverse=True)[0:5])
#
#
# print(get_rating(posts))


# Задача 2. Отчёт по заказам
# Задача:
# У тебя есть список заказов. Нужно сгруппировать заказы по дате (date), и для каждой даты посчитать:
#
# * количество заказов,
#
# * общую сумму.


# orders = [
#     {"id": 1, "date": "2025-07-18", "amount": 100},
#     {"id": 2, "date": "2025-07-18", "amount": 50},
#     {"id": 3, "date": "2025-07-19", "amount": 70},
#     {"id": 4, "date": "2025-07-20", "amount": 30},
#     {"id": 5, "date": "2025-07-20", "amount": 90},
#     {"id": 6, "date": "2025-07-20", "amount": 60},
# ]
#
#
# def group_by_date(data: list):
#     total_sums = {}
#     total_orders = {}
#
#     for order in data:
#         total_sums[order['date']] = total_sums.get(order['date'], 0) + order['amount']
#         total_orders[order['date']] = total_orders.get(order['date'], 0) + 1
#
#     return total_sums, total_orders
#
#
# print(group_by_date(orders))


# Задача 3. Лента событий с сортировкой по пользователям
# Задача:
# Есть список событий от пользователей. Каждое событие содержит user_id, action, timestamp.
# Нужно:
#
# сгруппировать события по пользователям;
#
# отсортировать события каждого пользователя по времени.
#
# Вводные данные:

# events = [
#     {"user_id": 1, "action": "login", "timestamp": 11},
#     {"user_id": 2, "action": "logout", "timestamp": 13},
#     {"user_id": 1, "action": "view", "timestamp": 12},
#     {"user_id": 2, "action": "login", "timestamp": 10},
#     {"user_id": 1, "action": "click", "timestamp": 14},
# ]
#
#
# def sorted_user_events(data: list):
#     result = {}
#
#     data.sort(key=lambda event: event['timestamp'])
#
#     for event in data:
#         if event['user_id'] not in result:
#             result[event['user_id']] = [event['action']]
#         else:
#             result[event['user_id']].append(event['action'])
#
#     return result
#
#
# print(sorted_user_events(events))


# Задача 4. Выявить "лояльных" пользователей
# Задача:
# Есть список заказов. У каждого заказа — user_id, amount.
# Считаем "лояльным" пользователя, если он сделал 3+ заказа и суммарно потратил более 300.

# 👉 Верни список user_id лояльных пользователей.

# orders = [
#     {"user_id": 1, "amount": 120},
#     {"user_id": 2, "amount": 80},
#     {"user_id": 1, "amount": 100},
#     {"user_id": 1, "amount": 100},
#     {"user_id": 2, "amount": 130},
#     {"user_id": 3, "amount": 90},
#     {"user_id": 3, "amount": 110},
#     {"user_id": 3, "amount": 105},
# ]
#
# def get_loyal(data: list):
#     user_stats = {}
#
#     for order in data:
#         if order['user_id'] not in user_stats:
#             user_stats[order['user_id']] = {'order_num': 1, 'total_spent': order['amount']}
#         else:
#             user_stats[order['user_id']]['order_num'] += 1
#             user_stats[order['user_id']]['total_spent'] += order['amount']
#
#     loyal_id = []
#
#     for user in user_stats:
#         if user_stats[user].get('order_num') >= 3 and user_stats[user].get('total_spent') >= 300:
#             loyal_id.append(user)
#
#     return loyal_id
#
#
# print(get_loyal(orders))


# Найти всех пользователей, которые:
#
# Совершили как минимум одно действие из каждой категории:
#
# view
#
# click
#
# purchase
#
# Совершили их в правильном порядке, то есть сначала хотя бы один view, потом click, потом purchase.
# (Не обязательно подряд, но в этом порядке.)

# events = [
#     {"user_id": 1, "action": "view"},
#     {"user_id": 1, "action": "click"},
#     {"user_id": 1, "action": "purchase"},
#
#     {"user_id": 2, "action": "click"},
#     {"user_id": 2, "action": "purchase"},
#     {"user_id": 2, "action": "view"},
#
#     {"user_id": 3, "action": "view"},
#     {"user_id": 3, "action": "purchase"},
#
#     {"user_id": 4, "action": "view"},
#     {"user_id": 4, "action": "click"},
#     {"user_id": 4, "action": "view"},
#     {"user_id": 4, "action": "click"},
#     {"user_id": 4, "action": "purchase"},
# ]
#
# def get_involved(data: list):
#     user_actions = {}
#
#     for event in data:
#         if event['user_id'] not in user_actions:
#             user_actions[event['user_id']] = [event['action']]
#         else:
#             user_actions[event['user_id']].append(event['action'])
#
#     involved_users = []
#
#     for user, action in user_actions.items():
#         if "view" in action and "click" in action and "purchase" in action and action.index("view") < action.index("click") < action.index("purchase"):
#             involved_users.append(user)
#
#     return involved_users
#
#
# print(get_involved(events))


# Задача 1. Товары и заказы (сложение по ключу)
# У тебя есть два списка:
#
# products — справочник товаров с их ценами;
#
# orders — список заказов, где каждый заказ содержит product_id и quantity.
#
# Нужно посчитать общую выручку по каждому товару и отсортировать результат по убыванию выручки.


# products = [
#     {"product_id": 1, "name": "Laptop", "price": 1200},
#     {"product_id": 2, "name": "Mouse", "price": 25},
#     {"product_id": 3, "name": "Keyboard", "price": 75},
#     {"product_id": 4, "name": "Monitor", "price": 300},
# ]
#
# orders = [
#     {"product_id": 1, "quantity": 2},
#     {"product_id": 2, "quantity": 10},
#     {"product_id": 1, "quantity": 1},
#     {"product_id": 3, "quantity": 4},
#     {"product_id": 4, "quantity": 2},
#     {"product_id": 2, "quantity": 5},
# ]
#
# def get_stats(products: list, orders: list):
#     result = {}
#
#     item_id_quantity = {}
#
#     for order in orders:
#         item_id_quantity[order['product_id']] = item_id_quantity.get(order['product_id'], 0) + order['quantity']
#
#     for product in products:
#         result[product['name']] = item_id_quantity[product['product_id']] * product['price']
#
#     output = []
#
#     for item, total in result.items():
#         output.append((item, total))
#
#     output.sort(key=lambda couple: couple[1], reverse=True)
#
#     return output
#
#
# print(get_stats(products, orders))


# Задача 2. Пользователи и активности
# Дан список событий пользователей. Нужно:
#
# сгруппировать события по пользователям;
#
# посчитать, сколько раз каждый пользователь выполнил каждое уникальное действие;
#
# результат — словарь, где ключ — user_id, а значение — словарь с действиями и их количеством.

# events = [
#     {"user_id": 1, "action": "login"},
#     {"user_id": 2, "action": "login"},
#     {"user_id": 1, "action": "view"},
#     {"user_id": 1, "action": "click"},
#     {"user_id": 2, "action": "view"},
#     {"user_id": 1, "action": "view"},
#     {"user_id": 2, "action": "click"},
#     {"user_id": 1, "action": "logout"},
#     {"user_id": 2, "action": "logout"},
# ]

# user_events = {
#     1: {'login': 1, 'view': 2, 'click': 1, 'logout': 1},
#     2: {'login': 1, 'view': 1, 'click': 1, 'logout': 1}
# }


# Задача 2. Уникальные элементы
# Условие:
# Дан список. Верни новый список, содержащий только уникальные значения (встречаются один раз).

# items = [1, 2, 2, 3, 4, 4, 5]
#
# def get_uniq(data: list):
#     return list(filter(lambda element: data.count(element) == 1, data))
#
#
# print(get_uniq(items))

# Задача 3. Поиск самого длинного слова
#
# words = ['apple', 'banana', 'pear', 'watermelon']
#
# def get_longest(data: list):
#     return max(data, key=len)
#
#
# print(get_longest(words))

# Задача 4. Фильтр по длине строки
# Условие:
# Верни все строки длиной не меньше 5 символов.

# lines = ['hi', 'hello', 'yes', 'world', 'no', 'python']
#
# def get_5_syms(data: list):
#     return list(filter(lambda word: len(word) >= 5, data))
#
#
# print(get_5_syms(lines))


# Задача 1. Самый активный пользователь
# Условие:
# Дан список событий, каждое из которых содержит user_id. Найди пользователя с наибольшим количеством событий.

# events = [
#     {'user_id': 1, 'action': 'login'},
#     {'user_id': 2, 'action': 'click'},
#     {'user_id': 1, 'action': 'purchase'},
#     {'user_id': 3, 'action': 'logout'},
#     {'user_id': 2, 'action': 'view'},
#     {'user_id': 1, 'action': 'logout'},
#     {'user_id': 2, 'action': 'click'}
# ]
#
#
# def get_max_acts_user(data: list):
#     res = {}
#
#     for event in data:
#         if event['user_id'] not in res:
#             res[event['user_id']] = [event['action']]
#         else:
#             if event['action'] not in res[event['user_id']]:
#                 res[event['user_id']].append(event['action'])
#
#     max_acts = max(res.values(), key=len)
#
#     for user, evs in res.items():
#         if evs == max_acts:
#             return user
#
#
# print(get_max_acts_user(events))


# Задача 2. Отфильтровать товары по выручке
# Условие:
# Дан список словарей с product_name и revenue. Верни отсортированный по убыванию выручки список названий товаров, где выручка больше 100.

# products = [
#     {"product_name": "A", "revenue": 150},
#     {"product_name": "B", "revenue": 90},
#     {"product_name": "C", "revenue": 200},
#     {"product_name": "D", "revenue": 50}
# ]
#
# def get_100_plus(data: list):
#     res_products = sorted(list(filter(lambda product: product['revenue'] > 100, data)), key=lambda  product: product['revenue'], reverse=True)
#
#     output = []
#
#     for product in res_products:
#         output.append(product['product_name'])
#
#     return output
#
#
# print(get_100_plus(products))


# Задача 3. Список покупателей с общей суммой покупок
# Условие:
# Дан список заказов. Посчитай общую сумму покупок для каждого пользователя и верни словарь {user_id: total}.

# orders = [
#     {'user_id': 1, 'amount': 100},
#     {'user_id': 2, 'amount': 200},
#     {'user_id': 1, 'amount': 50},
#     {'user_id': 3, 'amount': 70},
#     {'user_id': 2, 'amount': 100}
# ]
#
#
# def get_stats(data: list):
#     result = {}
#
#     for order in data:
#         result[order['user_id']] = result.get(order['user_id'], 0) + order['amount']
#
#     return result
#
#
# print(get_stats(orders))


# Задача 4. Пользователи, совершившие хотя бы один заказ дороже 100
# Условие:
# Из списка заказов найти всех user_id, у которых есть хотя бы один заказ с amount > 100.

# orders = [
#     {'user_id': 1, 'amount': 90},
#     {'user_id': 2, 'amount': 120},
#     {'user_id': 3, 'amount': 70},
#     {'user_id': 1, 'amount': 110},
#     {'user_id': 2, 'amount': 80}
# ]
#
#
# def get_premium(data: list):
#     result = []
#
#     for order in data:
#         if order['amount'] > 100:
#             if order['user_id'] not in result:
#                 result.append(order['user_id'])
#
#     return result
#
#
# print(get_premium(orders))


# Задача 1. Подсчёт количества товаров по категориям
# Условие:
# Дан список словарей, где каждый элемент содержит product_name и category.
# Нужно вернуть словарь, где ключ — это название категории, а значение — количество товаров в этой категории.


# products = [
#     {"product_name": "Laptop", "category": "Electronics"},
#     {"product_name": "Shampoo", "category": "Beauty"},
#     {"product_name": "TV", "category": "Electronics"},
#     {"product_name": "Foundation", "category": "Beauty"},
#     {"product_name": "Headphones", "category": "Electronics"}
# ]
#
#
# def get_stats(data: list):
#     result = {}
#
#     for product in data:
#         result[product['category']] = result.get(product['category'],0) + 1
#
#     return result
#
#
# print(get_stats(products))


# Задача 2. Сумма выручки по товару (с использованием .get)
# Условие:
# Дан список заказов с полями product_name и amount.
# Нужно вернуть словарь, где ключ — название товара, а значение — сумма выручки по нему.

# orders = [
#     {"product_name": "A", "amount": 100},
#     {"product_name": "B", "amount": 200},
#     {"product_name": "A", "amount": 150},
#     {"product_name": "C", "amount": 50},
#     {"product_name": "B", "amount": 100}
# ]
#
#
# def get_revenue(data: list):
#     result = {}
#
#     for item in data:
#         result[item['product_name']] = result.get(item['product_name'], 0) + item['amount']
#
#     return result
#
#
# print(get_revenue(orders))


# Задача 1: Наиболее активные пользователи
# Условие:
# Дан список действий пользователей, где каждое действие — словарь с user_id. Верни список user_id, у которых максимальное количество действий.

# events = [
#     {'user_id': 1}, {'user_id': 2}, {'user_id': 1},
#     {'user_id': 3}, {'user_id': 2}, {'user_id': 2}
# ]
#
# def get_most_active(data: list):
#     all_act = {}
#
#     for act in data:
#         all_act[act['user_id']] = all_act.get(act['user_id'], 0) + 1
#
#     return max(list(all_act.items()), key=lambda pair: pair[1])[0]
#
#
# print(get_most_active(events))


# Задача 2: Префиксы имен
# Условие:
# Дан список имён. Нужно создать словарь, где ключ — первая буква имени, а значение — список всех имён, начинающихся на эту букву.

# names = ["Alice", "Arnold", "Bob", "Ben", "Cindy"]
#
# def get_common(data: list):
#     output = {}
#
#     for name in data:
#         if name[0] not in output:
#             output[name[0]] = [name]
#         else:
#             output[name[0]].append(name)
#
#     return output
#
#
# print(get_common(names))


# Задача 3: Самый дорогой товар в категории
# Условие:
# Дан список заказов с product_name, category, price. Верни для каждой категории название самого дорогого товара.

# products = [
#     {"product_name": "Laptop", "category": "Electronics", "price": 1000},
#     {"product_name": "TV", "category": "Electronics", "price": 2000},
#     {"product_name": "Foundation", "category": "Beauty", "price": 300},
#     {"product_name": "Shampoo", "category": "Beauty", "price": 150}
# ]
#
# def get_most_expensive(data: list):
#     output = {}
#
#     final = {}
#
#     for item_info in data:
#         output[item_info['category']] = 0
#
#     for category in output:
#         for item_info in data:
#             if category == item_info['category']:
#                 if item_info['price'] > output[category]:
#                     output[category] = item_info['price']
#                     final[category] = item_info['product_name']
#
#     return final
#
#
# print(get_most_expensive(products))


# Задача 4: Проверка уникальности по ключу
# Условие:
# Дан список словарей с id и name. Верни True, если все id уникальны, иначе False.

# users = [
#     {"id": 1, "name": "Alice"},
#     {"id": 2, "name": "Bob"},
#     {"id": 1, "name": "Charlie"}
# ]
#
#
# def check_if_all_unique(data: list):
#     checked_ids = []
#
#     for user in data:
#         checked_ids.append(user['id'])
#
#     if tuple(checked_ids) == tuple(set(checked_ids)):
#         return True
#
#     return False
#
#
# print(check_if_all_unique(users))


# Задача 5: Общая сумма по категориям
# Условие:
# Для каждого заказа у тебя есть category и amount. Верни словарь с суммой по категориям.


# orders = [
#     {"category": "Books", "amount": 200},
#     {"category": "Books", "amount": 100},
#     {"category": "Tech", "amount": 150}
# ]
#
#
# def get_sum_cat(data: list):
#     res = {}
#
#     for order in data:
#         res[order['category']] = res.get(order['category'], 0) + order['amount']
#
#     return res
#
#
# print(get_sum_cat(orders))


# Задача 1: Самый прибыльный товар в каждой категории
# Условие:
# Дан список заказов. Каждый заказ — словарь с product, category, amount. Один и тот же товар может появляться в списке несколько раз.
# Верни словарь, где ключ — категория, а значение — название самого прибыльного товара (по суммарному amount за все появления).


# orders = [
#     {"product": "Laptop", "category": "Electronics", "amount": 1000},
#     {"product": "TV", "category": "Electronics", "amount": 1500},
#     {"product": "Laptop", "category": "Electronics", "amount": 800},
#     {"product": "Phone", "category": "Electronics", "amount": 1200},
#     {"product": "Shampoo", "category": "Beauty", "amount": 100},
#     {"product": "Foundation", "category": "Beauty", "amount": 200},
#     {"product": "Shampoo", "category": "Beauty", "amount": 150},
#     {"product": "Notebook", "category": "Stationery", "amount": 50},
#     {"product": "Notebook", "category": "Stationery", "amount": 70},
#     {"product": "Pen", "category": "Stationery", "amount": 20}
# ]
# print(max(order['amount'] for order in orders))
# x = sum(order['amount'] for order in orders)
#
# print(x)

# def get_best_in_category(data: list):
#     result = {}
#
#     merged_amount = []
#
#     checked_products = []
#
#     categories = []
#
#     for order in data:
#         if order['product'] not in checked_products:
#             checked_products.append(order['product'])
#
#             total_amount = sum(
#                 ord['amount'] for ord in data
#                 if ord['product'] == order['product']
#             )
#
#             merged_amount.append({
#                 "product": order['product'],
#                 "category": order['category'],
#                 "amount": total_amount
#             })
#
#         if order['category'] not in categories:
#             categories.append(order['category'])
#
#     for category in categories:
#         category_max = max(merg['amount'] for merg in (list(filter(lambda merged: merged['category'] == category, merged_amount))))
#         for m in merged_amount:
#             if m['amount'] == category_max:
#                 result[category] = m['product']
#
#     return result
#
#
# print(get_best_in_category(orders))


# 🔹 Задача 2: Сортировка пользователей по количеству и сумме покупок
# Условие:
# Есть список заказов с user_id и amount. Нужно вернуть отсортированный список кортежей (user_id, total_orders, total_spent) по убыванию:
#
# сначала по количеству заказов,
#
# если одинаково — по сумме покупок.


# orders = [
#     {"user_id": 1, "amount": 100},
#     {"user_id": 2, "amount": 200},
#     {"user_id": 1, "amount": 300},
#     {"user_id": 3, "amount": 100},
#     {"user_id": 2, "amount": 150},
#     {"user_id": 3, "amount": 100},
#     {"user_id": 1, "amount": 50},
#     {"user_id": 2, "amount": 300}
# ]
#
# def sort_users(data: list):
#     total_amount_orders = {}
#
#     for user in data:
#         if user['user_id'] not in total_amount_orders:
#             total_amount_orders[user['user_id']] = {'orders number': 1, 'total amount': user['amount']}
#         else:
#             total_amount_orders[user['user_id']]['orders number'] += 1
#             total_amount_orders[user['user_id']]['total amount'] += user['amount']
#
#     total_amount = []
#
#     for user, info in total_amount_orders.items():
#         total_amount.append((user, info))
#
#     total_amount.sort(key=lambda user_info: user_info[1]['orders number'],  reverse=True)
#     total_amount.sort(key=lambda user_info: user_info[1]['total amount'], reverse=True)

        ##             лучше так: total_amount.sort(
        ##     key=lambda user_info: (user_info[1]['orders number'], user_info[1]['total amount']),
        ##     reverse=True
        ## )

#
#     return total_amount
#
#
# print(sort_users(orders))


# Задача 3: Пользователь с максимальной средней покупкой
# Условие:
# Тот же список заказов. Найди user_id, у которого средний размер одной покупки максимальный.


# orders = [
#     {"user_id": 1, "amount": 100},
#     {"user_id": 2, "amount": 250},
#     {"user_id": 1, "amount": 100},
#     {"user_id": 2, "amount": 150},
#     {"user_id": 3, "amount": 500},
#     {"user_id": 3, "amount": 100}
# ]
#
# def get_best_avg_user(data: list):
#     avg_spent = {}
#
#     max_avg_user = 0
#
#     for order in data:
#         if order['user_id'] not in avg_spent:
#             avg_spent[order['user_id']] = [order['amount']]
#         else:
#             avg_spent[order['user_id']].append(order['amount'])
#
#     for user in avg_spent:
#         if max_avg_user < sum(avg_spent[user]) / len(avg_spent[user]):
#             max_avg_user = sum(avg_spent[user]) / len(avg_spent[user])
#             output = user
#
#     return output
#
#
# print(get_best_avg_user(orders))


#  Задача 4: Группировка по первой букве категории и сортировка по количеству товаров
# Условие:
# Список товаров с name и category. Сгруппируй по первой букве категории, посчитай количество товаров в каждой группе, отсортируй группы по убыванию количества.


# products = [
#     {"name": "Laptop", "category": "Electronics"},
#     {"name": "TV", "category": "Electronics"},
#     {"name": "Shampoo", "category": "Beauty"},
#     {"name": "Foundation", "category": "Beauty"},
#     {"name": "Notebook", "category": "Stationery"},
#     {"name": "Pen", "category": "Stationery"},
#     {"name": "Eraser", "category": "Stationery"},
#     {"name": "Sunscreen", "category": "Beauty"},
#     {"name": "Speaker", "category": "Electronics"}
# ]
#
#
# def sort_by_first_char(data: list):
#     categorized = {}
#
#     for product in data:
#         categorized[product['category'][0]] = categorized.get(product['category'][0], 0) + 1
#
#     return categorized
#
#
# print(sort_by_first_char(products))


# Задача 1: Проверка соблюдения лимитов
# Условие:
# Есть список транзакций и лимиты по категориям. Каждая транзакция — это {"user_id": int, "category": str, "amount": int}.
# Верни список user_id, которые превысили хотя бы один лимит.


# transactions = [
#     {"user_id": 1, "category": "Food", "amount": 300},
#     {"user_id": 1, "category": "Food", "amount": 250},
#     {"user_id": 2, "category": "Books", "amount": 400},
#     {"user_id": 1, "category": "Books", "amount": 150},
#     {"user_id": 2, "category": "Food", "amount": 100},
#     {"user_id": 3, "category": "Food", "amount": 600},
#     {"user_id": 3, "category": "Books", "amount": 300},
# ]
#
# limits = {
#     "Food": 500,
#     "Books": 300
# }
#
#
# def check_limits(data: list, lims: dict):
#     output = []
#
#     for order in data:
#         for category in lims:
#             if order['category'] == category and order['amount'] > lims[category]:
#                 output.append(order['user_id'])
#
#     return list(set(output))
#
#
# print(check_limits(transactions, limits))


# Задача 2: Кто купил все
# Условие:
# Есть список покупок. Нужно вернуть user_id, которые сделали хотя бы по одной покупке в каждой категории.


# orders = [
#     {"user_id": 1, "category": "Tech"},
#     {"user_id": 1, "category": "Books"},
#     {"user_id": 2, "category": "Books"},
#     {"user_id": 3, "category": "Tech"},
#     {"user_id": 2, "category": "Tech"},
#     {"user_id": 3, "category": "Books"},
#     {"user_id": 3, "category": "Beauty"},
#     {"user_id": 1, "category": "Beauty"},
#     {"user_id": 2, "category": "Beauty"}
# ]
#
# def who_bought_all(data: list):
#     categories = []
#     user_categories = {}
#     output = []
#
#     for order in data:
#         if order['category'] not in categories:
#             categories.append(order['category'])
#
#     for order in data:
#         if order['user_id'] not in user_categories:
#             user_categories[order['user_id']] = [order['category']]
#         else:
#             user_categories[order['user_id']].append(order['category'])
#
#     for user_info in user_categories:
#         if set(user_categories[user_info]) == set(categories):
#             output.append(user_info)
#
#     return output
#
#
# print(who_bought_all(orders))


# 🔹 Задача 3: Верификация структуры
# Условие:
# Проверить, что в каждом элементе списка data есть ключи "id", "name", "category" и "amount".
# Верни True, если все записи валидны, иначе False.

# data = [
#     {"id": 1, "name": "Item1", "category": "A", "amount": 100},
#     {"id": 2, "name": "Item2", "category": "B", "amount": 150},
#     {"id": 3, "name": "Item3", "amount": 120},  # <--- отсутствует category
# ]
#
# def check_keys(datei: list):
#     keys = ["id", "name", "category", "amount"]
#
#     for element in datei:
#         if len(element.keys()) != len(keys):
#             return False
#
#     return True
#
#
# print(check_keys(data))


# 🔹 Задача 4: Группировка по ключу с фильтрацией
# Условие:
# Группируй товары по категории и оставь только те, где сумма по этой категории больше 200.


# items = [
#     {"name": "Item1", "category": "A", "amount": 100},
#     {"name": "Item2", "category": "A", "amount": 120},
#     {"name": "Item3", "category": "B", "amount": 50},
#     {"name": "Item4", "category": "B", "amount": 30},
#     {"name": "Item5", "category": "C", "amount": 300},
# ]
#
#
# def group_items(data: list):
#     items_total = {}
#
#     for item in data:
#         items_total[item['category']] = items_total.get(item['category'], 0) + item['amount']
#
#     return list(filter(lambda category: items_total[category] > 200, items_total))
#
#
# print(group_items(items))


# 🔹 Задача: "Анализ покупок по подписке"
# У тебя есть список пользователей и список заказов. Нужно определить:
#
# кто из пользователей имеет активную подписку ("subscription": True),
#
# и в рамках подписки потратил более 500 у.е. за последние 30 дней (относительно текущей даты).
#
# Нужно вернуть список словарей с полями:
#
# {
#     "user_id": int,
#     "total_spent": float,
#     "orders": [список id заказов]
# }


# from datetime import datetime, timedelta
#
# users = [
#     {"user_id": 1, "subscription": True},
#     {"user_id": 2, "subscription": False},
#     {"user_id": 3, "subscription": True},
#     {"user_id": 4, "subscription": True},
# ]
#
# orders = [
#     {"order_id": 101, "user_id": 1, "amount": 150, "date": "2025-07-10"},
#     {"order_id": 102, "user_id": 1, "amount": 200, "date": "2025-07-15"},
#     {"order_id": 103, "user_id": 1, "amount": 300, "date": "2025-06-10"},  # старый
#     {"order_id": 104, "user_id": 2, "amount": 600, "date": "2025-07-18"},
#     {"order_id": 105, "user_id": 3, "amount": 250, "date": "2025-07-01"},
#     {"order_id": 106, "user_id": 3, "amount": 300, "date": "2025-07-20"},
#     {"order_id": 107, "user_id": 4, "amount": 100, "date": "2025-07-05"},
# ]
#
#
# def get_active_30_days_500_plus(users_list: list, orders_list: list):
#     result = []
#
#     active_users = list(filter(lambda user: user['subscription'], users_list))
#
#     actives = []
#
#     for us in active_users:
#         actives.append(us['user_id'])
#
#     last_30_days_orders_actives = list(filter(lambda order: ((datetime.today()) - (datetime.fromisoformat(order['date']))).days <= 30 and order['user_id'] in actives, orders_list))
#
#     for active_user in actives:
#         active_user_info = {
#             "user_id": 0,
#             "total_spent": 0,
#             "orders": []
#         }
#
#         active_user_info['user_id'] = active_user
#
#         for order in last_30_days_orders_actives:
#             if order['user_id'] == active_user_info['user_id']:
#                 active_user_info["total_spent"] += order['amount']
#                 active_user_info["orders"].append(order['order_id'])
#
#         result.append(active_user_info)
#
#     return list(filter(lambda user_info: user_info['total_spent'] > 500, result))
#
#
# print(get_active_30_days_500_plus(users, orders))


# Задача 1: Отфильтровать заказы на сумму больше 200
# Условие:
# Дан список заказов. Оставь только те, где amount больше 200. Используй filter и lambda.


# orders = [
#     {"order_id": 101, "amount": 150},
#     {"order_id": 102, "amount": 300},
#     {"order_id": 103, "amount": 250},
#     {"order_id": 104, "amount": 100},
# ]
#
#
# def filter_200_more(data: list):
#     return list(filter(lambda order: order['amount'] > 200, data))
#
#
# print(filter_200_more(orders))


# 🔹 Задача 2: Сортировать пользователей по имени (в обратном порядке)
# Условие:
# Есть список пользователей с именами. Отсортируй их по имени в обратном алфавитном порядке.
#
#
# users = [
#     {"user_id": 1, "name": "Anna"},
#     {"user_id": 2, "name": "Zoe"},
#     {"user_id": 3, "name": "Mike"},
# ]
#
#
# def sort_by_name_reverse(data: list):
#     return sorted(data, key=lambda user: user['name'], reverse=True)
#
#
# print(sort_by_name_reverse(users))


# 🔹 Задача 3: Найти пользователя с максимальным количеством баллов
# Условие:
# Найди пользователя с максимальным score с помощью max() и key=lambda.


# users = [
#     {"user_id": 1, "score": 75},
#     {"user_id": 2, "score": 88},
#     {"user_id": 3, "score": 64},
# ]
#
#
# def get_max(data: list):
#     return tuple(max(data, key=lambda user: user['score']).values())[0]
#
# print(get_max(users))


# Задача 4
# Дан список словарей с пользователями и датами регистрации. Верни список пользователей, зарегистрировавшихся в последние 7 дней (считай от текущей даты).


# users = [
#     {"user_id": 1, "registered": "2025-07-20"},
#     {"user_id": 2, "registered": "2025-07-15"},
#     {"user_id": 3, "registered": "2025-07-10"},
#     {"user_id": 4, "registered": "2025-06-30"},
# ]
#
# def sort_date(data: list):
#     from datetime import datetime
#
#     today = datetime.today()
#
#     return list(filter(lambda user: (today - datetime.fromisoformat(user['registered'])).days <= 7, data))
#
#
# print(sort_date(users))


# Задача 5
# Дан список заказов. Для каждого пользователя посчитай общую сумму заказов и верни словарь вида {user_id: total_amount}.


# orders = [
#     {"order_id": 101, "user_id": 1, "amount": 150},
#     {"order_id": 102, "user_id": 1, "amount": 200},
#     {"order_id": 103, "user_id": 2, "amount": 300},
#     {"order_id": 104, "user_id": 3, "amount": 100},
# ]
#
#
# def user_total(data: list):
#     result = {}
#
#     for order in data:
#         result[order['user_id']] = result.get(order['user_id'], 0) + order['amount']
#
#     return result
#
#
# print(user_total(orders))


# Задача 6
# Дан список товаров с категориями и ценами. Верни топ-2 категории по суммарной цене товаров.


# products = [
#     {"product": "A", "category": "X", "price": 100},
#     {"product": "B", "category": "Y", "price": 200},
#     {"product": "C", "category": "X", "price": 300},
#     {"product": "D", "category": "Z", "price": 150},
#     {"product": "E", "category": "Y", "price": 50},
# ]
#
#
# def get_most_exp(data: list):
#     top_categories = {}
#
#     for product in data:
#         top_categories[product['category']] = top_categories.get(product['category'], 0) + product['price']
#
#     return sorted(list(top_categories.items()), key=lambda couple: couple[1], reverse=True)[:2]
#
#
# print(get_most_exp(products))

# with open("text.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)


# Твоя задача на практике:
# Напиши генератор, который возвращает все чётные числа от 2 до 20.
#
# Напиши генератор, который будет выдавать по одному слову из строки текста.
#
# Создай генератор, который выдаёт бесконечную последовательность квадратов чисел (1, 4, 9, 16, ...).

# 1)
# def all_even_till20():
#     for num in range(21):
#         if num % 2 == 0:
#             yield num
#
#
# for even_num in all_even_till20():
#     print(even_num)


# 2)
# def get_words_sep(data: str):
#     from string import punctuation
#
#     for char in string.punctuation:
#         data = data.replace(char, '')
#
#     for word in data.split():
#         yield word
#
#
# for element in get_words_sep('Напиши генератор, который будет выдавать по одному слову из строки текста.'):
#     print(element)


# 3)
# def get_power2_eternal():
#     counter = 0
#
#     while True:
#         counter += 1
#         yield counter**2
#
#
# for number in get_power2_eternal():
#     print(number)


# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("Деление на ноль!")
# finally:
#     print("Этот блок выполнится всегда")


# 1. Чтение файла с обработкой ошибок
# Напиши функцию, которая принимает имя файла, пытается открыть его и вывести содержимое.
#
# Добавь обработку исключения, если файл не найден — выводи понятное сообщение.
#
# Проверь на реальном файле и на несуществующем.


# def open_file_or_reject(file_name: str):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print('File was not identified in this directory')
#
#
# open_file_or_reject('text.txt')


# 2. Подсчёт слов в файле
# Создай текстовый файл с любым небольшим текстом (5–10 строк).
#
# Напиши функцию, которая читает файл и считает общее количество слов.
#
# Выведи результат.


# def count_words(file_name: str):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#             all_words_sep = content.split()
#
#             print(f'Всего слов в тексте: {len(all_words_sep)}')
#
#     except FileNotFoundError:
#         print('File was not identified in this directory')
#
#
# count_words('text.txt')


# 3. Запись отфильтрованных слов в новый файл
# Используя функцию из задачи 2, отфильтруй слова длиной больше 3 символов.
#
# Запиши эти слова в новый файл (каждое слово на новой строке).
#
# Используй контекстный менеджер (with) для работы с файлами.

# def filter_3_chars_or_more_words(file_name: str):
#     try:
#         from string import punctuation
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#             for char in string.punctuation:
#                 content = content.replace(char, '')
#
#             all_words_sep = content.split()
#
#             three_chars_or_more_words = list(filter(lambda elem: len(elem) >= 3, all_words_sep))
#
#             with open('output.txt', 'w', encoding='utf-8') as output_file:
#                 for word in three_chars_or_more_words:
#                     output_file.write(word + '\n')
#
#     except FileNotFoundError:
#         print('File was not identified in this directory')
#
#
# filter_3_chars_or_more_words('text.txt')


# 4. Генератор для слов из файла
# Напиши генератор, который построчно читает файл и отдаёт по одному слову.
#
# Используй этот генератор в цикле for и выведи все слова.

# def read_and_print_file(file_name: str):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         content = file.read()
#
#         for element in content.split():
#             yield element
#
#
# for word in read_and_print_file('output.txt'):
#     print(word)


# Задание 1.
# Прочитай текстовый файл. Подсчитай, сколько раз встречается каждое слово (без учёта регистра и знаков препинания).
# Затем запиши в новый файл все слова и их количество, отсортировав их по убыванию частоты встречаемости.

# def last_char_punct(word: str):
#     from string import punctuation
#
#     if word[-1] in tuple(string.punctuation):
#         word = word[:-1]
#
#     return word
#
#
# def count_words(file_name: str):
#     try:
#         from string import punctuation
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = file.read().lower()
#
#             all_words = content.split()
#
#             all_words = list(map(lambda word: last_char_punct(word), all_words))
#
#         result = {}
#
#         for word in all_words:
#             result[word] = result.get(word, 0) + 1
#
#         result_items = []
#
#         for item in result.items():
#             result_items.append(item)
#
#         result_items.sort(key=lambda tpl: tpl[1], reverse=True)
#
#         return result_items
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# def save_new_file(file_name: str):
#     with open('output.txt', 'w', encoding='utf-8') as file:
#         for item in count_words(file_name):
#             file.write(str(item) + '\n')
#
# save_new_file('text.txt')


#  Задание 1: Частотный анализ с фильтрацией
# У тебя есть текстовый файл log.txt, содержащий по одной строке в каждом сообщении (например, лог чата или комментарии).
# Твоя задача:
#
# Считать файл построчно.
#
# Посчитать, сколько раз встречается каждое слово.
#
# Отфильтровать все слова короче 4 символов.
#
# Записать результат в новый файл filtered_freq.txt в формате:
#
# слово — количество


# def filter_freq(file_name: str):
#     try:
#         from string import punctuation
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#             for char in string.punctuation:
#                 content = content.replace(char, '')
#
#             content_lines = content.splitlines()
#
#             print(content_lines)
#
#             output = {}
#
#             for line in content_lines:
#                 for word in line.split():
#                     output[word] = output.get(word.lower(), 0) + 1 # тут я не придумал, как оставить имена с большой буквы (чтобы они в словаре были с большой, а все остальные с маленькой)
#
#         with open('filtered_freq.txt', 'w', encoding='utf-8') as file:
#             file.write(str(output))
#
#             return output
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#         return None
#
#
# print(filter_freq('log.txt'))


# 🔹 Задание 2: Фильтрация пользователей по активности
# Есть файл messages.txt, в котором каждая строка имеет формат:
#
# Имя: сообщение
# Твоя задача:
#
# Посчитать, сколько сообщений написал каждый пользователь.
#
# Записать результат в файл active_users.txt в формате:
#
# Имя — количество сообщений
#
# Отсортировать результат по алфавиту имени.


# def filter_active_users(file_name: str, verbose=False):
#     try:
#         from string import punctuation
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#             content_lines = content.splitlines()
#
#             users = set()
#
#             result = {}
#
#             for char in content_lines:
#                 users.add(char[:char.index(':')])
#
#             users = tuple(users)
#
#             for line in content_lines:
#                 for user in users:
#                     if line.startswith(user):
#                         result[user] = result.get(user, 0) + 1
#
#             output = []
#
#             for name, messes in result.items():
#                 output.append((name, messes))
#
#             output.sort(key=lambda items: items[0])
#
#             with open('active_users.txt', 'w', encoding='utf-8') as file:
#                 for items in output:
#                     file.write(f'{items[0]}: {items[1]}\n')
#
#             if verbose:
#                 print(output)
#
#             return output
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#         return None
#
#
# filter_active_users('messages.txt', verbose=False)


# CSV - comma-separated values

# ✅ Задание 1: Подсчитать выручку по каждому продавцу
# Требуется:
#
# Прочитать файл.
#
# Для каждой строки вычислить Количество * Цена.
#
# Сложить выручку по каждому продавцу.
#
# Записать результат в файл revenue_by_seller.csv в формате:

# Продавец,Выручка
# Анна,1150
# Иван,3250
# Олег,750

# def get_revenue_by_seller(file_name: str):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content_lines = file.read().splitlines()[1:]
#
#             seller_revenue = {}
#
#             for order in content_lines:
#                 values = order.split(',')
#
#                 seller_revenue[values[0]] = seller_revenue.get(values[0], 0) + int(values[-2]) * int(values[-1])
#
#             with open('revenue_by_seller.csv', 'w', encoding='utf-8') as file:
#                 file.write('Продавец,Выручка\n')
#
#                 for seller, revenue in seller_revenue.items():
#                     file.write(f'{seller},{revenue}\n')
#
#             return seller_revenue
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#         return None
#
#
# print(get_revenue_by_seller('sales.csv'))


# z = '1 + 1'
#
# print(eval(z))

# Твоя задача:
# Прочитай файл orders.csv.
#
# Для каждого города вычисли:
#
# общее количество заказов (количество строк);
#
# общую сумму выручки (цена × количество).
#
# Запиши результат в файл city_stats.csv в формате:


# def get_city_stats_csv(file_name: str):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             file_content = file.read()
#
#             all_orders = []
#
#             for line in file_content.splitlines():
#                 all_orders.append(line.split(','))
#
#             all_orders.pop(0)
#
#             cities_stats = {}
#
#             for order in all_orders:
#                 if order[1] not in cities_stats:
#                     cities_stats[order[1]] = [1, eval(order[-2] + '*' + order[-1])]
#                 else:
#                     cities_stats[order[1]][0] += 1
#                     cities_stats[order[1]][1] += eval(order[-2] + '*' + order[-1])
#
#             with open('city_stats.csv', 'w', encoding='utf-8') as output_file:
#                 output_file.write('City,total orders,total revenue\n')
#
#                 for city, orders_total in cities_stats.items():
#                     output_file.write(f'{city},{orders_total[0]},{orders_total[1]}\n')
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# get_city_stats_csv('orders.csv')


# def get_items_stats(file_name: str):
#         try:
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#                 all_orders = []
#
#                 for line in content.splitlines():
#                     all_orders.append(line.split(','))
#
#                 all_orders.pop(0)
#
#                 items_stats = {}
#
#                 for order in all_orders:
#                     items_stats[order[1]] = items_stats.get(order[1], 0) + int(order[-2]) * int(order[-1])
#
#             with open('product_revenue.csv', 'w', encoding='utf-8') as output_file:
#                 output_file.write('Product,TotalRevenue\n')
#
#                 for item, revenue in items_stats.items():
#                     output_file.write(f'{item},{revenue}\n')
#
#         except Exception as err:
#             print(f'Error: {err}')
#
#
# get_items_stats('products.csv')


# def read_csv_to_dicts(file_name: str):
#     import csv
#
#     with open(file_name, 'r', encoding='utf-8') as file:
#         content = csv.reader(file)
#
#         header = next(content)
#
#         output = []
#
#         for user in content:
#             data = {}
#
#             for i in range(len(user)):
#                 data[header[i]] = user[i]
#
#             output.append(data)
#
#     return output
#
#
# read_csv_to_dicts('id_name_score.csv')


# def get_dict_from_csv(file_name: str):
#     import csv
#     with open(file_name, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#
#         return list(reader)
#
#
# print(get_dict_from_csv('users.csv'))

# users = [
#     ['Имя', 'Возраст', 'Город'],
#     ['Ольга', '30', 'Москва'],
#     ['Андрей', '25', 'Сочи'],
#     ['Светлана', '22', 'Казань']
# ]
#
# def get_users_file(data: list):
#     import csv
#
#     with open('users_output.csv', 'w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
#
#
# get_users_file(users)


# books = [
#     {'Название': '1984', 'Автор': 'Джордж Оруэлл', 'Год': '1949'},
#     {'Название': 'Мастер и Маргарита', 'Автор': 'Михаил Булгаков', 'Год': '1967'},
#     {'Название': 'Преступление и наказание', 'Автор': 'Фёдор Достоевский', 'Год': '1866'},
# ]
#
#
# def save_books_to_csv(data: list):
#     try:
#         import csv
#
#         with open('books.csv', 'w', encoding='utf-8', newline='') as file:
#             head = ['Название','Автор','Год']
#
#             writer = csv.DictWriter(file, fieldnames=head)
#
#             writer.writeheader()
#
#             writer.writerows(data)
#
#     except Exception as err:
#        print(f'Error: {err}')
#
#
# save_books_to_csv(books)


# def get_age30(file_name: str):
#     try:
#         import csv
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             reader_iterable = list(csv.reader(file))
#             reader_iterable.pop(0)
#
#         with open('adults.csv', 'w', encoding='utf-8', newline='') as output_file:
#             writer = csv.writer(output_file)
#
#             writer.writerow(['Имя','Возраст','Должность'])
#
#             writer.writerows(list(filter(lambda user: int(user[1]) >= 30, reader_iterable)))
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# get_age30('employees.csv')


# Задание 2: Подсчёт количества заказов по каждому товару
# Файл orders.csv содержит информацию о заказах.
#
# Твоя задача:
# Создать файл products_count.csv с двумя колонками:
# Товар, ОбщееКоличество — общее количество заказов по каждому товару.

# def get_products_count_csv(file_name: str):
#     try:
#         import csv
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = list(csv.reader(file))
#
#             content.pop(0)
#
#             output_data = {}
#
#             for order in content:
#                 output_data[order[1]] = output_data.get(order[1], 0) + int(order[-1])
#
#         with open('products_count.csv', 'w', encoding='utf-8', newline='') as output_file:
#             writer = csv.writer(output_file)
#
#             writer.writerow(['Товар','ОбщееКоличество'])
#
#             for item,count in output_data.items():
#                 writer.writerow([item,count])
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# get_products_count_csv('orders.csv')


# У тебя есть CSV-файл orders.csv с данными о заказах.
#
# Создать CSV-файл category_stats.csv, в котором будет:
#
# категория (из поля category),
#
# общее количество проданных единиц товаров этой категории,
#
# общая выручка по категории.

# def generate_category_report(file_name: str):
#     try:
#         import csv
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = list(csv.DictReader(file))
#
#             output_data = {}
#
#             for order in content:
#                 if order['category'] not in output_data:
#                     output_data[order['category']] = [int(order['quantity']), int(order['quantity']) * int(order['price'])]
#                 else:
#                     output_data[order['category']][0] += int(order['quantity'])
#                     output_data[order['category']][1] += int(order['quantity']) * int(order['price'])
#
#         with open('category_stats.csv', 'w', encoding='utf-8', newline='') as output_file:
#             header = ['Категория', 'ОбщееКоличество', 'ОбщаяВыручка']
#
#             writer = csv.DictWriter(output_file, fieldnames=header)
#
#             writer.writeheader()
#
#             for item in list(output_data.items()):
#                 writer.writerow({header[0]: item[0], header[1]: item[1][0], header[2]: item[1][1]})
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# generate_category_report('id,product,category,quantity,price.csv')


# def get_electronics(file_name: str):
#     try:
#         import csv
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = list(csv.DictReader(file))
#
#             only_electronics = list(filter(lambda item: item['Категория'] == "Электроника", content))
#
#             print(only_electronics)
#
#         with open('electronics.csv', 'w', newline='', encoding='utf-8') as output_file:
#             header = ['Название','Категория','Цена']
#
#             writer = csv.DictWriter(output_file, fieldnames=header)
#
#             writer.writeheader()
#
#             for item in only_electronics:
#                 writer.writerow(item)
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# get_electronics('products_task.csv')


# def get10_k_or_more(file_name: str, new_file_name: str):
#     try:
#         import csv
#
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = list(csv.DictReader(file))
#             filtered_items = list(filter(lambda item: int(item['Цена']) >= 10000, content))
#
#         with open(new_file_name, 'w', encoding='utf-8', newline='') as output_file:
#             header = ['Название','Категория','Цена']
#             writer_csv = csv.DictWriter(output_file, fieldnames=header)
#             writer_csv.writeheader()
#
#             for item in filtered_items:
#                 writer_csv.writerow({key: item[key] for key in header})
#
#     except Exception as err:
#         print(f"Error: {err}")
#
#
# get10_k_or_more('products_task.csv', 'expensive_products.csv')



##### JSON - JavaScript Object Notation #####



# Задача:
#
# У тебя есть файл data.json с таким содержимым (в точности, как JSON-массив объектов).
#
# Что нужно сделать:
#
# Открыть файл, считать его как обычный текст (строку).
#
# Найти количество товаров (количество объектов {...}).
#
# Найти вручную (без парсинга в словари) продукт с максимальной ценой (например, искать "price": и вытаскивать число).
#
# Записать в новый файл expensive.txt строки только с товарами, у которых цена > 500


# def str_to_dict(data: str):
#     if data.startswith('{') and data.endswith('}'):
#         open_par = data[0]
#         closing_par = data[-1]
#         data = data.replace(open_par, '').replace(closing_par, '').replace('"', '')
#
#         items = data.split(', ')
#
#         output = {}
#
#         for item in items:
#             item_split = item.split(': ')
#
#             output[item_split[0]] = item_split[1]
#
#         return output
#
#     else:
#         raise ValueError
#
#
# def get_expensive_json(file_name: str, new_file_name: str):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#             json_arrays = []
#
#             parentheses_opened = False
#
#             json_obj = ''
#
#             for char in content:
#                 if char == '{':
#                     parentheses_opened = True
#                     json_obj += char
#
#                 if parentheses_opened and char != '{':
#                     json_obj += char
#
#                 if char == '}':
#                     parentheses_opened = False
#                     json_arrays.append(json_obj)
#                     json_obj = ''
#
#             json_arrays = list(map(lambda item: str_to_dict(item), json_arrays))
#
#             biggest_price = 0
#
#             for item in json_arrays:
#                 if int(item['price']) > biggest_price:
#                     biggest_price = int(item['price'])
#                     most_expensive_item = item['product']
#
#             print(f'Самый дорогой продукт - {most_expensive_item}')
#
#             print(f'Количество товаров - {len(json_arrays)}')
#
#         expensive_items = list(filter(lambda item: int(item['price']) >= 500, json_arrays))
#
#         print(expensive_items)
#
#
#         with open(new_file_name, 'w', encoding='utf-8') as new_file:
#             for item in expensive_items:
#                 items_list = (list(item.items()))
#
#                 for i in range(len(items_list)):
#                     couple = items_list[i]
#
#                     if i != len(items_list) - 1:
#                         new_file.write(couple[0] + ': ' + couple[1] + ', ')
#                     else:
#                         new_file.write(couple[0] + ': ' + couple[1] + '\n')
#
#     except Exception as err:
#         print(f"Error: {err}")
#
#
# get_expensive_json('data.json', 'expensive.txt')


# Задание: фильтрация товаров по цене
# Условие:
# У тебя есть строка в формате JSON — список товаров. Нужно:
#
# Преобразовать её в Python-объект с помощью json.loads().
#
# Отфильтровать товары дороже 1000.
#
# Полученный список преобразовать обратно в JSON-строку с помощью json.dumps().
#
# Вывести результат.

# json_data = '''
# [
#     {"product": "Phone", "price": 800},
#     {"product": "Laptop", "price": 1200},
#     {"product": "Tablet", "price": 600},
#     {"product": "Monitor", "price": 1500}
# ]
# '''
#
# import json
#
# def get_filtered_items(data: str):
#     try:
#         content = json.loads(data)
#
#         filtered_items = list(filter(lambda product: product['price'] >= 1000, content))
#
#         return json.dumps(filtered_items, ensure_ascii=False)
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# print(get_filtered_items(json_data))


# 📌 Твоя задача:
# Считать содержимое из users.json.
#
# Оставить только пользователей старше 18 лет.
#
# Записать результат в новый файл adults.json.
#
# Дополнительно: вывести на экран количество взрослых и их имена.


# import json
#
# def get_adults_in_json(src_file_name: str, new_file_name: str):
#     try:
#         with open(src_file_name, 'r', encoding='utf-8') as file:
#             json_content = json.load(file)
#
#             adult_users = list(filter(lambda user: user['age'] >= 18, json_content))
#
#         with open(new_file_name, 'w', encoding='utf-8') as new_file:
#             json.dump(adult_users, new_file, indent=4, ensure_ascii=False)
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# get_adults_in_json('users.json', 'adults.json')


# import json
#
#
# def get_category_report(src_file_name: str, new_file_name: str):
#     try:
#         with open(src_file_name, 'r', encoding='utf-8') as file:
#             json_content = json.load(file)
#
#             output = {}
#
#             for item in json_content:
#                 category = item['category']
#                 quantity = int(item['quantity'])
#                 price = int(item['price'])
#
#                 if not category in output:
#                     output[category] = [quantity, quantity * price]
#                 else:
#                     output[category][0] += quantity
#                     output[category][1] += quantity * price
#
#             json_output = {}
#
#             for category in list(output.items()):
#                 json_output[category[0]] = {"total_quantity": category[1][0], "total_revenue": category[1][1]}
#
#         with open(new_file_name, 'w', encoding='utf-8') as output_file:
#             json.dump(json_output, output_file, ensure_ascii=False, indent=4)
#
#     except Exception as err:
#         print(f'Error: {err}')
#
#
# get_category_report('sales.json', 'category_report.json')



##### class #####



# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category
#
#     def __str__(self):
#         return f'{self.name}, {self.price}, {self.category}'
#
#     def is_expensive(self):
#         return self.price >= 10000
#
#     def to_dict(self):
#         return {'Name': self.name, 'Price': self.price, 'Category': self.category}
#
# class Cart:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def total_price(self):
#         return sum(p.price for p in self.products)
#
#     def show_cart(self):
#         print('Cart:')
#         for p in self.products:
#             print(p.to_dict())
#         print(f'Total sum: {self.total_price()} USD')
#
#
# new_product = Product('Phone', 2000, 'Electronics')
#
# # print(new_product)
# #
# # print(new_product.is_expensive())
# #
# # print(new_product.to_dict())
#
# cart = Cart()
# cart.add_product(new_product)
# cart.add_product(Product('Microwave', 1000, 'Electronics'))
# cart.show_cart()


# EMPLOYEES = []
# PROJECTS = []
#
# class Employee:
#     def __init__(self, name: str, position: str, salary: int, projects=None):
#         if projects is None:
#             projects = []
#         self.name = name
#         self.position = position
#         self.salary = salary
#         self.projects = projects
#
#         EMPLOYEES.append({
#             'name': self.name,
#             'position': self.position,
#             'salary': self.salary,
#             'projects': self.projects
#         })
#
#
#     def __str__(self):
#         return f'{self.name}, {self.position}, {self.salary}'
#
#
#     def assign_projects(self, project):
#         if project.name not in self.projects:
#             self.projects.append(project.name)
#             if self.name not in project.employees_assigned:
#                 project.add_employee(self)
#
#
#     def total_projects(self):
#         return len(self.projects)
#
#
# class Project:
#     def __init__(self, name: str, budget: int, employees_assigned=None):
#         if employees_assigned is None:
#             employees_assigned = []
#         self.name = name
#         self.budget = budget
#         self.employees_assigned = employees_assigned
#
#         PROJECTS.append({
#             'name': self.name,
#             'budget': self.budget,
#             'employees_assigned': employees_assigned
#         })
#
#
#     def __str__(self):
#         return f'{self.name}, {self.budget}'
#
#
#     def add_employee(self, employee):
#         if employee not in self.employees_assigned:
#             self.employees_assigned.append(employee.name)
#             if self.name not in employee.projects:
#                 employee.assign_projects(self)
#
#
#     def total_salary_cost(self):
#         total = 0
#
#         for emp_name in self.employees_assigned:
#             for emp in EMPLOYEES:
#                 if emp['name'] == emp_name:
#                     total += emp['salary']
#                     break
#
#         return total
#
#
# employee1 = Employee('Vlad','Python Engineer', 100000)
# employee2 = Employee('Liza', 'Web Developer', 80000)
#
# project1 = Project('Corporate Page', 1000000)
# project2 = Project('Advertisement campaign', 1500000)
#
# employee1.assign_projects(project1)
# employee2.assign_projects(project1)
# employee2.assign_projects(project1)
# employee1.assign_projects(project2)
#
#
# print(employee1.total_projects())
#
# print(project1.total_salary_cost())
#
# print(employee1)
#
# print(EMPLOYEES)
# print(PROJECTS)


# class Book:
#     def __init__(self, title: str, author: str, pages: int):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#
#     def __str__(self):
#         return f'{self.title}, {self.author}, {self.pages} pages'
#
#
#     def is_long(self):
#         return self.pages >= 300
#
#
# book1 = Book('Karamazov Brothers', 'Fedor Dostojevskij', 900)
#
# print(book1)
#
# print(book1.is_long())


# class Rectangle:
#     def __init__(self, width: (int, float), height: (int, float)):
#         self.width = width
#         self.height = height
#
#
#     def area(self):
#         return self.width * self.height
#
#
#     def perimeter(self):
#         return 2*self.width + 2*self.height
#
#
# rect1 = Rectangle(5, 10)
#
# print(rect1.area())
#
# print(rect1.perimeter())


# class Student:
#     def __init__(self, name: str, grades: list):
#         self.name = name
#         self.grades = grades
#
#
#     def __str__(self):
#         return f'{self.name}, grades: {self.grades}'
#
#
#     def add_grade(self, grade):
#         if not isinstance(grade, (int, float)):
#             print('Type number to add a grade')
#             return None
#
#         self.grades.append(grade)
#
#
#     def average(self):
#         if not self.grades:
#             return 0
#
#         return sum(self.grades) / len(self.grades)


# class BankAccount:
#     def __init__(self, owner: str, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#
#     def __str__(self):
#         return f'{self.owner} --- {self.balance} USD'
#
#
#     def deposit(self, amount):
#         try:
#             if amount > 0 and isinstance(amount, (float, int)):
#                 self.balance += amount
#             else:
#                 raise ValueError
#
#         except Exception:
#             print('Deposit sum has to be positive number')
#
#
#     def withdraw(self, amount):
#         try:
#             if amount <= self.balance and isinstance(amount, (float, int)):
#                 self.balance -= amount
#             else:
#                 raise ValueError
#
#         except Exception:
#             print('Withdraw sum can not exceed your current balance')
#
#
# new_acc = BankAccount('Vlad')
#
# new_acc.deposit(20000)
#
# new_acc.withdraw(2000000)
#
# print(new_acc)


# MOVIES = []
#
# import datetime
#
# year_now = datetime.datetime.today().year
#
# class Movie:
#     def __init__(self, title: str, director: str, year: int, rating: float):
#         self.title = title
#         self.director = director
#
#         try:
#             if 1900 <= year <= year_now:
#                 self.year = year
#             else:
#                 self.year = None
#                 raise ValueError
#         except ValueError:
#             print('Type correct year value (1900 - current year)')
#
#         try:
#             if 0 <= rating <= 10:
#                 self.rating = rating
#             else:
#                 self.rating = None
#                 raise ValueError
#         except ValueError:
#             print('Type rating in range from 0 to 10')
#
#         for m in MOVIES:
#             if m.title == self.title:
#                 print('Movie with this title was already added')
#                 return None
#
#         MOVIES.append(self)
#
#
#     def __str__(self):
#         return f'{self.title} ({self.year}), by {self.director} - {self.rating}/10'
#
#
# movie1 = Movie('Inception', 'Christopher Nolan', 2010, 8.8)
# movie2 = Movie('The Godfather', 'Francis Ford Coppola', 1972, 9.2)
# movie3 = Movie("One Flew Over the Cuckoo's Nest", 'Miloš Forman', 1975, 8.7)
#
#
# class Cinema:
#     def __init__(self, name: str, movies=None):
#         self.name = name
#         if not movies:
#             self.movies = []
#
#
#     def add_movie(self, movie):
#         for m in MOVIES:
#             if movie.title == m.title: # есть ли фильм в списке доступных фильмов
#                 for item in self.movies: #
#                     if movie.title == item.title:  # нет ли фильма в списке уже имеющихся в кинотеатре фильмов
#                         print('Movie with this title was already added')
#                         return None
#
#         self.movies.append(movie)
#
#
#     def show_movies(self):
#         for movie_obj in self.movies:
#             print(f'{movie_obj.title} ({movie_obj.year}), by {movie_obj.director} - {movie_obj.rating}/10')
#
#
#     def top_movie(self):
#         print(f'Top movie - {max(self.movies, key=lambda m: m.rating)}')
#
#
#     def classic_movies(self):
#         filtered_movies = list(filter(lambda m: m.year < year_now - 30, self.movies))
#
#         print('Classic movies:')
#
#         for m in filtered_movies:
#             print(f'{m.title} ({m.year}), by {m.director} - {m.rating}/10')
#
#
# new_cinema = Cinema("Cinema City")
#
# new_cinema.add_movie(movie1)
# new_cinema.add_movie(movie2)
# new_cinema.add_movie(movie3)
#
# new_cinema.show_movies()


# import datetime
# import json
#
# current_year = datetime.datetime.today().year
#
# BOOKS = [] # доступные книги
#
# class Book:
#     def __init__(self, title: str, author: str, year: int, genre: str):
#         self.title = title
#         self.author = author
#         self.genre = genre
#
#         try:
#             if year < current_year and isinstance(year, int):
#                 self.year = year
#             else:
#                 raise ValueError
#         except ValueError:
#             print('Type correct year')
#
#         if BOOKS:
#             for b in BOOKS:
#                 if b.title == self.title:
#                     print('This title was already added')
#                     return None
#
#         BOOKS.append(self)
#
#
# book1 = Book("Brave New World", "Aldous Huxley", 1932,"Science Fiction")
# book2 = Book("1984", "George Orwell", 1949,"Dystopian")
#
#
# class Library:
#     def __init__(self, books=None):
#         if not books:
#             self.books = []
#
#     def add_book(self, book_obj):
#         if self.books:
#             for b in self.books:
#                 if b.title == book_obj.title:
#                     print('This title was already added')
#                     return None
#
#         self.books.append(book_obj)
#
#
#     def show_library(self):
#         if self.books:
#             print("Library")
#             for b in self.books:
#                 print(f'{b.title}, {b.author}, {b.year}, {b.genre}')
#         else:
#             print('Library is empty')
#
#
#     def save_library_to_json(self):
#         data = []
#
#         for book in self.books:
#             data.append({"title": book.title, "author": book.author, "year": book.year, "genre": book.genre})
#
#         with open('books.json', 'w', encoding='utf-8') as json_file:
#             json.dump(data, json_file, ensure_ascii=False, indent=4)
#
#
#     def save_json_to_library(self):
#         try:
#             with open('json_books.json', 'r', encoding='utf-8') as json_file:
#                 content = json.load(json_file)
#
#             for book_data in content:
#                 if any(b.title == book_data["title"] for b in BOOKS):
#                     print(f'Book "{book_data["title"]}" already exists. Skipping.')
#                     continue
#
#                 new_book = Book(
#                     title=book_data["title"],
#                     author=book_data["author"],
#                     year=book_data["year"],
#                     genre=book_data["genre"]
#                 )
#
#                 if new_book:
#                     self.add_book(new_book)
#
#             print("Books successfully loaded from JSON into library.")
#
#         except Exception as e:
#             print(f"Error loading from JSON: {e}")
#
# library1 = Library()
#
# # library1.add_book(book1)
# # library1.add_book(book2)
#
# # library1.show_library()
# #
# # library1.save_library_to_json()
#
# library1.save_json_to_library()



##### API requests #####


# import requests
#
# def get_movie_info(title):
#     url = f"http://www.omdbapi.com/?t={title}&apikey=thewdb"
#     response = requests.get(url)
#     data = response.json()
#
#     if data["Response"] == "True":
#         print(f"Название: {data['Title']}")
#         print(f"Год: {data['Year']}")
#         print(f"Жанр: {data['Genre']}")
#         print(f"Режиссёр: {data['Director']}")
#         print(f"IMDb рейтинг: {data['imdbRating']}")
#     else:
#         print("Фильм не найден.")
#
# movie_name = input("Введи название фильма: ")
# get_movie_info(movie_name)


# import requests
#
# def exchange_currency(src_currency: str, final_currency: str, verbose=True):
#     url = f"https://open.er-api.com/v6/latest/{src_currency}"
#
#     response = requests.get(url)
#
#     if verbose:
#         print(f"Rate {src_currency} to {final_currency}: {response.json()['rates'][final_currency]}")
#
#     return response.json()['rates'][final_currency]
#
# print(exchange_currency('USD', 'UAH'))


# import requests
#
# def get_weather(city: str, verbose: bool=True):
#     try:
#         url = f'https://wttr.in/{city}?format=j1'
#
#         data = requests.get(url, timeout=5)
#
#         if data.status_code == 404:
#             raise ValueError
#
#         temp_c_feels_like = data.json()["current_condition"][0]['FeelsLikeC']
#         humidity = data.json()["current_condition"][0]['humidity']
#         weather_desc = data.json()["current_condition"][0]['weatherDesc'][0]['value']
#
#         if verbose:
#             print(f'Temperature in {city} now - feels like {temp_c_feels_like} °C, humidity - {humidity}, {weather_desc.lower()} ')
#
#     except ValueError:
#         print('Error 404')
#     except requests.exceptions.Timeout:
#         print('Timeout to get request from server')
#
# get_weather("Lodz")


# import requests
#
#
# def get_random_dog_image():
#     try:
#         url = 'https://dog.ceo/api/breeds/image/random'
#
#         response = requests.get(url)
#
#         data = response.json()
#         image_url = data['message']
#
#         image_response = requests.get(image_url, stream=True)
#
#         with open('dog.jpg', 'wb') as dog_img:
#             for chunk in image_response.iter_content(chunk_size=8192):
#                 dog_img.write(chunk)
#
#         return 'Image saved as dog.jpg'
#
#     except requests.exceptions as err:
#         print(f'Error: {err}')
#
# print(get_random_dog_image())

# import datetime
# import csv
#
# margin_year = 1900
# current_year = int(datetime.datetime.now().year)
#
# movies = []
#
#
# class Movie:
#     _id_num = 1
#
#     def __init__(self, title: str, year: str, genre: str):
#         self.id = Movie._id_num
#         Movie._id_num += 1
#         self.title = title
#         self.year = year
#         self.genre = genre
#
#
#
#     def __str__(self):
#         return f'{self.id}. {self.title} ({self.year}) - {self.genre}'
#
#
# def add_movie():
#     m_title = input('Введите название фильма: ').strip()
#     m_year = input('Введите год фильма: ').strip()
#
#     if not m_year.isdigit() or not margin_year < int(m_year) < current_year:
#         print('Введен неправильный год или неверный формат даты')
#
#     m_genre = input('Введите жанр фильма: ').strip()
#
#     new_movie = Movie(m_title, m_year, m_genre)
#
#     movies.append(new_movie)
#
#
# def list_movies():
#     for m in movies:
#         print(m)
#
#
# def save_to_csv():
#     with open('movies.csv', 'w', encoding='utf-8') as new_file:
#         new_file.write('Индекс,название,год,жанр\n')
#
#         for m in movies:
#             new_file.write(f'{m.id},{m.title},{m.year},{m.genre}\n')
#
#
# def load_from_csv():
#     try:
#         file_name = input('Введите имя искомого файла: ').strip()
#
#         with open(file_name, 'r', encoding='utf-8') as src_file:
#             file_content = list(csv.reader(src_file))
#
#         file_content.pop(0)
#
#         for m in file_content:
#             m.pop(0)
#
#         for film in file_content:
#             movies.append(Movie(list(film)[0], list(film)[1], list(film)[2]))
#
#     except Exception as err:
#         print(f'Ошибка: {err}')

# Вам дано положительное целое число, num состоящее только из цифр 6 и 9.
#
# Верните максимальное число, которое вы можете получить, изменив не более одной цифры (6 становится 9, а 9 становится 6).

# import random
#
# def get_random69():
#     res = 0
#     source = (6, 9)
#     mult = 1000
#
#     for _ in range(4):
#         res += mult * random.choice(source)
#         mult /= 10
#
#     return int(res)
#
#
# def get_max69(data: int):
#     dig_changed = False
#
#     digs = []
#
#     for char in str(data):
#         digs.append(char)
#
#     for dig in digs:
#         if not dig_changed:
#             if dig == '6':
#                 digs[digs.index('6')] = '9'
#                 dig_changed = True
#
#     return ''.join(digs)
#
#
# rand_num = get_random69()
# print(rand_num)
#
#
# print(get_max69(rand_num))

# Дан массив целых чисел nums и целое число target, вернуть индексы двух чисел так, чтобы их сумма давала target .
#
# Вы можете предположить, что каждый вход будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.
#
# Вы можете возвращать ответ в любом порядке.

# nums = [1, 5, 9, -1]
# t1 = 10
# t2 = 100
#
# def get_sum(data: list, target: int):
#     data_copy = data.copy()
#
#     for element in data:
#         data_copy.pop(0)
#
#         for e in data_copy:
#             if element + e == target:
#                 return data.index(element), data.index(e)
#
#     return 'target not found'
#
#
# print(get_sum(nums, t1))

# n1 = [2,4,3]
# n2 = [5,6,4]
#
# def get_sum(num1: list, num2: list):
#     num1_rev = num1.copy()
#     num1_rev.reverse()
#     num1_rev = list(map(lambda el: str(el), num1_rev))
#     num1_rev = ''.join(num1_rev)
#
#     num2_rev = num2.copy()
#     num2_rev.reverse()
#     num2_rev = list(map(lambda el: str(el), num2_rev))
#     num2_rev = ''.join(num2_rev)
#
#     return int(num1_rev) + int(num2_rev)
#
#
# print(get_sum(n1,n2))

# Дан целочисленный массив nums, вернуть все триплеты, [nums[i], nums[j], nums[k]]
# такие что i != j, i != k, и j != k, и nums[i] + nums[j] + nums[k] == 0.
#
# Обратите внимание, что набор решений не должен содержать повторяющихся триплетов.


# nums = [0,1,0]
#
# def get_all_triplets(data: list):
#     res = []
#
#     for i in range(len(data)):
#         for j in range(i+1, len(data)):
#             for k in range(j+1, len(data)):
#                 triplet = [data[i], data[j], data[k]]
#                 if sum(triplet) == 0 and i != j and i != k and j != k:
#                     if sorted(triplet) not in res:
#                         res.append(sorted(triplet))
#
#     return res
#
#
# print(get_all_triplets(nums))


# def merge_lists(data: list):
#     merged = []
#
#     for l in data:
#         merged += l
#
#     return sorted(merged)
#
#
# print(merge_lists([[1,4,5],[1,3,4],[2,6]]))

# source_data = [5, 7, 9, 11, 13, 15, 17]
#
# def swap_couples(data: list):
#     output = []
#
#     for i in range(0, len(data), 2):
#         if i != len(data) - 1:
#             output.append(data[i + 1])
#
#         output.append(data[i])
#
#     return output
#
#
# print(swap_couples(source_data))


# def sum_seq(n: int):
#     if n == 1:
#         return 1
#
#     return n + sum_seq(n - 1)
#
#
# print(sum_seq(5))


# def get_factorial(n: int):
#     if n == 1:
#         return 1
#
#     return n * get_factorial(n - 1)
#
#
# print(get_factorial(10))

# result = ''

# def get_rev_str(data: str, result):
#     if data == '':
#         return result
#
#     result += data[-1]
#     data = data[:-1]
#     return get_rev_str(data, result)
#
# print(get_rev_str('hello',''))


# def get_sum(data: list, res=0):
#     if not data:
#         return res
#     res += data[0]
#     data.pop(0)
#
#     return get_sum(data, res)
#
#
# print(get_sum([1,2,3,4,5]))


# def get_max(data: list, res=None):
#     if not data:
#         return res
#
#     if not res:
#         res = data[0]
#     else:
#         if data[0] > res:
#             res = data[0]
#
#     data.pop(0)
#
#     return get_max(data, res)
#
#
# print(get_max([-100, 230, 40, 1, 2, 3]))


# def get_len_str(data: str, res=0):
#     if not data:
#         return res
#
#     data = data[:-1]
#     res += 1
#
#     return get_len_str(data, res)
#
#
# print(get_len_str('hello world'))


# # Найди все цифры в строке "Мой номер: 123-456-7890".
#
# import re
#
# def get_digs(data: str):
#     res = re.findall(r'\d', data)
#
#     return res
#
#
# print(get_digs("Мой номер: 123-456-7890"))


# Найди все слова, начинающиеся с буквы "a" в "apple and apricot are not awesome".

# import re
#
# def startswith(data: str, letter_or_string='a'):
#     res = []
#
#     for w in data.split():
#         if re.match(pattern=fr'{letter_or_string}',string=w):
#             res.append(w)
#
#
#     return res
#
# print(startswith('apple and apricot are not awesome', 'n'))
# print(startswith("Hello world", "Hello"))

# pattern = 'example@domain.com'
#
# import re
#
# def check_valid_email(data: str):
#     if re.fullmatch(r'\w+@[a-z]+\.(com|net|org)', data):
#         return True
#
#     return False
#
#
# print(check_valid_email(pattern))


# Извлечение хэштегов:
# Дана строка с текстом, например "Я люблю #python и #regex". Нужно вернуть список всех слов, начинающихся с #.


# import re
#
# def get_hashtags(data: str):
#     res = []
#
#     for w in data.split():
#         if re.match('#', w):
#             res.append(w)
#
#     return res
#
#
# print(get_hashtags('Я люблю #python и #regex'))

# Замена цифр на *:
# Дана строка с числами, например "Мой номер 1234". Замени все цифры на * с помощью re.sub.

# import re
#
# def replace_digs(data: str):
#     return re.sub(r'\d', '*', data)
#
#
# print(replace_digs('1234 my number'))


# products = ["apple", "banana", "cherry"]
# prices = [2, 3, 5]
#
# def get_dict(data1: list, data2: list):
#     return dict(zip(data1,data2))
#
#
# print(get_dict(products, prices))
#
#
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
#
#
# def get_grades(data1: list, data2: list):
#     for k, v in list(zip(data1, data2)):
#         print(f'{k}: {v}')
#
#
# get_grades(names, scores)


# fruits = ["apple", "banana", "cherry", "mango"]
#
#
# def get_enum(data: list):
#     for i, p in enumerate(data, start=1):
#         print(f'{i}. {p}')
#
#
# get_enum(fruits)


# numbers = [10, 20, 30, 40]
#
# def get_num_dict(data: list):
#     output = {}
#
#     for i, n in enumerate(data):
#         output[i] = n
#
#     return output
#
#
# print(get_num_dict(numbers))


# cities = ["Warsaw", "Berlin", "Paris"]
# countries = ["Poland", "Germany", "France"]
#
#
# def get_enum_pairs(data1: list, data2: list):
#     tuples = list(zip(data1, data2))
#
#     for i, tup in enumerate(tuples, start=1):
#         print(f'{i}. {tup[0]} - {tup[1]}')
#
#
# get_enum_pairs(cities, countries)


# nums = [0, 0, 0, 5, 0]
#
# def check_if_not0(data: list):
#     if any(n != 0 for n in data):
#         return True
#
#     return False
#
# print(check_if_not0(nums))


# flags = [True, True, True, False]
#
# def check_if_all_true(data: list):
#     if all(data):
#         return True
#
#     return False
#
#
# print(check_if_all_true(flags))


# text = "Python3"
#
# def check_if_dig_char(data: str):
#     if any(char.isdigit() for char in data):
#         return True
#
#     return False
#
#
# print(check_if_dig_char(text))


# email = "test@example.com"
#
# def check_dot_and_at(data: str):
#     if any(char == '@' for char in data) and any(char == '.' for char in data):
#         return True
#
#     return False
#
#
# print(check_dot_and_at(email))


# numbers = [10, 15, 20, 25, 30]
#
# def check_division(data: list):
#     return all(num % 5 == 0 for num in data)
#
#
# print(check_division(numbers))


# words = ["hello", "world", "python", "AI"]
#
# def check_len(data: list):
#     return any(len(word) > 5 for word in data)
#
#
# print(check_len(words))


# users = [
#     {"name": "Alice", "active": True},
#     {"name": "Bob", "active": True},
#     {"name": "Charlie", "active": False}
# ]
#
# def check_inactive(data: list):
#     return any(not user['active'] for user in data)
#
#
# print(check_inactive(users))


# passwords = ["qwerty1", "hello", "Pass1234", "admin"]
#
# def if_contain_dig(data: list):
#     return all((any(char.isdigit() for char in p)) for p in data)
#
#
# print(if_contain_dig(passwords))


# emails = ["test@gmail.com", "invalidmail", "user@domain.org"]
#
# def check_valid(data: list):
#     return all((any(char == '@' for char in mail) and (any(char == '.' for char in mail)) for mail in data))
#
#
# print(check_valid(emails))


# orders = [
#     {"id": 1, "paid": True},
#     {"id": 2, "paid": True},
#     {"id": 3, "paid": True},
# ]
#
#
# def check_payments(data: list):
#     return all(order['paid'] for order in data)
#
#
# print(check_payments(orders))


# words = ["sky", "fly", "try", "apple", "orange", 'fck']
#
#
# def check_vowels(data: list):
#     vowels = 'eyaio'
#
#     return all(any(char in vowels for char in word) for word in data)
#
#
# print(check_vowels(words))



# вернуть True, если у всех студентов хотя бы одна оценка >= 90

# students = [
#     {"name": "Alice", "grades": [90, 80, 70]},
#     {"name": "Bob", "grades": [85, 60, 90]},
#     {"name": "Charlie", "grades": [85, 95, 75]}
# ]
#
# def check_excel(data: list):
#     return all(any(grade >= 90 for grade in student['grades']) for student in data)
#
#
# print(check_excel(students))


# вернуть True, если хотя бы одна задача полностью выполнена (все подзадачи True)

# tasks = [
#     {"task": "Task1", "subtasks": [True, True, True]},
#     {"task": "Task2", "subtasks": [True, False, True]},
#     {"task": "Task3", "subtasks": [True, True]}
# ]
#
# def check_tasks_done(data: list):
#     return all(all(sub for sub in task['subtasks']) for task in data)
#
#
# print(check_tasks_done(tasks))


# вернуть True, если все пароли содержат хотя бы одну букву и хотя бы одну цифру

# passwords = ["abc123", "passw1rd", "a123456", "admin1"]
#
# def check_validity(data: list):
#     return all(any(char.isalpha() for char in p) and any(char.digit() for char in p) for p in data)
#
#
# print(check_validity(passwords))


# employees = [
#     {"name": "Anna", "age": 28, "years_at_company": 3},
#     {"name": "Bob", "age": 35, "years_at_company": 10},
#     {"name": "Clara", "age": 23, "years_at_company": 1}
# ]
#
#
# # Нужно написать функцию, которая возвращает True, если все сотрудники старше 25 лет и работают больше года, иначе False.
#
# def check_employees(data: list):
#     return all(employee['age'] >= 25 and employee['years_at_company'] >= 1 for employee in data)
#
#
# print(check_employees(employees))


# guests = [
#     {"name": "Tom", "coming": True},
#     {"name": "Jerry", "coming": False},
#     {"name": "Spike", "coming": True}
# ]
#
# # Нужно определить:
# #
# # Придёт ли хотя бы один гость.
# #
# # Все ли подтвердили своё присутствие.
#
# def check_invites(data: list):
#     '''
#     :param data: invitations acceptance list
#     :return: tuple[0] --- if any guest accepted invitation, tuple[1] --- if all guests accepted invitations
#     '''
#
#     return any(guest['coming'] for guest in data), all(guest['coming'] for guest in data)
#
#
# print(check_invites(guests))


# # Задача 3: Проверка чисел
# #
# # У тебя есть список чисел, и нужно:
# #
# # Проверить, все ли числа положительные.
# #
# # Проверить, есть ли хотя бы одно число, которое делится на 7.
#
#
# def check_nums(data: list):
#     return all(num > 0 for num in data), any(num % 7 == 0 for num in data)
#
#
# print(check_nums([1, -7, 10, 2, 7]))


# orders = [
#     {"item": "apple", "quantity": 5},
#     {"item": "banana", "quantity": 0},
#     {"item": "orange", "quantity": 3}
# ]
#
# # Нужно определить:
# #
# # Все ли заказы имеют количество больше нуля.
# #
# # Есть ли хотя бы один заказ с количеством больше 10.
#
#
# def check_orders(data: list):
#     return all(order['quantity'] > 0 for order in data), any(order['quantity'] >= 10 for order in data)
#
#
# print(check_orders(orders))


# employees = [
#     {"name": "Anna", "projects": [{"name": "A", "completed": True}, {"name": "B", "completed": False}]},
#     {"name": "Bob", "projects": [{"name": "A", "completed": True}, {"name": "C", "completed": False}]},
#     {"name": "Clara", "projects": [{"name": "B", "completed": True}]}
# ]
#
# # Определи, есть ли хотя бы один сотрудник, у которого все проекты завершены.
# #
# # Определи, все ли сотрудники хотя бы один проект завершили.
#
# def check_emp(data: list):
#     return any(all(p['completed'] for p in emp['projects']) for emp in data), all(any(p['completed'] for p in emp['projects']) for emp in data)
#
#
# print(check_emp(employees))


# events = [
#     {"event": "Concert", "attendees": [{"name": "Tom", "came": True}, {"name": "Jerry", "came": True}]},
#     {"event": "Meetup", "attendees": [{"name": "Spike", "came": False}]},
#     {"event": "Workshop", "attendees": [{"name": "Anna", "came": True}]}
# ]
#
# # Проверь, есть ли хотя бы одно событие, где пришли все приглашённые.
# #
# # Есть ли событие, где никто не пришёл?
#
#
# def check_events(data: list):
#     return any(all(attendee['came'] for attendee in event['attendees']) for event in data), any(all(not attendee['came'] for attendee in event['attendees']) for event in data)
#
#
# print(check_events(events))


# products = [
#     {"name": "Laptop", "price": 1200, "stock": 5, "on_sale": True},
#     {"name": "Mouse", "price": 25, "stock": 0, "on_sale": False},
#     {"name": "Keyboard", "price": 80, "stock": 12, "on_sale": True}
# ]
#
# # Определи, все ли товары в наличии стоят дороже 50.
# #
# # Определи, есть ли хотя бы один товар в наличии, который одновременно на распродаже и стоит меньше 100.
#
#
# def check_stock(data: list):
#     filtered_stock = list(filter(lambda product: product['stock'], data))
#
#     return all(item['price'] >= 50 for item in filtered_stock), any(item['price'] < 100 and item['on_sale'] for item in filtered_stock)
#
#
# print(check_stock(products))


# Email-фильтр
# Дана строка с текстом, где встречаются email-адреса. Нужно вытащить все корректные email-адреса.
# Условие: email состоит из букв, цифр, точек, подчёркиваний и дефисов до @, домен — только буквы, точка и ещё буквы (например: user.name-1@mail.com).

# import re
#
# text = "user123@mail.com, fake-email@@example.com, anna.kowalski@wp.pl, test@domain, john.doe@gmail.com"
#
# def extract_valid_emails(data: str):
#     template = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
#
#     return re.findall(template, data)
#
#
# print(extract_valid_emails(text))

# import re


# text = "I have 2 cats, 3 dogs, and 15 fish."
#
# def get_digits(data: str):
#     return re.findall(r'\d', data)
#
#
# print(get_digits(text))


# text = "apple banana cherry apple banana"
#
# def find_word(data: str, word: str):
#     return re.findall(word, data)
#
#
# print(find_word(text, 'apple'))


# text = "Hello! How are you? I'm fine, thanks!"
#
#
# def get_all_words(data: str):
#     return re.findall(r"[A-Za-z']+", data)
#
#
# print(get_all_words(text))

# text = "Contact us at support@example.com or sales@example.org"
#
# def get_emails(data: str):
#     return re.findall(r'\S+@\S+', data)
#
#
# print(get_emails(text))


# text = "The prices are: $5, $10, and $100."
#
# def get_prices(data: str):
#     return re.findall(r'\$\d+', data)
#
#
# print(get_prices(text))

# import re
#
#
# mess = "My phone numbers are 123-456-7890 and 987-654-3210."
#
# def get_nums(data: str):
#     nums_with_blanks = re.findall(r'\d{3}-\d{3}-\d{4}', data)
#
#     only_nums = list(map(lambda num: num.replace('-', ''), nums_with_blanks))
#
#     return only_nums
#
#
# print(get_nums(mess))


# text = "Am I sleeping? I have a cat, a dog, and a parrot."
#
#
# def get_startswith(data: str, letter: str):
#     return re.findall(fr'\b{letter}[A-Za-z\'-]*\b', data, re.IGNORECASE)
#
#
# print(get_startswith(text, 'a'))


# замени все знаки препинания на пробел

# import string
#
# text = "Hello! How are you? I'm fine."
#
# def sub_punctuation(data: str):
#     return re.sub(fr'[{string.punctuation}]', ' ', data)
#
#
# print(sub_punctuation(text))


# task = 'В строке "My emails: first@example.com, second@test.org" извлеки все адреса электронной почты.'
#
# def only_emails(data: str):
#     data = data.replace('"', '')
#     data = data.replace(',', '')
#
#     return re.findall(r'\S+@\S+', data)
#
#
# print(only_emails(task))


# import re


# text = "Order numbers: AB123, XY456, Z789."
#
# def get_codes(data: str):
#     return re.findall(r'\b[A-Z]{2}\d{1,3}\b', data)
#
#
# print(get_codes(text))


# text2 = "The temperatures are -5, 0, 15, and +20 degrees."
#
# def get_tems(data: str):
#     return re.findall(r'[+-]*\d+', data)
#
#
# print(get_tems(text2))

# text3 = "Call me at 123-456-7890 or 987-654-3210."
#
#
# def get_country_phones(data: str):
#     full_nums = re.findall(r'\d{3}-\d{3}-\d{4}', data)
#
#     result = []
#
#     for num in full_nums:
#         result.append((num[:3], num[4:]))
#
#     return result
#
#
# print(get_country_phones(text3))


# Найди все пароли, состоящие из букв + цифр, и раздели их на две группы: буквы и цифры.

# text4 = "My passwords: abc1234, qwer456, xyz789."
#
# def get_sep(data: str):
#     passwords = re.findall(r'[A-Za-z]+\d+', data)
#
#     res = []
#
#     for p in passwords:
#         res.append((re.search(r'[A-Za-z]+', p).group(), re.search(r'\d+', p).group()))
#
#     return res
#
#
# print(get_sep(text4))


# Замени все знаки препинания на пробел.
#
# Удали все лишние пробелы подряд, чтобы остался один пробел между словами.

# import string
#
# text5 = "Hello! How are you? I'm fine."
#
# def get_bad_order(data: str):
#     extra_spaces = re.sub(fr'[{string.punctuation}]', ' ', data)
#
#     print(extra_spaces)
#
#     result = re.sub(r'\s+', ' ', extra_spaces)
#
#     if result[-1] == ' ':
#         result = result[:-1]
#
#     return result
#
#
# print(get_bad_order(text5))


# text6 = "Contact: support@example.com, admin@test.org, fake@wrong."
#
# def blur_emails(data: str):
#     blur = '[EMAIL]'
#
#     res = re.sub(r'\S+@\S+', blur + ',', data)
#
#     res = res[:-1] + '.'
#
#     return res
#
#
# print(blur_emails(text6))


# import re


# text = 'Hello, world!'
#
# def startswith(data: str):
#     return re.match('Hello', data).group()
#
#
# print(startswith(text))


# text = "123-456-7890"
#
# def check_pattern(data: str):
#     pattern = r'\d{3}-\d{3}-\d{4}'
#
#     if re.fullmatch(pattern, data):
#         return 'match'
#
#     return None
#
#
# print(check_pattern(text))

# text = "My email is test@example.com for contact."
#
# def find_email(data: str):
#     email = re.search(r'\S+@\S+', data)
#
#     if email:
#         return email.group()
#
#     return None
#
#
# print(find_email(text))


# text = "Order codes: AB123, XY456, Z789."
#
# def get_iter(data: str):
#     codes = re.finditer(r'[A-Z]+\d+', data)
#
#     result = []
#
#     for code in codes:
#         result.append((code.group(), code.span()))
#
#     return result
#
#
# print(get_iter(text))

# output_must_be = {
# 'PriceUSD': (123, 45),
# 'TaxUSD': (6, 78)
# }


# text = "PriceUSD: $123.45, TaxUSD: $6.78"
#
# def get_sums(data: str):
#     str_iter = re.findall(r'[A-Za-z]+', data)
#
#     sums = re.findall(r'\d+\.*\d*', data)
#
#     res_sums = list(map(lambda price: tuple(price.split('.')), sums))
#
#     output = {el[0]: el[1] for el in zip(str_iter, res_sums)}
#
#     return output
#
#
# print(get_sums(text))




# import sqlite3
#
# conn = sqlite3.connect('first_db.db')
#
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER,
#     email TEXT
# )
# """)
#
# conn.commit()
#
# cursor.execute(('''
# DELETE FROM users
# WHERE name = 'Vlad'
# '''))
#
# conn.commit()

# cursor.execute("""
# INSERT INTO users (name, age, email)
# VALUES ('Vlad', 21, 'vlad@example.com')
# """)
#
# conn.commit()

# cursor.execute('''
# UPDATE users
# SET age = 22
# where id = 13
# ''')
#
# conn.commit()

# cursor.execute('''
# INSERT INTO users (name, age, email)
# VALUES ('Liza', 20, 'lizka@icloud.com')
# ''')
#
# cursor.execute('''
# INSERT INTO users (name, age, email)
# VALUES ('Max', 45,'max@gmail.com')
# ''')
#
# conn.commit()

# cursor.execute('''
# SELECT name, age FROM users
# ''')
#
# data = cursor.fetchall()
#
# print(data)

# cursor.execute('''
# SELECT * FROM users
# ORDER BY age DESC, name ASC
# ''')
#
# data = cursor.fetchall()
#
# # only_25plus = list(filter(lambda user: user[2] >= 25, data))
#
# # print(only_25plus)
#
# print(data)



# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print('Please insert positive number')
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#         elif amount < 0:
#             print('Please insert positive number')
#         else:
#             print('Insufficient funds')
#
#     def info(self):
#         print(f'{self.owner}: {self.balance}')
#
#
# new_ba1 = BankAccount('Vlad')
#
# new_ba1.deposit(100)
# new_ba1.withdraw(50)
# new_ba1.info()
















