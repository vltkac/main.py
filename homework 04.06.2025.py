# Створіть 2 списки чисел.
# Створіть на їх основі списки з
#  Усіма числами з обох списків
#  Усіма числами з обох списків, але без повторень
#  Спільними числами для двох списків
#  Числа які є в першому, але немає в другому

first_list = [2, 5, 1, 2, 3, 4, 9, 8, 3, 2]
second_list = [5, 6, 4, 3, 5, 7, 9, 4, 6, 1]

all_nums_list = first_list + second_list
all_nums_list.sort()

print(f'Список со всеми числами из двух списков: {all_nums_list}')

all_nums_list_unique = []

for num in all_nums_list: # ищем уникальные числа
    if num not in all_nums_list_unique:
        all_nums_list_unique.append(num)

print(f'Список с уникальными числами: {all_nums_list_unique}')

common_nums = []

for num in all_nums_list: # ищем все числа, которые есть в обоих списках
    if num in first_list and num in second_list:
        common_nums.append(num)

common_nums_result = [] # список с уникальными числами списка общих (не уточнено, нужно принтить все числа или только общие значения)

for num in common_nums:
    if num not in common_nums_result:
        common_nums_result.append(num)

print(f'Список с общими числами: {common_nums_result}')

first_list_unique = []

for num in all_nums_list:
    if num in first_list and num not in second_list:
        first_list_unique.append(num)

first_list_unique_result = [] # то же самое - не уточнено, нужно принтить все числа или только общие значения

for num in first_list_unique:
    if num not in first_list_unique_result:
        first_list_unique_result.append(num)

print(f'Список с уникальными числами первого списка: {first_list_unique_result}')









