# # 28.04
# #
# # print('Hello, world!')
# #
# # # x
# # # x = 10
# # # x = 20
# # # x = 1 * 1000000
# #
# # #print
# # # print(x)
# #
# # #названия переменных
# # # a-z A-Z 0-9 _
# # # цифра не в начале
# # # стили
# # #snake_case = 1
# # #CamelCase = 2
# # #CONSTANT = 3
# #
# # # типы данных
# # # int - целое число (2, 3, -100)
# #
# # # float - числа с дробной частью (1.5, 3.14, -124124.1241201)
# #
# # # str - текст (последовательность символов)
# # # 'text' = "text"
# #
# # # "утиная" типизация - динамическая типизация
# # #x = 100
# # x = 'x'
# # #print(type(x)) - вывести тип данных
# # # print(x)
# #
# # # math operations
# # # a = 7
# # # b = 3
# # # print(a + b)
# # # print(a - b)
# # # print(a* b)
# # # print(a / b)
# # # print(a ** 2) #a^2
# # # print(a // b) #целая часть от деления
# # # print(a % b) #остаток от деления
# #
# # # получение данных от пользователя
# # # пользователь вводит имя и возраст. Вывести приветствие
# #
# # name = input('Please submit your name:')
# # age = input('Please submit your age:')
# #
# # # print(name)
# # # print(age)
# #
# # # форматирование строк
# # # Привет, Влад. Тебе 22 года
# #
# # print(f"Привет, {name}. Тебе {age} года")
# #
# # # конвертация типов данных
# #
# # age_str = input('Please submit your age:')
# #
# # print(type(age_str))
# #
# # age_int = int(age_str)
# #
# # print(type(age_int))
# #
# # # в одну строчку
# #
# # age = int(input('Please submit your age:'))
# # print(type(age))
# #
# # age_half = age / 2
# # print(age_half)
# #
# #
# #
# #
# #
# # practice
# # 1.1
# # читаем данные от пользователя как str (текст)
# # x = input('please submit number a')
# # y = input('please submit number b')
# #
# # #изменениe типа данных на int
# #
# # x = int(x)
# # y = int(y)
# #
# # sum = x + y
# # minus = x - y
# # multi = x * y
# #
# # print(sum)
# # print(minus)
# # print(multi)
# #
# # #1.2
# # number = input("Please submit number:")
# # percent = input("Please submit percent:")
# #
# # number = float(number)
# # percent = float(percent)
# #
# # result = number * percent / 100
# #
# # print(result)
# #
# # #2.3
# # width = input("Please submit width:")
# # length = input("Please submit length:")
# #
# # width = float(width)
# # length = float(length)
# #
# # result = width * length
# #
# # print('Your result:' , result)
#
# # 30.04
# #functions
#
# #min - функция, которая находит минимальное число
# #round - функция, которая округляет дробь
# #print etc.
#
# #find the smallest number 4, 2, 7
#
# #
# # min_num = min(4, 2, 7)
# #
# # #округлить число 12.37
# #
# # result = round(12.37)
# #
# # max_result = max(1, 2, 10, 7)
# # print(max_result)
#
# #Чтобы испечь один пирог, нужно 4 яблока. Пользователь вводит количество яблок. Посчитай количество пирогов, которое можно испечь.
#
# # apple_count = input("Введите количество яблок:")
# # apple_count = int(apple_count)
# #
# # apples_per_pie = 4
# #
# # pie_count = apple_count // apples_per_pie # Делим нацело
# # unused_apples = apple_count % apples_per_pie #Остаток от деления
# #
# # print(f"Вы можете испечь {pie_count} пирогa/ов")
# # print(f"Останется {unused_apples} яблок/a")
#
# # Программа получает количество баллов, которые получил студент за тест, а также максимально возможное количество баллов. Введите процент правильных ответов.
#
# student_score = int(input("Введите количество баллов:"))
# max_score = int(input("Введите максимальную оценку:"))
# # Обрати внимание: сначала запускается функция, которая во внутренних скобках!
#
# percent = student_score / max_score * 100
#
# # обычный вариант
# print(f"Процент правильных ответов - {percent} %")
#
# # один знак после запятой
# print(f"Процент правильных ответов - {percent:.1f} %")
# #=
# print(round(percent, 1))

# 05.05

# conditions
a = 1
b = 2
# bool - True, False - тип данных

# logical operations

# print("a > b", a > b) # if more than
# print("a < b", a < b) # if less than
# print("a == b", a == b) # if equal
# print("a != b", a != b) # if not equal
# print("a >= b", a >= b) # if equal or more than
# print("a <= b", a <= b) # if    equal or less than

# adult

# age = 27
# age >= 18
#
# # command number = 3
#
# command_id = 3
# command_id == 3
#
# # number is divided to 5
#
# num = 124
# num % 5 == 0

# if else

# print("Start program")

age = 1

# to pring notification if person is adult

# if age >= 18: # двоеточие, чтобы идентифицировать, что условие обозначено
#     # блок кода if
#     # выполняется только если условие верно
#     print("Код с if")
#     print("Conditions are fulfilled")
#     print("Person is adult")
#
# else:
#     # блок кода else
#     # выполняется когда условие неверно
#     print("Код с else")
#     print("Conditions are not fulfilled")
#     print("Person is not adult")
#
# print("End program")

# print(type(x)) Функция type говорит, какой тип данных

# Пользователь вводит возраст и цену покупки
# Детям до 12 лет (включительно) скидка 10 %

# ввод данных
# age = int(input("Введите возраст: "))
# cost = float(input("Введите цену покупки: "))
#
# percent = 0.1
#
# скидка детям до 12 лет
# if age <= 12:
#     discount = cost * percent
#     cost = cost - discount
#
# print(f"К оплате: {cost:.2f} грн")

# tab - tab
# shift + tab - minus tab



# many conditions
# пользователь вводит слово по-русски
# переведите на английский
# рассмотрите несколько слов

# word_ru = input("Введите слово: ")
#
# if word_ru == "привет":
#     print("hello")
#
# elif word_ru == "кот":
#     print("cat")
#
# elif word_ru == "яблоко":
#     print("apple")
#
# elif word_ru == "собака":
#     print("dog")
#
# else:
#     print("Неизвестное слово")

# 07.05

# 2

#  Самоприсваивание

# amount_item = int(input("Введите количество товара: "))
# price_item = int(input("Введите цену товара: "))
# percent = int(input("Введите скидку: "))
#
# # initial price
# total = amount_item * price_item
# #discount
# discount = total * (percent / 100)
# total = total - discount # =
# total -= discount # =
#
# counter = 10
#
# counter += 2 # 12
#
# counter *= 1.5 # 12 * 1.5 = 18

# 14.05.2025

# Цикл

# Цикл для перебора элементов

# вариант с числами (диапазонами)
# задача: вывести все целые числа между 1 и 10

# range(1, 10) # диапазон от 1 до 10
# print(num)

# цикл for

# for num in range(1, 10):
#     print(f"число из цикла: {num}")

