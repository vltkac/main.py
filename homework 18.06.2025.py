# Завдання 1
# Напишіть функцію, яка повертає добуток чисел з списку.
# Список передається як параметр

# def return_mul(nums):
#     multiplier = 1
#
#     for num in nums:
#         multiplier *= num
#
#     return multiplier
#
#
# print(return_mul([1, 2, 3, 4, 5, 6]))

# Завдання 2
# Напишіть функцію, яка повертає найменше число з
# списку. Список передається як параметр.

# def return_min(nums):
#     return min(nums)
#
#
# print(return_min([0.0001, 1, -100, 10000]))

# Завдання 3
# Напишіть функцію, яка повертає кількість парних
# чисел з списку. Список передається як параметр.

# def show_even(nums):
#     even_nums = []
#
#     for num in nums:
#         if num % 2 == 0:
#             even_nums.append(num)
#
#     return even_nums
#
#
# print(show_even([1, 3, 120, 666, 550]))

# Завдання 4
# Напишіть функцію, яка видаляє з списку певне число.
# Якщо число повторюється, то треба видалити всі входження.
# Функція повинна повернути кількість видалених елементів.
# Список та число передаються як параметри.

# def delete_num(nums, num_to_delete):
#     deleted_counter = 0
#     new_list = []
#
#     for num in nums:
#         if num == num_to_delete:
#             deleted_counter += 1
#         if num != num_to_delete
#             new_list.append(num)
#
#     nums[:] = new_list
#
#     return deleted_counter
#
#
# print(delete_num([1, 2, 3, 1, 4, 5, 1, 6], 1))

# Завдання 5
# Напишіть функцію, яка отримує два списи як параметри.
# Функція повинна об’єднати списки та повернути результат.
# Наприклад, якщо функція отримує списки [1, 2, 3] та [3, 4]
# то результатом має бути список [1, 2, 3, 3, 4]

# def merge_lists(nums1, nums2):
#     return nums1 + nums2
#
#
# print(merge_lists([1, 2, 3], [3, 4]))

# Завдання 6
# Напишіть функцію, яка підносить кожен елемент списку
# до степеня. Результатом має бути список з степенями всіх
# чисел. Список та показник степеня передаються як параметри.

# def power_list(power, nums):
#     powered_nums = []
#
#     for num in nums:
#         powered_nums.append(num ** power)
#
#     return powered_nums
#
#
# print(power_list(2, [-1, 0, 1, 10, 100, 200, 300]))