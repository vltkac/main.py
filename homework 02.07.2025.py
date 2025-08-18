# Завдання 1
# Напишіть lambda-функції, які:
#  Множить число на -1
#  Перевіряє чи рядок непорожній

# key=lambda num: -num

# key1=lambda string: string != ''

# Завдання 2
# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел, рахує середнє арифметичне та
# повертає список з числами, які більші за середнє
#  Отримує список слів та повертає список слів, в яких
# рівно 4 літери

# 1

# def filter_more_than_average(nums):
#     avg = sum(nums) / len(nums)
#
#     more_than_avg = filter(lambda num: num > avg, nums)
#
#     return list(more_than_avg)
#
#
# nums1 = [100, -500, 600, -700, 200, -800, 300, -900, 1000]
#
# print(filter_more_than_average(nums1)) # [100, 600, 200, 300, 1000]
#
#
# # 2
#
# def filter_4_letters(some_words):
#     new_words = filter(lambda word: len(word) == 4, some_words)
#
#     return list(new_words)
#
#
# words = [
#     "house", "room", "kitchen", "bed", "chair", "table", "door", "window",
#     "mother", "father", "brother", "sister", "friend", "child", "people",
#     "morning", "afternoon", "evening", "night", "today", "tomorrow", "yesterday",
#     "apple", "bread", "water", "milk", "cheese", "meat", "soup",
#     "car", "bus", "train", "bicycle", "plane", "taxi",
#     "sun", "rain", "snow", "wind", "cloud", "hot", "cold"
# ]
#
# print(filter_4_letters(words)) # ['room', 'door', 'milk', 'meat', 'soup', 'taxi', 'rain', 'snow', 'wind', 'cold']

# Завдання 3
# Напишіть функцію, яка отримує літеру та список слів і
# знаходить слово зі списку, в якому найбільша кількість даної
# літери.

# def find_max_letters_word(some_words, letter):
#     letter_count = []
#
#     for word in some_words:
#         counter = word.lower().count(letter.lower())
#         letter_count.append(counter)
#
#     index_max_letter_word = letter_count.index(max(letter_count))
#
#     return some_words[index_max_letter_word]
#
#
# words = [
#     "house", "room", "kitchen", "bed", "chair", "table", "door", "window",
#     "mother", "father", "brother", "sister", "friend", "child", "people",
#     "morning", "afternoon", "evening", "night", "today", "tomorrow", "yesterday",
#     "apple", "bread", "water", "milk", "cheese", "meat", "soup",
#     "car", "bus", "train", "bicycle", "plane", "taxi",
#     "sun", "rain", "snow", "wind", "cloud", "hot", "cold"
# ]
#
# print(find_max_letters_word(words, 'o')) # tomorrow
# print(find_max_letters_word(words, 's')) # sister
# print(find_max_letters_word(words, 'y')) # yesterday