# range(stop) - все числа от 0 до stop (не включительно)
# for num in range (20):
#     print(num)

# range(start, stop) - числа от start (включительно) до stop (не включительно)
# for num in range(10, 20):
#     print(num)

# range - только с целыми числами

# range(start, stop, step) - где step - шаг (изначально = 1)

# for num in range (1, 10, 2):
#     print(num)

# диапазон задом-наперед (только в этом случае start > stop)
# for num in range (20, 1, -1):
#     print(num)

# задача: вывести все числа всего диапазона (пользователь вводит)

# start = int(input("Введите начало диапазона: "))
# stop = int(input("Введите конец диапазона: "))
#
# for user_num in range(start, stop + 1):
#     print(user_num)
#
# # посчитать количество чисел в нём
#
# # счётчик чисел
#
# counter = 0
#
# # посчитать сумму чисел
#
# total = 0
#
# for num in range(start, stop+1):
#     counter += 1
#     total += num
#
# print(f"количество чисел {counter}")
#
# print(f"сумма чисел {total}")



# Строки (str, тексты, последовательность символов)


# """text""" - используется для большого количества строк в одной строке кода

# Кавычки как символы

# text = "Vlad's"
# text = 'Vlad\'s'

# Символ перехода на новую строчку
# text = 'Hello, how\nare you?'
# print(text)


# Конкатенация (объединение)

# word1 = 'privet'
# word2 = 'kak'
# word3 = 'dela'
#
# text = word1 + ' ' + word2 + ' ' + word3

# так же с += -=


# дублирование

# word = 'hello'
# text = 5 * word
# print(text)


# str в цикле for

# for num in range(1, 5):
#     print(num)
#
# text = 'Hello, world!'
# for symbol in text:
#     print(symbol)
#
# for symbol in 'abcd':
#     print(symbol)


# Операции

# Длина строки (количество символов)

# text = 'abcd'
#
# num_symbols = len(text)
# print(num_symbols) # 4


# Методы

# <название переменной>.<название метода>()

# text = 'hello'

# Посчитать количество какого-то символа

# res = text.count('l') // 2
# print(res)

# Так же с последовательностью символов

# Регистр (верхний и нижний)

# text = 'Yo wass UP m4n?!'
#
# lower_text = text.lower()
#
# print(lower_text) # yo wass up m4n?!
#
# lower_text = text.upper()
#
# print(lower_text) # YO WASS UP M4N?!


# Замена символов

# text = 'a big RED fox IS eating 23 red apples'
#
# # Заменить слово red на blue
#
# new_text = text.replace('red', 'blue')
#
# print(new_text) # a big RED fox IS eating 23 blue apples
#
# print('apple' in text) # True
#
# if 'apple' in text:
#     print('Слово cat есть в тексте')
# else:
#     print('Слова cat нет в тексте')
#
#
# # есть ли все символы в конкретном регистре
#
# text = 'hello123'
#
# if text.islower():
#     print('нижний регистр')
# else:
#     print('верхний регистр')
#
#
# # все ли символы буквы
#
# print(text.isalpha()) # False
#
# # все ли символы цифры
#
# print(text.isdigit()) # False


# 28.05

# https://www.ascii-code.com/

# ascii

# Получить код символа

# sym = 'g'
#
# ascii_code = ord(sym)
# print(ascii_code)
#
# # Получить символ по коду
#
# symbol = chr(61)
# print(symbol)
#
# # Сравнение символов по коду
#
# sym1 = 'Vlad'
# sym2 = 'Liza'

# if sym1 < sym2: #ord(sym1) < ord(sym2)
#     print(f'{sym1} Находится в таблице раньше, чем {sym2}')
# else:
#     print(f'{sym2} Находится в таблице раньше, чем {sym1}')


# Синтаксис функции print

# help(print)

# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.


# индексация

# text = 'abcde'
#
# # <название переменной>[<индекс>]
#
# index = len(text) - 1 # Последний символ
# sym = text[index]
#
# print(sym)

# Индексация начинается с нуля (как и во всех языках программирования)


# text = 'abcde'

# # цикл обычный
# for sym in text:
#     print(sym, end = ' ')
# print()

# =====

# цикл с индексацией
# for i in range(len(text)):
#     sym = text[i]
#     print(sym, end=' ')
# print()



# отрицательный индекс i-ый с конца

# text = 'abcde'
#
# i = -2 # 'd'


# слайс

# text[start:end:step]
#
# text = 'Hello, world!'
#
# print(text[2:6]) # вывести символы со 2-го индекса по 6-ой
# print(text[2:]) # конец по умолчанию - конец строки
# print(text[:2]) # первые два символа
# print(text[-2:]) # от второго с конца до самого конца
# print(text[:]) # вся строка (например для копии)
# print(text[2:8:2]) # символы со 2-го индекса до 8-го с шагом 2
# print(text[::2]) # каждый второй символ
# print(text[::-1]) # строка задом-наперед
# print(text[:100]) # все равно напечатает, но
# print(text[100]) # ошибка
#
# # методы
#
# index = text.index('w')
# print(index)

# help(input)


# # списки
#
# # text = "anjfl123456"
# #
# # list_num = [15, 12, -8, 3]
# #
# # # створення
# # # nums
# # # prices
# # # ages
# # # years
# #
# # nums = [1, 2, 3, 4]
# # nums = [] # порожній список
# # nums = [10]  # список з одним елементом(10)
# #
# # # конвертація типів даних
# # # age = int(input())
# # # age = int('25')
# #
# # nums = list(range(10, 20))
# # print(nums)
# #
# symbols = list("hello, world!")
# print(symbols)
#
#
# # # створіть список з числами від 1 до 5,
# # # але помножте їх на 4
# # # [4, 8, 12, 16, 20]
# #
# # nums = []
# #
# # for num in range(1, 5+1):
# #     nums.append(num*4)  # добавити елемент в кінець списку
# #
# # print(nums)
# #
# # # генератор списків
# #
# # # list = [<вираз що добавити> for <змінна> in <інша послідовність> ]
# # nums = [num*4 for num in range(1, 5+1)]
# #
# # print(nums)
#
# # індексація
#
# nums = [15, 20, 18, -65]
#
# # print(nums[0]) # перший елемент -- 15
# # print(nums[2])
# # print(nums[-1]) # останній елемент
# # print(nums[-3]) # третій елемент з кінця
#
# # print(nums[1:3])
# # print(nums[:2])  # перші 2 елемента
# # print(nums[-2:])  # останні 2 елемента
# # print(nums[::-1])  # крок -1, вивести задом наперед
#
# nums = [8, 7, 15, 10]
#
# # проходження по всіх індексах
# for i in range(len(nums)):
#     print(nums[i])
#
# # вивести всі елементи крім 3 очтанніх
# for i in range(len(nums)-3):
#     print(nums[i])

# зміни елементів за індексом
# text = 'hello'
# # text[2] = '*'
# print(text[:1] + '*' + text[2:])

nums = [15, 20, 18, 9]

# # змінити елемент з індексом 3
# #nums[3] = -1
# nums[3] *= 10
#
# print(nums)

# nums = [15, 20, 18, 9]
# # збільшити кожен елемент списку на 10
#
# positive_nums = []
#
# for num in nums:
#     print(num)
#     num = num + 10
#
# for i in range(len(nums)):
#     nums[i] += 10
#
# print(nums)


# методи
# nums = [15, 20, 18, 9, 20]
#
# # довжина(кількість елементів)
# len(nums)

# # добавити елемент в кінець списку
# nums.append(100)
# print(nums)

# # добавити елемент на будь-яке місце
# nums.insert(0, 100)
# print(nums)

# # видалити елемент
# nums.remove(20)
# print(nums)

# # видалити елемент за індексом
# nums.pop(2)
# print(nums)

# count
# index


# # перевірка чи є елемент в списку
# if 20 in nums:
#     print('20 є в списку')
# else:
#     print('20 немає в списку')




# Зарплата менеджера становить 200$ + відсоток від продажу:
# продаж до 500$ –3%, 500 –1000$ – 5%, понад 1000$ – 8%.
# Користувач вводить з клавіатури рівень продажу для трьох
# менеджерів. Визначте їхню зарплату, а також найкращого
# менеджера, нарахуйте йому премію 200$ та виведіть підсумки на
# екран.


# Користувач вводить з клавіатури рівень продажу для трьох менеджерів.

# sales = []
# for i in range(3):
#     manager_sale = int(input("Введіть продажі для менеджера: "))
#     sales.append(manager_sale)
#
# # список зарплат менеджерів
# salaries = [200, 200, 200]
#
# # нарахування відсотків
# for i in range(len(salaries)):
#     # отримати рівень продаж для і-го менеджера
#     manager_sale = sales[i]
#
#     # відсоток
#     if manager_sale < 500:
#         percent = 3
#     elif 500 <= manager_sale < 1000:
#         percent = 5
#     else:
#         percent = 8
#
#     # змінюємо зарплату менеджера
#     #salaries[i] += salaries[i]*percent/100
#     salaries[i] *= 1 + percent / 100
#
# #найкращого менеджера, нарахуйте йому премію 200$
#
# # максимальні продажі
# max_sale = max(sales)
#
# for i in range(len(salaries)):
#     # перевіряємо чи продав цей менеджер найбільше
#     if sales[i] == max_sale:
#         salaries[i] += 200
#
# print(salaries)


# 04.06.2025


# nums = [10, 12, 20, 5, 12]
#
# ind = int(input("Введіть індекс числа: "))
#
#
# if 0 <= ind < len(nums):
#     print(nums[ind])
# else:
#     print("індекс неправильний")

# список рядків

# fruits = ['apple', 'pear', 'kiwi']

# ind = int(input("Введіть індекс фрукта: "))
#
# if 0 <= ind < len(fruits):
#     print(fruits[ind])
# else:
#     print("індекс неправильний")

# fruit = input("Введіть назву фрукта")
#
# if fruit in fruits:
#     ind = fruits.index(fruit)
#     print(ind)
# else:
#     print("Такого фрукта немає в списку")


# # зрізи
#
# text = 'hello'
# char = 'e'
#
# print(text[0])   # 1 символ
# print(type(text[0]))
# print(text[:1])  # 1 символ
# print(type(text[:1]))
#
# nums = [1, 2, 3, 4]
# print(nums[0])  # число
# print(nums[:1]) # список з одним елементом
#
# num = nums[0]
# print(type(num))
# print(num + 10)
#
# num = nums[:1]
# print(type(num))
# print(num + 10)


# списки рядків

# text = 'apple, banana, kiwi, pear'
#
# # ріже текст на частини
# parts = text.split(", ")
#
# print(type(parts))
# print(parts)

# words = input("Введіть слова через пропуск ").split()


# # замінити в кожному слові букву а на А
# for i in range(len(words)):
#     words[i] = words[i].replace('а', "A")
#     word = words[i]
#
#     print(word)
#
# print(words)

# # вивести слова які мають менше 4 символів
# for word in words:
#     if len(word) < 4:
#         print(word)

# # вивести слова які написані в нижньому регістрі
# for word in words:
#     if word.islower():
#         print(word)

# for num in nums:
#     pass
#
# for user in users:
#     pass

# замінити слова написані в нижньому регістрі на stop
# for i in range(len(words)):
#     # word = words[i]
#     #
#     # if word.islower():
#     #     words[i] = 'stop'
#
#     if words[i].islower():
#         words[i] = 'stop'
#
#
# # об'єднати слова в текст через ', '
# text = ', '.join(words)
# print(type(text))
# print(text)
#
# # сортування
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
# ]
#
# salaries = [
#     3000, 3100, 2200, 2300, 2400, 2000,
#     1900, 2000, 2500, 2600, 2700, 3200
# ]
#
# salaries.sort(reverse=True) # від бульшого до меншого
# print(salaries)
#
# months.sort()
# print(months)






# # Є два списки: назви місяців та зарплата співробітника.
# # Користувач вводить назву місяця. Ввиведіть зарплату
# # за цей місяць
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
# ]
#
# salaries = [
#     3000, 3100, 2200, 2300, 2400, 2000,
#     1900, 2000, 2500, 2600, 2700, 3200
# ]
#
# while True:
#     # інструкція
#     print("Введіть один з місяців або END для закінчення")
#     print("  ".join(months))
#
#     # введення даних
#     month = input('Введіть назву місяця: ').strip()
#
#     # strip -- видаляє лишні пропуски на початку та вкінці
#
#     # перевірка чи кінець
#     if month == "END":
#         break
#
#     # отримуємо перші 3 літери
#     month = month[:3].capitalize()
#
#     # чи правильний місяць
#     if month not in months: # якщо неправильний, починаємо заново
#         print("Неправильна назва місяця")
#         print()
#         continue
#
#     # вивід даних
#     ind = months.index(month)
#
#     salary = salaries[ind]
#
#     print(f'Зарплата за {month} -- {salary}')
#     print()



# итерация - один круг в цикле

# iterable - то, что можно поместить в цикл for (range, list, str etc)

# break - остановить все итерации
# continue - перейти на новые итерации


# функції

# print("Hello")
# print("Програма працює")

# # визначення функції
# # def <назва функції>(параметри):
# def my_func():
#     print("Hello")
#     print("Програма працює")
#
# # виклик функції
# # <назва функції>(параметри)
# my_func()
#
# print('-----------')
#
# my_func()

# параметри функції

# # функція яка показує суму чисел
# # def <назва функції>(параметр1, параметр2, ...):
# def show_sum(num1, num2):
#     summa = num1 + num2
#     print(f"{num1} + {num2} = {summa}")
#
#
# show_sum(2, 8)
# show_sum(10, 12)
#
# a = 25
# b = 17
# show_sum(a, b)


# # Напишіть функцію, яка приймає два числа як параметри та
# # відображає всі числа між ними.
#
# def show_range(start, end):
#     for num in range(start, end+1):  # кінець включно
#         print(num, end=' ')  # числа через пропуск
#
#     print()  # в кінці перехід на новий рядок
#
#
# show_range(1, 10)
# show_range(100, 105)
#
# end = 20
# show_range(1, end)
# show_range(1, end-5)

# # Напишіть функцію, яка відображає горизонтальну або
# # вертикальну лінію. Функція має приймати 3 параметри:
# # довжину лінії, символ для заповнення та логічну змінну:
# #  Якщо вона рівна True, то лінія горизонтальна
# #  Якщо False, то лінія вертикальна
#
# def draw_line(length, symbol, is_horizontal):
#     # горизонтальна лінія
#     if is_horizontal:
#         print(symbol*length)
#     else:
#         # вертикальна
#         for i in range(length):
#             print(symbol)
#
#
# draw_line(5, '-', True)
# draw_line(3, '*', False)


# функція яка рахує суму чисел

# def get_sum(a, b):
#     res = a + b
#
#     # повертає результат
#     return res
#
#
# # text = input('Введіть текст')
# # res = min(1, 2)
#
# summa = get_sum(2, 7)
# print(summa)
# # перевірка типів даних
#
# # def get_sum(num1, num2):
# #     # перевірка що num1 типу int або float
# #     if not isinstance(num1, (int, float)):
# #         print('Неправильний тип даних')
# #         return
# #
# #     if not isinstance(num2, (int, float)):
# #         print('Неправильний тип даних')
# #         return
# #
# #     result = num1 + num2
# #
# #     return result
# #
# #
# # print(get_sum(2.5, 3))
# # print(get_sum('text1', '  text2'))
# # print(get_sum(2, '3'))
#
# # декілька значень в return
#
# def statistics(num1, num2):
#     min_num = min(num1, num2)
#     max_num = max(num1, num2)
#     mean = (num1 + num2) / 2
#
#     return min_num, max_num, mean
#
#
# # result = statistics(2, 3)
# # print(result)
# # print(type(result))
# #
# # print(result[0])
# # print(result[-1])
#
# # min_num, max_num, mean = statistics(2, 5)
# #
# # print(max_num)
#
# # text1, text2, text3 = 'dog'
# # a, b, c = 1, 2, 10
# #
# # print(b)
#
# # # якщо потрібно не все
# # # _ -- змінна для зберігання непотребу
# #
# # _, _, mean = statistics(2, 5)
# # _, max_, _ = statistics(2, 5)
# # min_, _, mean = statistics(2, 5)
# #
# # _, _, _ = statistics(2, 5)
# # statistics(2, 5)
# #
# # #res = 2 + 3*10
# # print(_)
# #
# # # for _ in range(10):
# # #     print('hello')
#
# # параметри за замовчування
#
# # def get_sum(num1=10, num2=10):
# #     print(f"{num2 = }")
# #     return num1 + num2
# #
# #
# # print(get_sum(2, 3))
# # print(get_sum(2))
# # print(get_sum())
#
# # функція перевіряє чи є текст реченням, тобто
# # закінчується на певний символ(за замовчуванням .)
#
# # def is_sentence(text, symbol='.'):
# #     # text -- позиційний
# #     # symbol -- іменний
# #
# #     # позиційні параметри МАЮТЬ йти першими
# #
# #     return text + symbol
# #
# # user_text = 'hello.'
# #
# # print(is_sentence(user_text, symbol='?'))
# # print(is_sentence(user_text, '?'))
# # print(is_sentence(text=user_text, symbol='?'))
# # print(is_sentence(symbol='?', text=user_text))
# # # print(is_sentence(symbol='?', user_text))  # Помилка
# #
# # print(is_sentence(user_text))
# # print(is_sentence(text=user_text))
#
#
# # def func(num, nums=[]):
# #     nums.append(num)
# #
# #     print(nums)
# #     return len(nums)
# #
# # func(1)
# # func(2)
# # func(3)
#
# # def func(num, nums=None):
# #     if nums is None:
# #         nums = []
# #
# #     nums.append(num)
# #
# #     print(nums)
# #     return len(nums)
# #
# # func(1)
# # func(2)
# # func(3)
#
#
#
# # # Функція рахує добуток чисел з списку та, якщо вказати,
# # # виводить інформацію про свою роботу
#
# # def product(nums, verbose=False):
# #     # перевірка типів даних
# #     if not isinstance(nums, list):
# #         print("Ви маєте передати список чисел")
# #         return
# #
# #     if not isinstance(verbose, bool):
# #         print("verbose має бути типу bool")
# #         return
# #
# #     res = 1
# #
# #     for num in nums:
# #         # елементи списку числа
# #         if not isinstance(num, (int, float)):
# #             print("елементи списку мають бути числами")
# #             return
# #
# #         res *= num
# #
# #     # чи треба виводити результат
# #     if verbose:
# #         print(f"Добуток чисел рівний -- {res}")
# #
# #     return res
# #
# # #print(product([1, 2, 3, 4]))
# # #print(product([1, 2, '3', 4]))
# # print(product([1, 2, 3, 4], True))
# # print(product([1, 2, 3, 4], verbose=True))
# # print(product([1, 2, 3, 4], verbose=False))
# # print(product([1, 2, 3, 4], verbose='true'))
# # print(product('123', verbose='true'))
# # print(product(verbose=True, nums=[1, 2, 3, 4]))
#
#
#
# # # Функція отримує ціну товару, податок(за замовчуванням 0.20)
# # # та знижку(за замовчуванням 0). Поверніть кінцеву ціну
#
#
# def get_price(price, tax=0.2, discount=0, is_percentage=False):
#     # перевірки
#     if not isinstance(price, (int, float)) or price < 0:
#         print("Ціна має бути дадатнім числом")
#         return
#
#     if not isinstance(tax, (int, float)) or not (0 <= tax <= 100):
#         print("Податок має бути числом в діапазоні [0, 100]")
#         return
#
#     if not isinstance(discount, (int, float)) or not (0 <= discount <= 100):
#         print("Знижка має бути числом в діапазоні [0, 100]")
#         return
#
#     # робота з відсотками
#     if is_percentage:
#         tax /= 100
#         discount /= 100
#
#     # основна програма
#
#     price *= (1 + tax)  # нарахування податку
#     price *= (1 - discount)  # знижка
#
#     return price
#
#
# # print(get_price(100))
# # print(get_price(100, 0.5))
# # print(get_price(100, 0.5, 0.2))
# print(get_price(100, tax=0.5, discount=0.2))
# print(get_price(100, discount=0.2, tax=0.5))
# print(get_price(100, discount=20, tax=50, is_percentage=True))
# print(get_price(-100, discount=0.2, tax=0.5))


# DRAW = 'нічия'
# CROSS = 'X'
# ZERO = 'O'
#
#
# def create_field():
#     pass
#
#
# def symbol_choice():
#     pass
#
#
# def make_move(name, symbol, field):
#     pass
#
#
# def show_field(filed):
#     pass
#
#
# def check_winner(field):
#     pass
#
#
# def main():
#     pass
#
# Anton, [23.06.2025 19:11]
# # гра хрестики нулики
#
# DRAW = 'нічия'
# CROSS = 'X'
# ZERO = 'O'
# EMPTY_SYMBOL = '_'
#
#
# def create_field():
#     pass
#
#
# def symbol_choice():
#     pass
#
#
# def make_move(name, symbol, field):
#     pass
#
#
# def show_field(filed):
#     pass
#
#
# def check_winner(field):
#     pass
#
#
# def main():
#     pass
#
# Anton, [23.06.2025 19:12]
# main:
#   Патора Олексій Валерійович
#   Пентюхов Никита Владимирович
#   Бондаренко Олексій Анатоліович
# create_field:
#   Ткачук Владислав Максимович
#   Потерейко Володимир Іванович
# symbol_choice:
#   Шапошников Олександр Сергiйович
#   Рекуненко Микола Миколайович
# make_move:
#   Мовчан Захар Олександрович
#   Нашкородов Артем
# show_field:
#   Адєлартей Еммануель Адевунмі
#   Марущак Давид Сергеевич
# check_winner:
#   Токар Сергій Володимирович
#   Вельможний Тарас Володимирович

# # гра хрестики нуликиDRAW = 'нічия'CROSS = 'X'ZERO = 'O'EMPTY_SYMBOL = '_'def create_field():    passdef symbol_choice():    passdef make_move(name, symbol, field):    passdef show_field(filed):    passdef check_winner(field):    passdef main():    pass

# def create_field():
#     field = []
#
#     raw_template = [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL]
#
#     for _ in range(3):
#         field.append(raw_template.copy())
#
#     return field # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
#
# CROSS = 'X'
# def symbol_choice():
#     user_name = input('Введите имя: ')
#     symbol = input('Введите символ: ')
#
#     user_name1 = input('Введите имя: ')
#     symbol1 = input('Введите символ: ')
#
#     user = [user_name, symbol]
#     user1 = [user_name1, symbol1]
#
#
#     if user[1] == user1[1]:
#         if user_name > user_name1:
#             user[1] = CROSS
#         else:
#             user1[1] = CROSS
#
#     print(user, user1)
#
#
# symbol_choice()


# модули AKA библиотеки AKA фреймворки

# подключение модуля (импортирование)

# import module

# функция из модуля

# название модуля.название функции
# import random
# print(random)
#
# if __name__ == '__main__': # вписать 'main'

# встроенные модули

# import time # количество секунд с 1 января 1970 года 00:00:00 (UTC)
#
# start = time.time()
#
# count = 0
#
# for i in range(1000000000):
#     count += 1
#
# end = time.time()
#
# duration = end - start
#
# print(duration) # 56.81556510925293

# декоратори

# функція як об'єкт

# def func():
#     num = 10
#
#     print("hello")
#
#     return 5
#
# text = 'start'

# # присвоєння
# # new_func --  це те що в return
# new_func = func()
#
# print(new_func)
#
# # new_func --  це саме функція func
# new_func = func
# print(new_func)
#
# # new_func = func
# #
# # new_func()
# #
# # my_print = print
# # my_print(1, 2, 3, sep=' ')
# #
# # # func = 2
# # # func()
# #
# # # ось так ви втрачаєте доступ до функцій
# # min = 10
# # str = 'jkl'


# # список функцій
# def mean(num1, num2):  # середнє арифметичне
#     return (num1 + num2) / 2
#
#
# # список функцій
# funcs = [min, max, mean]
#
# for func in funcs:
#     result = func(10, 20)
#
#     # назва функції
#     name = func.__name__
#
#     print(f"{name}(10, 20) = {result}")


# функція як аргумент(параметр) іншої функція

# def func(num, text):
#     print(f"{num}, {text}")
#
#
# func(1, 'text')

# функція яка застосовує іншу функцію до 10, 20
# def apply_func(func):
#     result = func(10, 20)
#     print(result)
#     return result
#
#
# apply_func(max)

# отримати найкоротше слово зі списку слово

words = ['apple', 'banana', 'cat', 'zone']

# res = min(words, key=len)
# print(res)
#
# res = max(words, key=len)
# print(res)
#
# res = sorted(words, key=len)
# print(res)

# знайти слово в якому найбільше літер a

# функція яка рахує кількість a
def count_a(word):
    return word.count('a')


# res = max(words, key=count_a)
# print(res)

# інший спосід через lambda функцію
# def [назва](парам1, парам2, ..):
#     return [результат]

# lambda функція або анонімна функція
# key = lambda парам1, парам2, ..: результат

# res = max(words, key=lambda word: word.count('a'))
# print(res)
#
# key=lambda word: word.count('a')
# print(key('banana'))

# # відсортувати числа по їхнім квадратам
# nums = [1, 4, -2, 5, 6, -3]
#
# res = sorted(nums, key=lambda num: num**2)
# print(res)


# # алфавітний порядок
# "автобус" < "ананас"
# print([1, 3] < [1, 10])
#
# # відсортувати числа по їхнім квадратам, якщо вони
# # однакові тоді за самим числами
# nums = [-1, 1, 4, 2, -2, 5, 6, -3, -5]
#
# res = sorted(nums, key=lambda num: [num**2])
# print(res)
#
# res = sorted(nums, key=lambda num: [num**2, num])
# print(res)

# фільтрування
# дістати лише додатні числа зі списку
#
# nums = [-1, 1, 4, 2, -2, 5, 6, -3, -5]
#
# # filter(функція, послідовність)
# # функція має повертати True False
# func = lambda num: num > 0
# res = filter(func, nums)
#
# # перевечти результат в список
# res = list(res)
#
# print(res)

# як працює filter
# def my_filter(func, items):
#     new_items = []
#
#     for item in items:
#         if func(item):
#             new_items.append(item)
#
#     return new_items
#
#
# # надати функції яка отримує одне число властивіть: тепер вона отримує
# # список чисел і застосовується до кожного числа зі списку
#
# def list_decorator(func):
#     def new_func(nums):  # нова функція з новою властивістю
#         new_nums = []
#
#         for num in nums:
#             res = func(num)  # застосовуємо оригінальну функцію
#             new_nums.append(res)
#
#         return new_nums
#
#     return new_func
#
#
# @list_decorator
# def mult2(num):
#     return num*2
#
#
# #new_func = list_decorator(mult2)
#
# nums = [1, 2, 3, 4, 5]
# res = mult2(nums)
# print(res)

# # функція map
# # користувач вводить числа через кому, вивести їхню суму
#
# nums = input("Введіть числа через кому: ").split(', ')
#
# print(nums)
#
# # цикл for
# new_nums = []
# for num in nums:
#     new_nums.append(int(num))
#
# print(new_nums)
#
# # генератор
# # new_list = [item for...]
# new_nums = [int(num) for num in nums]
#
# # map
# new_nums = map(int, nums)
# new_nums = list(new_nums)
#
# print(new_nums)
#
# # об'єднати в один рядок
# new_nums = list(map(int, input("Введіть числа через кому").split(', ')))
#
# for num in new_nums:
#     print(num)

# кортежі
# # кортеж -- список, але без змін
# nums = [1, 2, 3]
# nums[1] = 100
# print(nums)

# # кортеж -- tuple
# nums = (1, 2, 3)
# print(nums)
# print(nums[1])

# # не можна вносити зміни
# nums[1] = 100

# методи count та index

# # проятись по циклу
# for num in nums:
#     print(num)
#
# for i in range(len(nums)):
#     print(nums[i])

# # зрізи
# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# print(nums[2:5])  # числа між індексом 2 та 5(не включно)
# print(nums[:4])  # перші 4 числа
# print(nums[-4:])  # останні 4 числа
# print(nums[-1])  # останній елемент
# print(nums[::-1])  # обернений порядок

# # створення кортежів
#
# words = ("pen", "pencil", "chalk")
# words = ("pen",)  # кортеж з одного елемента
# words = tuple()  # порожній кортеж
#
#
# print(type(words))
# print(words)
#
# # зміна типів даних
# result = tuple('apple')
# result = tuple(range(10))
#
# nums = [4, 5, 6, 2, 3]
# result = tuple(nums)
#
# print(result)
#
# # об'єднати елементи кортежу в str
# leters = ('a', 'p', 'p', 'l', 'e')
#
# result = ', '.join(leters)
# print(result)

# змінювальні типи даних -- list, set, dict
# незмінювальні -- int, float, str, tuple

# # присвоювання через розпаковку
# nums = (4, 5, 2)
#
# a, b, c = nums
#
#
# print(a)
# print(b)
# print(c)

# data = [
#     ('Ukraine', "Kyiv", 30),
#     ("Spain", "Madrid", 45),
#     ("UK", "London", 50)
# ]

# порахувати загальне населення та вивести всю інформацію
#
# total = 0
# for state, capital, population in data:
#     #state, capital, population = country
#     total += population
#     print(f"{state}: Столиця {capital}. Населення {population} млн")
#
# print(f"Загальне населення країн {total} млн")
#
# # інший варіант(генератор)
# total = sum(population for _, _, population in data)
# total = sum(country[-1] for country in data)
#
# print(f"Загальне населення країн {total} млн")

# # якщо з кортежа потрібно не все
# data = ('Ukraine', "Kyiv", 30)
#
# state, _, population = data
# _, capital, population = data

# отримання індекса та елемента послідавності

# words = ["apple", 'banana', 'kiwi', 'pear']
#
# # # цикл з індексом
# # for i in range(len(words)):
# #     word = words[i]
# #
# #     print(f"{i}. {word}")
#
# # # enumerate
# # for i, word in enumerate(words, start=1):  # індексація з 1
# #     print(f"{i}. {word}")
#
# # zip -- отримати пари з декількох списків
# items = ["apple", 'banana', 'kiwi', 'pear', "hgljhljhj"]
# prices = [20, 40, 50]
quantities = [2.5, 0.75, 0.5, 1.5]

# for item, price, quantity in zip(items, prices, quantities):
#     print(f"{item} -- загальна ціна {price*quantity}")

# for data in zip(items, prices, quantities):
#     print(data)

# # enumerate
#
# fruits = ['banana', 'apple', 'pear']
#
# for i, fruit in enumerate(fruits):
#     print(f"Індекс: {i}  елемент: {fruit}")
#
#
# for i in range(len(fruits)):
#     fruit = fruits[i]
#
#     print(f"Індекс: {i}  елемент: {fruit}")

# множини (set)
# list1 = [1, 2, 3, 4]
# tuple1 = (1, 2, 3, 4)
# set1 = {1, 2, 3, 4}  # Shift + [

# # порожня множина
# # set1 = {}  # не працює, це не множина а словник
# set1 = set()
# print(type(set1))


# # зміни типів даних
# list1 = [1, 2, 3, 4]
# set1 = set(list1)
#
# tuple1 = (1, 2, 3, 4)
# set1 = set(tuple1)
#
# set1 = set("hello")
# print(set1)
#
# set1 = set(range(1, 10))
# print(set1)

# # генератори
# set1 = {num for num in range(10)}
# print(set1)


# множина містить лише унікальні елементи(без повторень)
# set1 = {1, 1, 1, 4, 2, 2, 3, 4, 4, 1, 1, -100}

# print(set1)
# print(len(set1))

# мнодини не мають порядку, відповідно не мають індексів
# set1[0] -- помилка
# set1[1:3]

# # працює цикл for
# for item in set1:
#     print(item)

# # перевірка чи є елемент
# import time
#
#
# N = 10**7
# list1 = list(range(N))
# set1 = set(range(N))
#
# item = -1
#
# start = time.time()
# if item in list1:
#     pass
# end = time.time()
#
# print(f"Витрачено часу з list: {end - start}")
#
# start = time.time()
# if item in set1:
#     pass
# end = time.time()
#
# print(f"Витрачено часу з set: {end - start}")

# hash

# print(hash('apple'))
# print(hash('Apple'))
#
# set1 = {'apple', 'kiwi', 'pear'}
#
# print(hash((1, 2)))
# print(hash((1, 2, 3)))

# # хешуються лише незмінювальні типи даних
# # int, float, str, tuple
# nums = [1, 2]
#
# set1 = {nums, 12, 23}  # помилка
#
# if nums in set1:
#     pass
#
# nums.append(3)
#
# if nums in set1:
#     pass

# # операції
# set1 = {1, 2, 3}
#
# # перевірка си є елемент
# if 1 in set1:
#     pass
#
# if 2 not in set1:
#     pass
#
# # # добавити елемент
# # set1.add(4)
# # print(set1)
# #
# # set1.add(4)
# # print(set1)
#
# # # видалення елемента
# # set1.discard(2)
# # print(set1)
# #
# # set1.discard(-100) # немає помилки
# # print(set1)
#
#
# # операції з множинами
#
# workers = ["Анна", "Олег", "Ігор", "Олег", "Анна", "Марія", "Сергій", "Олег"]
# special_workers = ["Анна", "Ігор", "Вікторія"]  # працівники з особливим доступом
#
# workers = set(workers)
# special_workers = set(special_workers)
#
# # вивести усіх працівників
# # об'єднання множин
# #all_workers = workers.union(special_workers)
# all_workers = workers | special_workers
# all_workers = special_workers | workers
#
# print(all_workers)
#
# # вивести працівників які не мають спеціального доступу
# # різниця множин
# #no_special_workers = workers.difference(special_workers)
# no_special_workers = workers - special_workers
# print(no_special_workers)
#
# # інший результат
# # no_special_workers = special_workers - workers
# # print(no_special_workers)
#
# # перетин множин
# # елементи які є в обох одночасно
# #both = workers.intersection(special_workers)
# both = workers & special_workers
#
# print(both)


# словники

set1 = {'London', 'Kyiv'}
list1 = ['London', 'Kyiv']

items = ['молоко', 'яблуко']
prices = [30, 70]

# дані в словнику це пари(два знечення)
# key  value
# ключ та значення

prices = {
    'key': 'value',
    'молоко': 30,
    'яблуко': 70,
    'банани': 80
}

items[1] # елемент з індексом 1

# res = prices['яблуко']  # дістати значення за ключем 'яблуко'
# print(res)
#
# # ключі зберігаються так само як і в множинах, отже
# # 1 ключі будуть унікальні
# data = {
#     'молоко': 30,
#     'яблуко': 70,
#     'молоко': 80
# }
# print(data)
#
# # 2 ключі мають бути хешованими(незмінними)
# data = {
#     (1, 2): '',
#     'молоко': 30,
#     'яблуко': 70,
#     'молоко': 80
# }
#
# # значення -- обмежень немає
# data = {
#     'key1': 10,
#     'key2': 10,
#     'key3': [1, 2, 3, 4]
# }
#
# print(data)


# # створення
# # перерахувати всі пари у форматі ключ: значення
# data = {
#     'name': 'Anton',
#     'age': 25,
#     'email': 'anton@gail.com',
#     'grades': [12, 10, 11, 10]
# }
#
# # порожній словник
# data = {}
#
# # порожня множина
# set1 = set()
#
# # генератори
# list1 = [num*2 for num in range(10)]
# print(list1)
#
#
# items = ['молоко', 'яблуко', 'хліб']
# prices = [30, 70, 25]
# data = {item: price for item, price in zip(items, prices)}
#
# print(data)
#
# # зміни типів даних
# # помилка
# # list1 = [1, 2]
# # print(dict(list1))
#
# list1 = [
#     ('UK', 'London'),
#     ('France', 'Paris')
# ]
# print(dict(list1))
#
# print(dict(zip(items, prices)))

# операції

# data = {
#     'name': 'Anton',
#     'age': 25,
#     'email': 'anton@gail.com',
#     'grades': [12, 10, 11, 10]
# }
#
# # # перевірка чи є ключ
# #
# # if 'name' in data:
# #     print('є ключ name')
# # else:
# #     print('немає ключ name')
# #
# # # працює лише з ключами
# # if 'anton@gail.com' in data:
# #     print('є ключ anton@gail.com')
# # else:
# #     print('немає ключ anton@gail.com')
# #
# # # перевірити чи є таке значення
# # if 'anton@gail.com' in data.values():
# #     print('є значення anton@gail.com')
# # else:
# #     print('немає значення anton@gail.com')
#
# # використання ключа
#
# # res = data['email']
# # print(res)
# #
# # # res = data['location']  # помилка
# # # print(res)
# #
# #
# # res = data.get('location', 'зачення якщо ключа немає')
# # print(res)
# #
# # res = data.get('age', 'зачення якщо ключа немає')
# # print(res)
# #
# # res = data.get('location')
# # print(res)
#
# # print(data)
# #
# # # добавити нову пару ключ:значення
# # data['location'] = 'Kyiv'
# #
# # print(data)
# #
# # # змінити значення за ключем
# # data['location'] = 'Kharkiv'
# # data['age'] += 1
# # print(data)
# #
# # # видалення
# # grades = data.pop('grades')
# # print(grades)
# # print(data)
#
# # цикл for
#
# # for key in data:
# #     print(key)
# #
# # for key, value in data.items():
# #     print(f"{key} -- {value}")
# #
# # for value in data.values():
# #     print(f"{value}")
# #
# # for key in data:
# #     value = data[key]
# #
# #     print(value)
#
# # напишуть функцію яка створює словник з інформацією про працівника
# # (ім'я, зарплата, досвід)
# # напишуть функцію яка створює список з інформацією про співробітників
# # напишіть функцію яка збільшить зарплату працівникам які працюють більше 2 років
#
# def get_employee_info():
#     info = {}
#
#     info['name'] = input("Введіть ім'я: ")
#     info['salary'] = int(input("Введіть зарплату: "))
#     info['expirience'] = int(input("Введіть досвід: "))
#
#     return info
#
#
# def get_all_employee_info(count):
#     list_data = []
#     dict_data = {}
#
#     for _ in range(count):
#         info = get_employee_info()
#
#         list_data.append(info)
#
#         name = info.pop('name')
#         dict_data[name] = info
#
#     return dict_data
#
#
# def increase_salary(info):
#     for name in info:
#         # дані про співробітника name
#         data = info[name]
#
#         if data['expirience'] > 2:
#             data['salary'] += 1
#
#
#
# # #info = get_employee_info()
# # info = get_all_employee_info(3)
# #
# # # гарний вивід словників
# # import json
# #
# # print(json.dumps(info, indent=4))
#
#
# info = {
#     "Mary": {
#         "salary": 3000,
#         "expirience": 5
#     },
#     "Jhon": {
#         "salary": 2000,
#         "expirience": 1
#     },
#     "Anna": {
#         "salary": 15000,
#         "expirience": 10
#     }
# }
#
# for key in info:
#     print(key)
#
# print(info['Anna']['salary'])


# Є словник, де ключ — ім’я учня, а значення — множина гуртків,
# які він відвідує.
# Реалізуйте функціонал:
# 1 -- додати нового учня
# 2 -- додати новий гурток для учня
# 3 -- видалити гурток для учня
# 4 -- показати учнів які відвідують певний гурток(и)
# 5 -- для двох учнів показати гуртки які вони відвідують разом
# 6 -- вивести всю інформацію.
# 7 -- вивести усі згадані гуртки

# students_clubs = {
#     "Олег": {"Футбол", "Шахи", "Робототехніка"},
#     "Марія": {"Шахи", "Театр"},
#     "Іван": {"Футбол", "Програмування", "Робототехніка"},
#     "Софія": {"Малювання", "Театр"},
#     "Андрій": {"Програмування", "Шахи"},
#     "Катерина": {"Футбол", "Малювання"},
# }
#
#
# def get_student():
#     """
#     Отримати ім'я студента від користувача
#     """
#     while True:
#         student = input("Введіть ім'я студента: ").strip()
#         student = student.capitalize()  # зробити першу літеру великою
#
#         if len(student) == 0:
#             print('не може бути порожнім')
#             continue
#
#         if not student.isalpha():
#             print("мають бути лише літери")
#             continue
#
#         return student
#
#
# def get_club():
#     """
#     Отримати назву гуртка від користувача
#     """
#     while True:
#         club = input("Введіть назву гуртка: ").strip()
#         club = club.capitalize()  # зробити першу літеру великою
#
#         if not club:
#             print('не може бути порожнім')
#             continue
#
#         return club
#
#
# def add_new_student(students_clubs):
#     student = get_student()
#
#     if student in students_clubs:
#         print('такий студент вже є')
#         return
#
#     students_clubs[student] = set()
#
#
# def show_info(students_clubs):
#     print("Студенти та їхні гуртки")
#
#     for student, clubs in students_clubs.items():
#         print(f'\t{student}')
#         print('\tГуртки:')
#
#         if clubs:  # якщо не порожній
#             for club in clubs:
#                 print(f"\t\t{club}")
#         else:
#             print("\t\tНемає")
#
#         print()
#
#
# def add_new_club(students_clubs):
#     student = get_student()
#
#     if student not in students_clubs:
#         print("такого студента немає")
#         return
#
#     club = get_club()
#
#     if club in students_clubs[student]:
#         print('студент уже відвідує цей гурток')
#         return
#
#     students_clubs[student].add(club)
#
#
# def remove_club(students_clubs):
#     student = get_student()
#
#     if student not in students_clubs:
#         print("такого студента немає")
#         return
#
#     club = get_club()
#
#     if club not in students_clubs[student]:
#         print('студент не відвідує цей гурток')
#         return
#
#     students_clubs[student].remove(club)
#
#
# def attend_club(students_clubs):
#     club = get_club()
#     students = []
#
#     for student, clubs in students_clubs.items():
#         if club in clubs:
#             students.append(student)
#
#     if students:
#         for student in students:
#             print(f"\t{student}")
#     else:
#         print(f"Ніхто не відвідує гурток {club}")
#
#
# def attend_clubs(students_clubs):
#     target_clubs = set()
#     while True:
#         club = get_club()
#         target_clubs.add(club)
#
#         choice = input('чи закінчили вводити гуртки?(так/ні)').strip().lower()
#         if choice == 'так':
#             break
#
#     students = []
#
#     for student, clubs in students_clubs.items():
#         if clubs & target_clubs == target_clubs:
#             students.append(student)
#
#     if students:
#         for student in students:
#             print(f"\t{student}")
#     else:
#         print(f"Ніхто не відвідує ці гуртки {target_clubs}")
#
#
# def show_common_clubs(students_clubs):
#     # student1 = get_student()
#     # student2 = get_student()
#     #
#     # clubs1 = students_clubs[student1]
#     # clubs2 = students_clubs[student2]
#     #
#     # common_clubs = clubs1 & clubs2
#     #
#     # if common_clubs:
#     #     for club in common_clubs:
#     #         print(f'\t{club}')
#     # else:
#     #     print('немає спільних гуртків')
#
#     students = set()
#     while True:
#         student = get_student()
#         students.add(student)
#
#         choice = input('чи закінчили вводити імена?(так/ні)').strip().lower()
#         if choice == 'так':
#             break
#
#     student = students.pop()
#     common_clubs = students_clubs[student]
#
#     for student in students:
#         clubs = students_clubs[student]
#         common_clubs = common_clubs & clubs
#
#     if common_clubs:
#         for club in common_clubs:
#             print(f'\t{club}')
#     else:
#         print('немає спільних гуртків')
#
#
# def show_all_clubs(students_clubs):
#     all_clubs = set()
#
#     for clubs in students_clubs.values():
#         all_clubs = all_clubs | clubs  # union
#
#     if all_clubs:
#         for club in all_clubs:
#             print(f'\t{club}')
#     else:
#         print('немає інформації про гуртки')
#
#
# def main():
#     """
#     Головна функція яка запускає програму.
#     """
#
#     print("Меню")
#     print("1 -- додати нового учня")
#     print("2 -- додати новий гурток для учня")
#     print("3 -- видалити гурток для учня")
#     print("4 -- показати учнів які відвідують певний гурток(и) усі")
#     print("5 -- для двох учнів показати гуртки які вони відвідують разом")
#     print("6 -- вивести всю інформацію.")
#     print("7 -- вивести усі згадані гуртки")
#     print("8 -- вихід")
#
#     while True:
#         print()
#         choice = int(input("Введіть номер команди: "))
#
#         if choice == 1:
#             add_new_student(students_clubs)
#
#         elif choice == 2:
#             add_new_club(students_clubs)
#
#         elif choice == 3:
#             remove_club(students_clubs)
#
#         elif choice == 4:
#             attend_clubs(students_clubs)
#
#         elif choice == 5:
#             show_common_clubs(students_clubs)
#
#         elif choice == 6:
#             show_info(students_clubs)
#
#         elif choice == 7:
#             show_all_clubs(students_clubs)
#
#         elif choice == 8:
#             break
#
#         else:
#             print('Невідома команда')
#
#
# if __name__ == '__main__':
#     main()
# винятки

# # іноді зробити перевірку через if буває дуже складно
# str_num = input("Введіть число ")
#
# if str_num.isdigit():  # не враховує -123, +5, 456.7894
#     num = int(str_num)
#     print(num)
# else:
#     print("Введено не число")


# try:
#     # тут може виникнути помилка(виняток)
#     num = float(input("Введіть число "))
#     print(num)
# except ValueError:
#     print('ви ввели не число')
#     num = 0
#
# except ZeroDivisionError:
#     print('ділення на 0')
#     num = 0
#
# except Exception:  # обробка будь-якого винятку
#     print('помилка')
#     num = 0
#
#
# print('Кінець програми')
#
# if num > 0:
#     print("positive")
# else:
#     print('negative')

# if case == 1:
#     pass
# elif case == 2:
#     pass
# elif case == 3:
#     pass

# функція яка просить у користувача число
# def get_age():
#     while True:
#         try:
#             age = int(input('Введіть вік: '))
#         except Exception:
#             print('Ввели не число')
#             continue
#
#         if age < 0:
#             print('вік не може бути від\'ємним')
#             continue
#
#         return age
#
#
# age = get_age()
# print(age)


# Напишіть функцію, яка приймає список чисел і
# повертає їхнє середнє арифметичне.
# Обробіть можливий виняток, коли список порожній.


# def average(nums):
#     try:
#         total = sum(nums)
#         count = len(nums)
#         return total / count
#     except TypeError:
#         print("Помилка: не всі елементи є числами")
#         return None
#     except ZeroDivisionError:
#         print("Помилка: список порожній")
#         return None
#
#
# nums = [1, 23]
# res = average(nums)
# print(res)





# винятки у функціях

# def get_name():
#     name = input('Введіть ім\'я: ')
#
#     if name == '':
#         raise ValueError('ім\'я не може бути порожнім')
#
#     if not name.isalpha():
#         raise ValueError(f'ім\'я має містити лише літери: {name}')
#
#     return name
#
#
# try:
#     name = get_name()
#     print(name)
# except Exception as err:  # err = помилка
#     print(f'Помилка: {err}')






# Напишіть функцію, яка приймає список і елемент,
# який слід видалити зі списку. Обробіть можливий виняток,
# коли такого елементу немає у списку.


# def delete(items, item):
#     try:
#         items.remove(item)
#         print(f"Елемент {item} успішно видалено")
#     except ValueError:
#         print(f'Такого елементу немає в списку {item}')
#     except AttributeError:
#         print(f"Ви передали не послідовність або послідовність незмінна")
#     except Exception as err:
#         print(f"Помилка: {err}")
#
#
# delete([1, 2, 3], 'hello')
# delete(12, 1)





























