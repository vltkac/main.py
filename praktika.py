# # #1
# #
# # date = 2025
# #
# # age = int(input("Введите Ваш возраст "))
# #
# # user_age = date - age
# #
# # print(f"Ваш год рождения: {user_age}")
# #
# # #2
# #
# # length = float(input("Введите длину ребра куба "))
# #
# # volume = length ** 3
# #
# # print(f"Объем куба равен {volume}")
# #
# # #3
# #
# # number = float(input("Введите число "))
# #
# # percent = float(input("Введите процент, на который Вы хотите увеличить заданное число "))
# #
# # result = number * (1 + percent / 100)
# #
# # print(f"Результат {result:.6f}")
#
# # #4
# #
# # celoe = int(input("Введите целое число "))
# # drob = float(input("Введите дробное число "))
# #
# # summa = celoe + drob
# # multi = celoe * drob
# # ostatok = celoe % drob
# #
# # print(f"Сумма чисел = {summa}, cложение = {multi}, остаток = {ostatok}")
# #
# # #5
# #
# # radius = float(input("Задайте радиус круга "))
# #
# # area = 3.1415 * radius ** 2
# #
# # print(f"Площадь круга = {area:.2f}")
#
# #6
#
# # price = float(input("Введите цену кружки "))
# # budget = float(input("Введите Ваш бюджет "))
# #
# # cup_qty = budget // price
# #
# # print(f"Вы можете купить {cup_qty} кружку/ек")
#
# # 05.05
#
# # 1.1
#
# # number1 = int(input("Please submit a number: "))
# #
# # if number1 % 2 == 0:
# #     print(number1)
# #     print("Even number")
# #
# # else:
# #     print(number1)
# #     print("Odd number")
#
# # 1.2
#
# # number2 = int(input("Please submit a number: "))
# #
# # if number2 % 7 == 0:
# #     print(number2)
# #     print("Number is multiple 7")
# #
# # else:
# #     print(number2)
# #     print("Number is not multiple 7")
#
# # 2.3
#
# # number1 = float(input("Please submit first number: "))
# # number2 = float(input("Please submit second number: "))
# #
# # if number1 > number2:
# #     print(f"{number1} is max")
# #
# # elif number1 == number2:
# #     print("Numbers are equal (no max or min number)")
# #
# # elif number1 < number2:
# #     print(f"{number2} is max")
#
# # 2.4
#
# # number1 = float(input("Please submit first number: "))
# # number2 = float(input("Please submit second number: "))
# #
# # if number1 > number2:
# #     print(f"{number2} is min")
# #
# # elif number1 == number2:
# #     print("Numbers are equal (no max or min number)")
# #
# # elif number1 < number2:
# #     print(f"{number1} is min")
#
# # 3.5
#
# # number1 = float(input("Please submit first number: "))
# # number2 = float(input("Please submit second number: "))
# #
# # summa = number1 + number2
# # raznica = number1 - number2
# # srednee = (number1 + number2) / 2
# # multi = number1 * number2
# #
# # operation = int(input("Пожалуйста, выберите операцию: сумма, разница, среднее арифметическое, умножение (1 - 4) "))
# #
# #
# # if operation == 1:
# #     print(summa)
# #
# # elif operation == 2:
# #     print(raznica)
# #
# # elif operation == 3:
# #     print(srednee)
# #
# # elif operation == 4:
# #     print(multi)
# #
# # else:
# #     print("Wrong choice")
#
# # 3.6
#
# # usd = float(input("Введите сумму в долларах "))
# #
# # choice_currency = input("Пожалуйста, выберите валюту ")
# #
# # if choice_currency == "евро":
# #     eur_to_usd = float(input("Введите курс евро к доллару "))
# #     print(f"Ваша сумма в евро {usd * eur_to_usd}")
# #
# # elif choice_currency == "фунт":
# #     gbd_to_usd = float(input("Введите курс фунта к доллару "))
# #     print(f"Ваша сумма в фунтах {usd * gbd_to_usd}")
# #
# # elif choice_currency == "иена":
# #     eur_to_jpy = float(input("Введите курс иены к доллару "))
# #     print(f"Ваша сумма в иенах {usd * jpy_to_usd}")
# #
# # else:
# #     print("Неправильный выбор")
#
#
# # 2
#
# # price = float(input("Введите цену за единицу товара "))
# # qty = int(input("Введите количество единиц товара "))
# # age = int(input("Введите свой возраст "))
# #
# # check_summa = price * qty
# # skidka = 0.15
# #
# # if price > 0 and qty > 0 and age > 0:
# #
# #     if age < 18 or age > 65:
# #         print(f"Ваш чек со скидкой 15%: {check_summa - (check_summa * skidka)} грн")
# #
# #     else:
# #         print(f"Ваш чек {check_summa} грн")
# #
# # else:
# #     print("Введите правильное число")
#
# # 4
#
# # number = int(input("Введите целое число: "))
# #
# # # if type(number) == int: (ne nado)
# #
# # if number % 3 == 0 and number % 5 == 0:
# #     print("FizzBuzz")
# #
# # elif number % 3 == 0:
# #     print("Fizz")
# #
# # elif number % 5 == 0:
# #     print("Buzz")
#
# # 3 and 5
# item_price = float(input("Введите цену товара: "))
# item_qty = int(input("Введите количество товара: "))
#
# delivery_fee = 100
# discount = 0.12
#
# order_price = item_price * item_qty + delivery_fee
#
#
# if item_price >= 0 and item_qty >= 0:
#
#     promocode_choice = input("Есть ли у вас промокод на скидку (да/нет)? ")
#
#     if promocode_choice == "да":
#         promocode_verify = input("Введите промокод ")
#         if promocode_verify == "FREEBUY27":
#             order_price = order_price - (order_price * discount)
#             print(f"Стоимость вашего заказа с применением скидки 12 % - {order_price} грн")
#         else:
#             print("Промокод неверный")
#
#
#     elif order_price >= 1000 and promocode_choice == "нет":
#         delivery_fee = 0
#         order_price = item_price * item_qty + delivery_fee
#         print(f"Стоимость вашего заказа с бесплатной доставкой - {order_price} грн")
#
#     else:
#         print("Ответьте да или нет")
#
# else:
#     print("Введите корректные значения")
#
#
# budget = float(input("Введите свой бюджет "))
#
# if budget >= 0:
#
#     if budget >= order_price:
#         print("Заказ оплачен")
#         print(f"Денег осталось {budget - order_price} грн")
#
#     else:
#         print("Заказ не оплачен")
#         print(f"Для оплаты не хватает {order_price - budget} грн")
#
# else:
#     print("Введите корректное значение")
#
# from enum import unique
# from functools import total_ordering


# 6

# a = float(input("Введите первую сторону "))
# b = float(input("Введите вторую сторону "))
# c = float(input("Введите третью сторону "))
#
# if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
#     print("Да")
#
# else:
#     print("Нет")

# 7

# month = int(input("Введите количество месяцев "))
# tariff = input("Выбор тарифа: basic, pro, premium ")
#
# basic_cost = 100
# pro_cost = 200
# premium_cost = 300
# month_discount = 0.07
#
# if tariff != "basic" and tariff != "pro" and tariff != "premium":
#     print("Введите правильный тариф")
#
# if month > 0:
#
#     if month >= 12:
#
#         if tariff == "basic":
#             print(f"Сумма оплаты {(basic_cost * month) - (basic_cost * month * month_discount)} грн")
#
#         elif tariff == "pro":
#             print(f"Сумма оплаты {(pro_cost * month) - (pro_cost * month * month_discount)} грн")
#
#         elif tariff == "premium":
#             print(f"Сумма оплаты {(premium_cost * month) - (premium_cost * month * month_discount)} грн")
#     else:
#
#         if tariff == "basic":
#             month_discount = 0
#             print(f"Сумма оплаты {(basic_cost * month)} грн")
#
#         elif tariff == "pro":
#             print(f"Сумма оплаты {(pro_cost * month)} грн")
#
#         elif tariff == "premium":
#             print(f"Сумма оплаты {(premium_cost * month)} грн")
# else:
#     print("Введите верное количество месяцев")

# 8

# water = float(input("Введите температуру воды: "))
# air = float(input("Введите температуру воздуха: "))
#
# if water >= 20 and air >= water * 0.9:
#     print("Условия комфортные")
#
# else:
#     print("Условия некомфортные")
# 1
# salary = float(input("Введите зарплату "))
#
# if salary < 8000:
#     print("Зарплата слишком маленькая")
#
# else:
#     print("Зарплата удовлетворительная")

# 2

# week_day = input("Введите день недели: ")
#
# if week_day == "суббота" or week_day == "воскресенье":
#     print("Выходной день")
# else:
#     print("Будний день")

# 3

# age = int(input("Введите возраст: "))
#
# if age < 6:
#     print("Садик")
# elif 6 <= age < 11:
#     print("Начальная школа")
# elif 11 <= age < 18:
#     print("Средняя школа")
# elif 18 <= age < 22:
#     print("Университет")
# elif age >= 22:
#     print("Онлайн-курсы")

# 4

# month = input("Введите месяц: ")
# month_day = int(input("Введите число в месяце: "))
#
# if month == "Декабрь":
#     if month_day == 25:
#         print("Рождество")
#     elif month_day == 31:
#         print("Новый год")
#     else:
#         print("Обычный день")
# elif month == "Январь":
#     if month_day == 1:
#         print("Первый день в году")
#     else:
#         print("Обычный день")
# else:
#     print("Обычный день")

# 5

# age = int(input("Введите возраст: "))
#
# if age < 18:
#     print("Слишком молодой")
# else:
#     driver_license = input("У вас есть права? (да / нет) ")
#     if driver_license == "да":
#         print("Можно водить автомобиль")
#     elif driver_license == "нет":
#         print("Нельзя водить автомобиль")

# 7

# speed = float(input("Введите скорость: "))
#
# if speed > 90:
#     where = input("Вы едете на трассе или в городе? ")
#     if where == "трасса":
#         print("Предупреждение")
#     else:
#         print("Штраф")
# elif speed < 20:
#     car_age = int(input("Сколько лет машине? "))
#     if car_age > 15:
#         print("Купите новую машину")
#     else:
#         print("Поедьте на СТО")
# else:
#     print("Хорошей дороги!")

# 8

# air_temp = float(input("Введите температуру воздуха: "))
#
# if air_temp < 0:
#     if_snow = input("Идет ли снег? (да / нет) ")
#     if if_snow == "да":
#         print("Снегопад")
#     else:
#         print("Мороз")
# elif air_temp > 25:
#     vlaga = float(input("Введите показатели влажности в процентах: "))
#     if vlaga < 20:
#         print("Жарко и сухо")
#     elif vlaga > 75:
#         print("Жарко и душно")
#     else:
#         print("Комфортно для купания")
# elif 0 <= air_temp <= 10:
#     print("Прохладно")
# else:
#     print("Тепло")

# 9
#
# basic_manager_salary = 200
#
# manager1_sells = float(input("Введите продажи первого менеджера: "))
# manager2_sells = float(input("Введите продажи второго менеджера: "))
# manager3_sells = float(input("Введите продажи третьего менеджера: "))
#
# if manager1_sells < 500:
#     sells1_percent = 3
# elif 500 <= manager1_sells < 1000:
#     sells1_percent = 5
# else:
#     sells1_percent = 8
#
# if manager2_sells < 500:
#     sells2_percent = 3
# elif 500 <= manager2_sells < 1000:
#     sells2_percent = 5
# else:
#     sells2_percent = 8
#
# if manager3_sells < 500:
#     sells3_percent = 3
# elif 500 <= manager3_sells < 1000:
#     sells3_percent = 5
# else:
#     sells3_percent = 8
#
# manager1_total = basic_manager_salary + manager1_sells * sells1_percent / 100
# manager2_total = basic_manager_salary + manager2_sells * sells2_percent / 100
# manager3_total = basic_manager_salary + manager3_sells * sells3_percent / 100
#
# if manager1_total == max(manager1_total, manager2_total, manager3_total):
#     manager1_total += 300
# if manager2_total == max(manager1_total, manager2_total, manager3_total):
#     manager2_total += 300
# if manager3_total == max(manager1_total, manager2_total, manager3_total):
#     manager3_total += 300
#
# print(f"Зарплата первого менеджера {manager1_total:.2f} $")
# print(f"Зарплата второго менеджера {manager2_total:.2f} $")
# print(f"Зарплата третьего менеджера {manager3_total:.2f} $")

# 10


# zakuska = input("Выберите закуску: ")
# osnova = input("Выберите основное блюдо: ")
# desert = input("Выберите десерт: ")
#
# order = 0
#
# if zakuska == "салат":
#     order += 5
# elif zakuska == "суп":
#     order += 7
# elif zakuska == (""
#                  ""):
#     order += 0
#
# if osnova == "курица":
#     order += 10
# elif osnova == "рыба":
#     order += 12
# elif osnova == (""
#                 ""):
#     order += 0
#
# if desert == "мороженное":
#     order += 3
# elif desert == "фрукты":
#     order += 4
# elif desert == (""
#                 ""):
#     order += 0
#
# if order >= 20:
#     order *= 0.85
#     print(f"Сумма заказа со скидкой 15 % - {order} $")
#
# elif (zakuska == "салат" or zakuska == "суп") and (osnova == "курица" or osnova == "рыба") and (desert == "мороженное" or desert == "фрукты"):
#     order *= 0.9
#     print(f"Сумма заказа со скидкой 10 % - {order} $")
#
# elif zakuska == "суп" and osnova == "рыба":
#     print("Десерт в подарок!")
#     print(f"Сумма заказа {order} $")
#
# elif zakuska == "салат" and osnova == "курица":
#     print("Скидка на десерт - 2 $")
#     print(f"Сумма заказа {order} $")
#
# else:
#     print(f"Сумма заказа {order} $")

# 14.05.2025

# 1

# start = int(input("Введите начало: "))
# stop = int(input("Введите конец: "))
#
# for numbers in range(start, stop + 1):
#     print(numbers)

# 2

# start = int(input("Введите начало: "))
# stop = int(input("Введите конец: "))
#
# for numbers in range(start, stop + 1):
#     if numbers % 2 != 0:
#         print(numbers)

# 3

# start = int(input("Введите начало: "))
# stop = int(input("Введите конец: "))
#
# for numbers in range(start, stop + 1):
#     if numbers % 2 == 0:
#         print(numbers)

# 4

# start = int(input("Введите начало: "))
# stop = int(input("Введите конец: "))
#
# for numbers in range(start, stop - 1, - 1):
#     print(numbers)

# 5

# start = int(input("Введите начало: "))
# stop = int(input("Введите конец: "))
#
# if start > stop:
#     start, stop = stop, start
#
# for numbers in range(start, stop + 1):
#     if numbers % 2 != 0:
#         print(numbers)

# second part

# 1

# start = int(input("Введите число: "))
# stop = int(input("Введите число: "))
#
# counter = 0
# sum = 0
#
# for number in range(start, stop + 1):
#     sum += number
#     counter += 1
#
# print(sum)
# print(counter)
# print(sum / counter)

# 2

# user_number = int(input("Введите число: "))
#
# faktorial = 1
#
# for num in range(1, user_number + 1):
#     faktorial *= num
#
# print(faktorial)

# 3

# length = int(input("Введите длину линии: "))
#
# for line in range(length):
#     print("*")

# 4

# length = int(input("Введите длину линии: "))
# symbol = input("Введите символ: ")
#
# for line in range(length):
#     print(symbol)

# Завдання 1
# На вході програми маємо натуральне число n. Серед
# натуральних чисел менших ніж n, що діляться на 5 та не
# діляться на 10 знайти найбільше.

# n = int(input("Введите число: "))
#
# for num in range(1, n + 1):


# --------------------------------------------------------------------------------------------------------------------

# 19.05.2025

# Цикл while

# Пользователь должен ввести количество товара
# Количество единиц товара должно быть положительно

# item_count = -1
# while item_count < 0: # пока количество единиц товара неверно, продолжаем спрашивать пользователя
#     item_count = int(input('Введите количество товара: '))
#
# print(f'Вы ввели число {item_count}')

# Способ 2

# while True: # вечный цикл
#     item_count = int(input('Введите количество товара: '))
#
#     if item_count >= 0: # условие остановки
#         break # остановка цикла (может быть много)
#
# print(f'Вы ввели число {item_count}')

# pass - заглушка, чтобы не было ошибки

# continue - возвращаемся в самое начало цикла и продолжаем


# Завдання 1
# Користувач вводить свій вік та ім’я. Якщо вік менше 0 то
# спитати ще раз, поки буде правильним.
# Вивести привітання у форматі «Привіт, Джон. Тобі 42
# роки»

# while True:
#
#     age = int(input('Введите возраст: '))
#
#     if age < 0:
#         print('Введен неправильный возраст')
#         continue
#
#
#     name = input('Введите имя: ')
#
#     print(f'Привет, {name}. Тебе {age} лет')
#
#     break

# Завдання 2
# Користувач вводить числа, поки їхня сума не стане більше
# 100.
# В кінці програми покажіть суму всіх чисел.

# sum = 0
#
# while True:
#     num = float(input('Введите число '))
#     sum = sum + num
#
#     if sum > 100:
#         break
#
#
# print(f"Сумма всех чисел = {sum}")

# Завдання 3
# Користувач вводить оцінки студента, поки не введе -1.
# Після цього виведіть кількість оцінок та середню оцінку

# grade_sum = 0
# grade_counter = 0
#
# while True:
#     grade = int(input('Введите оценку: '))
#
#     if grade == -1:
#         break
#
#     grade_counter += 1
#     grade_sum += grade
#
#     grade_average = grade_sum / grade_counter
#
# print(f'Количество оценок {grade_counter}')
# print(f'Средняя оценка {grade_average}')

# Завдання 4
# Користувач вводить довжину в метрах. Покажіть її у
#  Ярдах(1 ярд = 0,9144 метра)
#  Футах(1 фут = 0,3048 метра)
# В кінці спитайте користувача чи продовжувати роботу
# програми


# while True:
#     metr = float(input('Введите длину в метрах: '))
#
#     yard = metr / 0.9144
#     fut = metr / 0.3048
#
#     print(f'Длина в ярдах = {yard}')
#     print(f'Длина в футах = {fut}')
#
#     user_choice = input('Хотите ли вы продолжить работу программы? (да/нет) ')
#
#     if user_choice == 'да':
#         continue
#     else:
#         break


# Завдання 5
# Напишіть простий калькулятор. Функціонал:
# 1. Сума
# 2. Різниця
# 3. Добуток
# 4. Вихід
# Користувач обирає дію, після чого вводить два числа. Тоді
# програма показує результат і продовжує працювати.
# Якщо вибрано вихід – програма зупиняє роботу.

# while True:
#
#     user_choice = int(input('Please choose operation: sum (1), difference (2), multiplication (3), shut down (4) '))
#     if user_choice == 1:
#         num1 = float(input('First number '))
#         num2 = float(input('Second number '))
#         summa = num1 + num2
#         print(f'Sum = {summa}')
#     elif user_choice == 2:
#         num1 = float(input('First number '))
#         num2 = float(input('Second number '))
#         diff = num1 - num2
#         print(f'Difference = {diff}')
#     elif user_choice == 3:
#         num1 = float(input('First number '))
#         num2 = float(input('Second number '))
#         mult = num1 * num2
#         print(f'Multiplication = {mult}')
#     elif user_choice == 4:
#         break
#     else:
#         print('Please choose 1-4')
#         continue

# Завдання 6
# Напишіть програму для підрахунку вартості товарів у
# магазині. Товари:
#  Кружка – 35 грн
#  Тарілка – 110 грн
# Користувач вводить назву товару та кількість.
# Якщо неправильна назва товару – continue
# Якщо від’ємна кількість – continue
# Виведіть загальну суму покупки.

# cup_cost = 35
# plate_cost = 110

#
# while True:
# cup_qty = 0
# plate_qty = 0
#     order_item = input('Please submit an item: cup / plate / cup and plate ')
#
#     if order_item == 'cup':
#         cup_qty = int(input('How many cups do you want to order? '))
#         if cup_qty < 0:
#             print('Please submit correct number')
#             continue
#     elif order_item == 'plate':
#         plate_qty = int(input('How many plates do you want to order? '))
#         if plate_qty < 0:
#             print('Please submit correct number')
#             continue
#     elif order_item == 'cup and plate':
#         cup_qty = int(input('How many cups do you want to order? '))
#         if cup_qty < 0:
#             print('Please submit correct number')
#             continue
#         plate_qty = int(input('How many plates do you want to order? '))
#         if plate_qty < 0:
#             print('Please submit correct number')
#             continue
#     else:
#         print('Please submit correct item name')
#         continue
#
#     total_cost = cup_qty * cup_cost + plate_qty * plate_cost
#
#     print(f'Total cost of your order is {total_cost} UAH')

# Завдання 7
# Напишіть програму для роботи з банківським рахунком.
# Стартовий баланс – 1000 грн
# Програма повинна мати такий функціонал:
#  Показати теперішній баланс
#  Поповнити рахунок(лише на додатню величину)
#  Зняти кошти(якщо їх достатньо)
#  Вихід
# Завдання 8
# Додайте до завдання 7 перевірку паролю перед показом
# меню. Справжній пароль 7842
# Користувачу дається 3 спроби.
# Якщо пароль введено успішно, то програма просить
# обрати дію як в завданні 7
# Якщо закінчились спроби, то програма виводить
# попередження та зупиняє роботу.


# balance = 1000
# password = 7842
# tries_left = 3
#
# for user_tries in range(tries_left):
#
#     password_try = int(input('Please submit a password to access your account '))
#
#     if password_try == password:
#         access_provided = True
#         print('Access provided')
#         break
#
#     else:
#         access_provided = False
#         print('Access denied. Please try again.')
#         tries_left -= 1
#         continue
#
#
# if access_provided == True:
#
#     while True:
#
#         user_choice = int(input('Choose operation: show balance (1), top up (2), withdraw (3), exit (4) '))
#
#         if user_choice == 1:
#             print(f'Your balance {balance} UAH')
#
#         elif user_choice == 2:
#             how_much_top_up = float(input('How much do you want to top up your account? '))
#
#             if how_much_top_up < 0:
#                 print('Please submit a positive number')
#                 continue
#             else:
#                 balance += how_much_top_up
#
#         elif user_choice == 3:
#             how_much_withdraw = float(input('How much do you want to withdraw? '))
#
#             if how_much_withdraw > balance:
#                 print('Insufficient funds')
#                 continue
#             else:
#                 balance -= how_much_withdraw
#
#         else:
#             break

# print('Цельции Фаренгейты Кельвины')
#
# for celcius in range (0, 101, 10):
#     kelvin = 273.15 + celcius
#     far = celcius * 1.8 + 32
#
#     print(f'    {celcius:^3}       {far:^5}      {kelvin}')


#
# while True:
#     percent = int(input('Введите процент от 0 до 25: '))
#
#     if percent > 0 and percent < 25: # if 0 < percent < 25:
#         break
#
#     balance = 1000
#     target_balance = 1100
#     month_count = 0
#
# while True:
#     balance += percent / 100 * balance
#     month_count += 1
#
#         if balance > target_balance:
#
# print(f'{month_count}')

# 1 + 2

# while True:
#     number = int(input('Введите число в диапазоне [1, 9] '))
#
#     if 1 <= number <= 9:
#         for multiplier in range(1, 11):
#             numbers_multiplied = number *  multiplier
#             print(f'{number} * {multiplier} = {numbers_multiplied}')
#     else:
#         print('Введите правильное число')

# 3

# start = int(input('Введите первое число: '))
# stop = int(input('Введите второе число: '))
#
# while True:
#     number_between = int(input('Введите число в диапазоне указанных чисел: '))
#     if start < number_between < stop:
#         break
#     else:
#         print('Введите правильное число')
#         continue
#
# for number in range(start, stop + 1):
#     if number == number_between:
#         print(f'! {number} !')
#     else:
#         print(number)

# 4

# while True:
#     user_choice = int(input('Выберите операцию: показать все числа диапазона (1), показать все числа диапазона в обратном порядке (2), сумма всех чисел диапазона (3), выход (4): '))
#
#     if user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4:
#         print('Неправильный выбор')
#         continue
#     if user_choice == 4:
#         break
#
#     first_number = int(input('Введите первое число: '))
#     second_number = int(input('Введите второе число: '))
#
#     if user_choice == 1:
#
#         print('Ваш диапазон: ')
#         for number in range(first_number, second_number + 1):
#             print(number)
#     elif user_choice == 2:
#         print('Ваш диапазон: ')
#         for number in range(second_number, first_number - 1, - 1):
#             print(number)
#     elif user_choice == 3:
#         sum = 0
#         print('Сумма диапазона: ')
#         for number in range(first_number, second_number + 1):
#             sum += number
#         print(sum)

# 5 + 6

# import random
#
# while True:
#     user_choice = int(input('Новая игра (1)       Выход (2) '))
#
#     if user_choice == 1:
#         random_number =  random.randint (0, 100)
#         try_counter = 0
#
#         while True:
#             user_number = int(input('Введите число: '))
#             try_counter += 1
#
#             if user_number < random_number:
#                 print('Меньше')
#             elif user_number > random_number:
#                 print('Больше')
#             else:
#                 print('Вы угадали!')
#                 print(f'Количество попыток = {try_counter}')
#                 break
#     elif user_choice == 2:
#         break
#     else:
#         print('Выберите 1 или 2')
#         continue

# 7

# import random
#
# draw_counter = 0
# win_counter = 0
# loss_counter = 0
#
# while True:
#     user_choice = int(input('Новая игра (1)       Выход (2) '))
#
#     if user_choice == 1:
#         rounds_number = int(input('Введите количество раундов: '))
#
#         for rounds in range (rounds_number):
#             rock_or_scissors_or_paper = input('Введите камень / ножницы / бумага: ')
#             computer_choice = random.choice(['камень', 'ножницы', 'бумага'])
#
#             if rock_or_scissors_or_paper == 'камень' and computer_choice == 'камень':
#                 draw_counter += 1
#             elif rock_or_scissors_or_paper == 'камень' and computer_choice == 'ножницы':
#                 win_counter += 1
#             elif rock_or_scissors_or_paper == 'камень' and computer_choice == 'бумага':
#                 loss_counter += 1
#
#             elif rock_or_scissors_or_paper == 'ножницы' and computer_choice == 'ножницы':
#                 draw_counter += 1
#             elif rock_or_scissors_or_paper == 'ножницы' and computer_choice == 'бумага':
#                 win_counter += 1
#             elif rock_or_scissors_or_paper == 'ножницы' and computer_choice == 'камень':
#                 loss_counter += 1
#
#             elif rock_or_scissors_or_paper == 'бумага' and computer_choice == 'бумага':
#                 draw_counter += 1
#             elif rock_or_scissors_or_paper == 'бумага' and computer_choice == 'камень':
#                 win_counter += 1
#             elif rock_or_scissors_or_paper == 'бумага' and computer_choice == 'ножницы':
#                 loss_counter += 1
#
#             else:
#                 loss_counter += 1
#
#         print(f'Ничья была {draw_counter} раз')
#         print(f'Вы победили {win_counter} раз')
#         print(f'Вы проиграли {loss_counter} раз')
#     elif user_choice == 2:
#         break
#     else:
#         print('Выберите 1 или 2')
#         continue

# 1

# user_str = input('Введите строку: ')
# user_symbol = input('Введите символ: ')

# count
# counter_count = user_str.count(user_symbol)
# print(counter_count)

# for
# counter_for = 0
# for symbol in user_str:
#     if symbol == user_symbol:
#         counter_for += 1
# print(counter_for)

# 3

# user_str = input('Введите строку: ')
# user_word = input('Введите слово: ')
#
# match = user_str.count(user_word)
#
# print(f'Слово {user_word} встречается {match} раз в тексте')

# 4

# user_str = input('Введите текст: ')
#
# letter_count = 0
# for symbol in user_str:
#     if symbol.isalpha() is True:
#         letter_count += 1
# print(f'В тексте {letter_count} букв')
#
# number_count = 0
# for symbol in user_str:
#     if symbol.isdigit() is True:
#         number_count += 1
# print(f'В тексте {number_count} цифр')

# 5

# user_str = input('Введите текст: ')
# search_word = input('Введите слово для поиска: ')
# replace_word = input('Введите слово, на которое заменить слово поиска: ')
#
# user_str = user_str.replace(search_word, replace_word)
# print(user_str)

# 6

# while True:
#     user_password = input('Введите пароль: ')
#
#     letter_count = 0
#
#     for letter in user_password:
#         if letter.isalpha() is True:
#             letter_count += 1
#
#     number_count = 0
#
#     for number in user_password:
#         if number.isdigit() is True:
#             number_count += 1
#
#     if len(user_password) > 8 and letter_count > 0 and number_count > 0:
#         print('Пароль создан успешно')
#         break
#     else:
#         print('Введен неверный пароль')
#         continue

# praktika

# user_str = input('Введите строку: ')
#
# # 1. Перевір, чи рядок починається з великої літери.
#
# letter_count = 0
#
# for symbol in user_str:
#     letter_count += 1
#     if letter_count == 1:
#         if symbol.isupper():
#             print('Строка начинается с большой буквы')
#         else:
#             print('Строка начинается с маленькой буквы, цифры или иного символа')
#
# # 2. Порахуйте кількість слів у рядку.
#
# words_count = 1 # Количество слов как минимум 1
#
# for symbol in user_str:
#     if symbol == ' ':
#         words_count += 1
#
# print(f'Количество слов: {words_count}')
#
# # 3. Замініть усі пробіли в рядку на підкреслення.
#
# low_line_text = user_str.replace(' ', '_')
#
# print(f'Строка с нижними подчеркиваниями вместо пробелов: {low_line_text}')
#
# # 4. Перетвори рядок на верхній регістр.
#
# uppercase_str = user_str.upper()
#
# print(f'Строка в верхнем регистре: {uppercase_str}')
#
# # 5. Перетвори рядок на нижній регістр.
#
# lowercase_str = user_str.lower()
#
# print(f'Строка в нижнем регистре: {lowercase_str}')
#
# # 6 -
#
# # 7. Додай до рядка знак оклику на кінці.
#
# print(f'Строка со знаком восклицания в конце {user_str + '!'}')
#
# # 8. Видали всі пробіли з рядка.
#
# print(f'Строка без пробелов {user_str.replace(' ', '')}')
#
# # 9. Порахуй, скільки разів у рядку зустрічається літера "а".
#
# a_count = 0
#
# for letter in user_str:
#     if letter == 'a' or letter == 'A':
#         a_count += 1
#
# print(f'Буква "а" встречается {a_count} раз')
#
# # 10. Перевір, чи рядок містить лише літери.
#
# if user_str.isalpha():
#     print('Строка состоит только из букв')
# else:
#     print('Строка состоит не только из букв')
#
# # 11. Перевір, чи рядок містить лише цифри.
#
# if user_str.isdigit():
#     print('Строка состоит только из цифр')
# else:
#     print('Строка состоит не только из цифр')
#
# # 12. Замініть усі входження "Python" на "PYTHON".
#
# python_caps_lock = user_str.replace('Python', 'PYTHON')
#
# print(f'Текст с PYTHON, вместо Python: {python_caps_lock}')
#
# # 13. Перевір, чи є у рядку слово "тест".
#
# if 'тест' in user_str:
#     print('В тексте есть слово "тест"')
# else:
#     print('В тексте нет слова "тест"')
#
# # 14. Розділіть речення на окремі слова.
#
# # Не понял задания
#
# # 15. З’єднай список слів у рядок через кому.
#
# coma_text = user_str.replace(' ', ', ')
# print(f'Текст со словами через запятую: {coma_text}')
#
# # 16. Перевір, чи починається рядок на "Привіт".
#
# letters_count = 0
# hello = False
#
# for symbol in user_str:
#     if symbol == 'П':
#         letters_count += 1
#
#     if letters_count == 1:
#         if symbol == 'р':
#             letters_count += 1
#
#     if letters_count == 2:
#         if symbol == 'и':
#             letters_count += 1
#
#     if letters_count == 3:
#         if symbol == 'в':
#             letters_count += 1
#
#     if letters_count == 4:
#         if symbol == 'е':
#             letters_count += 1
#
#     if letters_count == 5:
#         if symbol == 'т':
#             hello = True
#
# if hello:
#     print('Строка начинается с "Привет"')
#
# else:
#     print('Строка не начинается с "Привет"')
#
# # Тоже не знал, как по-другому сделать XD
#
# # 17. Перевір, чи закінчується рядок на "крапка.".
#
# # 18. Додай слово "Python" на початок рядка.
#
# python_user_str = 'Python' + user_str
# print(f'Строка с Python в начале: {python_user_str}')
#
# # 19. Замініть усі великі літери на маленькі.
#
# # lower() ? Если да, уже было
#
# # 20. Замініть усі входження символу "!" на "."
#
# dot_text = user_str.replace('!', '.')
# print(f'Строчка с . вместо !: {dot_text}')
#
# # 21. Виведи довжину рядка.
#
# user_str_length = len(user_str)
# print(f'Длина введенной строки: {user_str_length}')
#
# # 22. Додай до рядка лапки на початок і кінець.
#
# quote_user_str = '"' + user_str + '"'
# print(f'Начальная строка в кавычках: {quote_user_str}')


# 1

# user_str = input('Введите строку: ')
# index = int(input('Введите индекс: '))
#
# if index <= (len(user_str) - 1):
#     print(user_str[index])
# else:
#     print('Индекс слишком большой')

# 2

# user_str = input('Введите строку: ')
# start_index = int(input('Введите первый индекс: '))
# stop_index = int(input('Введите второй индекс: '))
#
# print(f'Начальная строка в пределах введенный индексов: {user_str[start_index:stop_index]}')

# 3

# user_str = input('Введите строку: ')
# n = int(input('Введите целое число: '))
#
# print(f'Первые символы: {user_str[0:n]}')
# print(f'Последние символы: {user_str[-1:-n-1:-1]}')

# 4

# user_str = input('Введите строку: ')
#
# if user_str.endswith('.') or user_str.endswith('!') or user_str.endswith('?'):
#     print('Заканчивается')
# else:
#     print('Не заканчивается')
#
# # или
#
# if user_str[-1] == '.' or user_str[-1] == '!' or user_str[-1] == '?':
#     print('Заканчивается')
# else:
#     print('Не заканчивается')

# 5

# user_str = input('Введите строку: ')
#
# if user_str[0].isupper():
#     print('Первая буква большая')
# else:
#     print('Первая буква маленькая или другой символ')

# 6

# user_str = input('Введите строку: ')
#
# if user_str == user_str[::-1]:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# 6 + 7

# user_str = input('Введите строку: ')
# user_symb = input('Введите символ: ')
#
# for i in range(len(user_str)):
#     if user_str[i] == user_symb:
#         print(f'Индекс символа: {i}')

# 8

# user_str = input('Введите слова через запятую: ')
#
# ind = user_str.index(',')
#
# print(f'Первое слово: {user_str[:ind]}')

# 9

# user_str = input('Введите слова через запятую: ')
#
# ind = user_str.rindex(',')
#
# end = user_str[:ind:-1]
#
# print(f'Последнее слово:{end[::-1]}')


# Завдання 10
# Користувач вводить слова поки не введе слово END.
# Збережіть це слово до одного з 4-ох рядків:
#  герундій – закінчується на ing
#  дієслово past tense – закінчується на ed
#  починаються на голосну – aeuio
#  решта
# Слова можуть вводитися як великими так і малими літерами.

# print('Чтобы вывести результаты впишите END')
# print()
#
# res_ing = ''
# res_ed = ''
# res_vowels = ''
# res_rest = ''
#
# while True:
#     word = input('Введите слово: ')
#     if word[-1:-4:-1] == 'gni':
#         res_ing += word + ', '
#     elif word[-1:-3:-1] == 'de':
#         res_ed += word + ', '
#     elif word[0] in 'aeuioAEUIO' and word != 'END':
#         res_vowels += word + ', '
#     elif word != 'END':
#         res_rest += word + ', '
#
#     if word == 'END':
#         break
#
# print()
# print(f'Слова с герундием: {res_ing[0:-2]}')
# print(f'Слова с past tense: {res_ed[0:-2]}')
# print(f'Слова на гласную: {res_vowels[0:-2]}')
# print(f'Остальные слова: {res_rest[0:-2]}')


# Завдання 11
# Користувач вводить математичний вираз, наприклад
# 23+45. Виведіть результат
# Обробіть такі математичні операції – +*/-
# Реалізуйте як консольну програму

# print('Чтобы закрыть программу, введите STOP')
# print()
#
# while True:
#     user_operation = input('Введите математическую операцию (+-*/) с двумя элементами: ')
#
#     if user_operation != 'STOP':
#         num1 = float(user_operation[:user_operation.index(' ')])
#
#         num2_preconverted = (user_operation[-1:user_operation.index(' ') + 2: -1])
#
#         num2_converted = float(num2_preconverted[::-1])
#
#         operation_to_do_index = user_operation.index(' ') + 1
#
#         operation_to_do = user_operation[operation_to_do_index]
#
#         if num1 and num2_converted and operation_to_do in '+-*/':
#             if operation_to_do == '+':
#                 result = num1 + num2_converted
#             elif operation_to_do == '-':
#                 result = num1 - num2_converted
#             elif operation_to_do == '*':
#                 result = num1 * num2_converted
#             elif operation_to_do == '/':
#                 result = num1 / num2_converted
#
#         print(result)
#         continue
#
#     else:
#         break


# Замініть всі символи з парними індексами у рядку на символ *.

# user_str = input('Введите строку: ')
#
# for i in range(len(user_str)):
#     if i % 2 == 0:
#         print('*', end = '')
#     else:
#         print(user_str[i], end = '')


# Користувач вводить рядок. Визначте, чи є він дійсним номером телефону у форматі (XXX) XXX-XXXX або XXX-XXX-XXXX.

# user_number = input('Введите номер телефона: ')
#
# if len(user_number) == 12 and user_number[:3].isdigit() and user_number[3] == '-' and user_number[4:7].isdigit() and user_number[7] == '-' and user_number[8:]:
#     print('Номер действителен')
# elif len(user_number) == 14 and user_number[0] == '(' and user_number[1:4].isdigit() and user_number[4] == ')' and user_number[5] == ' ' and user_number[6:9].isdigit() and user_number[9] == '-' and user_number[10:].isdigit():
#     print('Номер действителен')
# else:
#     print('Номер недействителен')


# Введіть текст. Замініть всі числа в тексті на символ #, не зачіпаючи інші символи.

# user_str = input('Введите строку: ')
#
# for symbol in user_str:
#     if symbol.isdigit():
#         print('#', end = '')
#     else:
#         print(symbol, end = '')


# Користувач вводить електронні адреси. Виведіть лише ті, що закінчуються на @gmail.com.

# print('Чтобы остановить ввод, впшите STOP')
# print()
#
# gmail_result = ''
#
# while True:
#     user_input = input('Введите электронный адрес: ')
#
#     if user_input != 'STOP':
#         if user_input.endswith('@gmail.com'):
#             gmail_result += user_input + ', '
#     else:
#         break
#
# print(f'Все адреса в домене @gmail.com: {gmail_result[:-2]}')


# Користувач вводить речення. Визначте, чи є це речення панграмою (містить кожну літеру алфавіту хоча б один раз).
# Необхідно враховувати лише літери, ігноруючи регістр, пробіли та пунктуацію

# user_sentence = input('Write sentence: ')
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# while True:
#
#     for i in range(len(user_sentence)):
#         if user_sentence[i] in alphabet:
#             alphabet_check = alphabet.replace(user_sentence[i], '')
#
#
#
#     print(alphabet_check)

# elif alphabet == '':
#     break


#
#
# x = alphabet.replace('a', '')
#
# print(x)
#


#
# for symbol in user_sentence:
#     if symbol in alphabet:
#         print(alphabet)
# print(alphabet)
#


# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
#  Виведіть на екран елементи цього списку
#  Збільшіть кожне число в 3 рази та виведіть результат
#  Замініть усі числа більші 10 на 0 та виведіть результат


# num_list = [1, 8, -5, 9]
#
# for i in range(len(num_list)):
#     print(num_list[i], end = ', ')

# for i in range(len(num_list)):
#     print(num_list[i] * 3, end = ', ')

# for i in range(len(num_list)):
#     if num_list[i] * 3 >= 10:
#         print(0, end = ', ')
#     else:
#         print(num_list[i] * 3, end = ', ')


# Завдання 2
# Користувач вводить числа, поки не введе -1. Збережіть усі
# ці числа в список. Виведіть їхню кількість, суму, мінімальне,
# максимальне та середнє.

# print('Чтобы остановить программу, введите -1')
# print()
#
# user_nums = []
#
# while True:
#     user_num = float(input('Введите число: '))
#     if user_num != -1:
#         user_nums.append(user_num)
#     else:
#         break
#
# print(f'Количество чисел в списке: {len(user_nums)}')
# print(f'Сумма чисел: {sum(user_nums)}')
# print(f'Минимальное число: {min(user_nums)}')
# print(f'Максимальное число: {max(user_nums)}')
# print(f'Среднее арифметическое чисел: {sum(user_nums) / len(user_nums)}')

# Завдання 3
# Користувач вводить числа, поки не введе 0. Створіть два
# нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.

# print('Чтобы остановить программу, введите 0')
# print()
#
# positive_nums = []
# negative_nums = []
#
# while True:
#     user_num = float(input('Введите число: '))
#     if user_num > 0:
#         positive_nums.append(user_num)
#     elif user_num < 0:
#         negative_nums.append(user_num)
#     else:
#         break
#
# positive_nums_str = str(positive_nums)[1: -1]
# negative_nums_str = str(negative_nums)[1: -1]
#
# print(f'Положительные числа: {positive_nums_str}')
# print(f'Отрицательные числа: {negative_nums_str}')

# Завдання 4
# Допоможіть користувачу створити набір з унікальних
# чисел.
# Спочатку користувач вводить кількість чисел, після чого
# самі числа. Якщо число нове, то добавте його в список. Якщо
# число уже є в списку, виведіть повідомлення про це.
# Практичне завдання
# Продовжуйте, поки не на збираєте потрібну кількість
# чисел

# user_unique_digits = []
#
# digits_num = int(input('Введите количество чисел: '))
#
# while True:
#     if len(user_unique_digits) == digits_num:
#         break
#
#     user_digit = float(input('Введите число: '))
#
#     if user_digit not in user_unique_digits:
#         user_unique_digits.append(user_digit)
#     else:
#         print('Такое число уже есть в Вашем списке')
#
# result = str(user_unique_digits)[1: -1]
#
# print(result)

# Завдання 5
# Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба збільшити
# усім зарплату.
# Виведіть нові зарплати

# print('Чтобы вывести результаты, введите -1')
# print()
#
# salaries = []
#
# while True:
#     employee_salary = float(input('Введите зарплату работника: '))
#     if employee_salary == -1:
#         print()
#         break
#     else:
#         salaries.append(employee_salary)
#
# percent = float(input('Введите процент, на который нужно увеличить всем зарплату: '))
#
#
# salaries_improved = []
#
# for salary in salaries:
#     salaries_improved.append(salary + salary * percent / 100)
#
# salaries_improved = str(salaries_improved)
#
# salaries_improved_result = salaries_improved[1: -1]
#
# print()
# print(f'Увеличенные на {percent} % зарплаты: {salaries_improved_result}')


# Завдання 6
# Створіть список з числами від 1 до 20. Користувач
# починає вводити числа поки не введе -1. Якщо число є в
# списку – видаліть його.
# В кінці виведіть кількість чисел що залишилась та самі
# числа.


# my_list = []
#
# for num in range(1, 21):
#     my_list.append(num)
#
# print('Чтобы оставновить ввод, впишите -1')
# print()
#
# while True:
#     user_num = int(input('Введите число: '))
#     if user_num == -1:
#         break
#     elif user_num in my_list:
#         my_list.remove(user_num)
#
# new_list_length = len(my_list)
#
# my_list = str(my_list)
# my_list_result = my_list[1: -1]
#
# print(f'Количество чисел которые остались: {new_list_length}')
# print(f'Числа, которые остались: {my_list_result}')

# Завдання 7
# Є 3 списки: додатні числа, числа що діляться на 10 та
# трицифрові числа.
# Користувач вводить числа поки не введе -1. Добавте число
# у відповідний список або списки.
# В кінці виведіть елементи усіх списків.

# positives = []
# ten_divided = []
# three_digits = []
# each_number = []
#
# print('Чтобы вывести списки, впишите -1')
# print()
#
# while True:
#     user_num = float(input('Впишите число: '))
#     if user_num != -1:
#         each_number.append(user_num)
#     else:
#         break
#
# num = float
#
# for num in each_number:
#     if num > 0:
#         positives.append(num)
#
# for num in each_number:
#     if num % 10 == 0:
#         ten_divided.append(num)
#
# for num in each_number:
#     if 100 <= num <= 999 and num.is_integer():
#         three_digits.append(num)
#
#
# positives.sort()
# ten_divided.sort()
# three_digits.sort()
#
# positives_result = str(positives)
# ten_divided_result = str(ten_divided)
# three_digits_result = str(three_digits)
#
# print()
# print(f'Положительные числа: {positives_result[1: -1]}')
# print(f'Числа, кратные 10: {ten_divided_result[1: -1]}')
# print(f'Трехзначные числа: {three_digits_result[1: -1]}')


# Завдання 8
# Користувач вводить кількість днів, після чого температуру
# повітря кожного дня.
# Збережіть температури у список
# Для кожного дня порахуйте різницю температур з
# попереднім днем.

# days_count = int(input('Введите количество дней: '))
# print()
#
# days = []
#
# for i in range(days_count):
#     i += 1
#     days.append(i)
#
# temps = []
#
# for day in days:
#     temp = float(input(f'Введите температуру в {day}-ый день: '))
#     temps.append(temp)
#
# diffs = []
#
# for i in range(1, len(temps)): # эту часть я подсмотрел у чата, потому что я сам два часа голову ломал, как это сделать XD
#         diff = temps[i] - temps[i - 1]
#         diffs.append(diff)
#
# diffs_result = str(diffs)
#
# print(f'Разница температур по сравнению с предыдущим днем: {diffs_result[1: -1]}')

# Завдання 9
# Створіть застосунок банк. Є список з рахунками клієнтів.
# Користувач вибирає одну з команд
#  Додати клієнта
#  Видалити клієнта
#  Поповнити рахунок
#  Зняти кошти
#  Вихід
# При додаванні клієнта, добавте рахунок в 0грн в кінець
# списку.
# В інших випадках запросіть ID(індекс) клієнта і якщо він
# вірний, то проведіть операцію

# import random
#
# users_ids = ['ID593802147', 'ID028374561', 'ID903284710', 'ID120394857', 'ID748920135']
# users_balances = [100.0, 200.0, 500.0, 1000.0, 5000.0]
# id_template = 'ID'
#
# while True:
#     user_choice = int(input('Добавить клиента (1)   Удалить клиента (2)   Пополнить баланс (3)   Снять средства (4)   Выход (5) '))
#     print()
#
#     if user_choice == 5:
#         break
#
#     if user_choice == 1:
#         for num in range(0, 9):
#             num = random.randint(0, 9)
#             num = str(num)
#             id_template += num
#             new_user_id = id_template
#
#         users_ids.append(new_user_id)
#         users_balances.append(0)
#
#     if user_choice == 2:
#         user_id_verification = input('Введите Ваш ID: ')
#         print()
#         if user_id_verification not in users_ids:
#             print('Указанного ID нет в базе')
#             print()
#         else:
#             deletion_ind = users_ids.index(user_id_verification)
#             users_ids.remove(users_ids[deletion_ind])
#             users_balances.remove(users_balances[deletion_ind])
#             print('Аккаунт удален')
#             print()
#
#     if user_choice == 3:
#         user_id_verification = input('Введите Ваш ID: ')
#         print()
#         if user_id_verification not in users_ids:
#             print('Указанного ID нет в базе')
#             print()
#         else:
#             while True:
#                 top_up = float(input('Введите сумму, на которую хотите пополнить баланс: '))
#
#                 if top_up > 0:
#                     top_up_ind = users_ids.index(user_id_verification)
#
#                     users_balances[top_up_ind] += top_up
#
#                     print()
#                     break
#                 else:
#                     print('Введите сумму больше 0')
#                     print()
#
#     if user_choice == 4:
#         user_id_verification = input('Введите Ваш ID: ')
#         print()
#         if user_id_verification not in users_ids:
#             print('Указанного ID нет в базе')
#             print()
#         else:
#             while True:
#                 withdraw = float(input('Введите сумму, которую хотите снять: '))
#                 print()
#
#                 withdraw_ind = users_ids.index(user_id_verification)
#
#                 if withdraw <= users_balances[withdraw_ind]:
#                     users_balances[withdraw_ind] -= withdraw
#                     print()
#                     break
#                 else:
#                     print('Недостаточно средств')
#                     print()


# Завдання 1
# Створіть список кольорів [“black”, “yellow”, “blue”]
#  Виведіть усі кольори
#  Виведіть кольори які починаються на b
#  Виведіть кольори де більше 5-ти літер
#  Добавте кольори red, green, purple
#  Зробіть усі слова в списку upper
#  Видаліть blue
#  Відсортуйте список в алфавітному порядку
#  У списку що вийшов виведіть елементи у форматі:
# 1. колір
# 2. колір
# …

# colors = ['black', 'yellow', 'blue']
#
# for color in colors:
#     print(color, end = ' ')
#
# print()
#
# for color in colors:
#     if color.startswith('b'):
#         print(color, end = ' ')
#
# print()
#
# for color in colors:
#     if len(color) > 5:
#         print(color, end = ' ')
#
# print()
#
# colors_expanded = colors + ['red', 'green', 'purple']
#
# for i in range(len(colors_expanded)):
#     colors_expanded[i] = colors_expanded[i].upper()
#
# colors_expanded.remove('BLUE')
#
# colors_expanded.sort()
#
# for color in colors_expanded:
#     print(f'{colors_expanded.index(color) + 1}. {color}')

# Завдання 2
# Користувач вводить слова через пропуск. Потрібно до
# кожного слова добавити ** на початку та в кінці і вивести
# результат через кому.
# Приклад: **яблуко**, **груша**, **персик**

# print('Чтобы показать результат, впишите END')
# print()
#
# user_input = input('Вводите слова через пропуск: ')
#
# user_words = user_input.split()
#
# user_words_edited = []
#
# for words in user_words:
#     user_words_edited.append('**' + str(words) + '**,')
#
# user_words_edited_str = ' '.join(user_words_edited)
#
# result = user_words_edited_str[:-1]
#
# print(result)

# Завдання 3
# Є два списки:
#  товари – ["хліб", "молоко", "сир", "яблука", "кава"]
#  ціни – [20.5, 28.0, 120.0, 45.3, 89.9]
# Користувач вводить назву товару, якщо такого товару
# немає, повідомити про це.
# Якщо товари є, то отримати його індекс та вивести
# відповідну ціну.

# print('Ассортимент магазина: хлеб, молоко, сыр, яблоки, кофе')
# print()
#
# items = ['хлеб', 'молоко', 'сыр', 'яблоки', 'кофе']
# prices = [20.5, 28.0, 120.0, 45.3, 89.9]
#
# while True:
#     user_input = input('Введите товар из ассортимента: ')
#     print()
#     if user_input not in items:
#         print('Название товара введено неверно')
#         print()
#         continue
#     else:
#         ind = items.index(user_input)
#
#     print(f'Цена {user_input} - {prices[ind]}')
#     print()

# Завдання 4
# На основі попереднього завдання створіть консольну
# програму магазину. Функціонал:
#  додати товар до кошика
#  видалити товар з кошика
#  вивести загальну ціну
#  очистити кошик
#  добавити новий товар у магазин
#  вихід

# print('Ассортимент магазина: хлеб, молоко, сыр, яблоки, кофе')
# print()

# items = ['хлеб', 'молоко', 'сыр', 'яблоки', 'кофе']
# prices = [20.5, 28.0, 120.0, 45.3, 89.9]

# user_options = ['1', '2', '3', '4', '5', '6']
# cust_items = []
# total_price = 0

# while True:
#     user_choice = input('Добавить товар в корзину (1)   Удалить товар из корзины (2)   Вывести общую цену (3)   Очистить корзину (4)   Добавить новый товар в магазин (5)   Выход (6) ').strip()

#     if user_choice in user_options:
#         if user_choice == '1':
#             item_choice = input('Какой товар вы хотите добавить? ')
#             item_qty = int(input('Сколько штук? '))
#             if item_choice in items:
#                 for i in range(item_qty):
#                     i += 1
#                     cust_items.append(item_choice)
#                 print('Товар добавлен в корзину')
#                 print()
#                 continue
#         if user_choice == '2':
#             item_choice = input('Какой товар вы хотите удалить? ')
#             item_qty = int(input('Сколько штук? '))
#             if item_choice in items:
#                 for i in range(item_qty):
#                     i += 1
#                     cust_items.remove(item_choice)
#                 print('Товар удалён из корзины')
#                 print()
#                 continue
#         if user_choice == '3':
#             for item in cust_items:
#                 ind = items.index(item)
#                 total_price += prices[ind] # не работает нормально, не понимаю почему

#             cust_items.sort()
#             print(f'Список Вашей корзины: {cust_items}')
#             print(f'Итоговая цена: {total_price}')

# total_price = 0

# Завдання 5
# У героя відомої гри є стати: сила, мудрість, інтелект,
# харизма та спритність. Рівень кожного стату генерується
# випадково від 50 до 70.
# Напишіть програму, де користувач буде мати змогу
# підвищити один стат який він сам обере від 5 до 10 значень
# випадково. Виведіть нові стати.
# stat_names = ["Strength", "Wisdom", "Intelligence", "Charisma", "Dexterity"]

# import random

# stat_names = ['Strength', 'Wisdom', 'Intelligence', 'Charisma', 'Dexterity']
# default_stats = [random.randint(50, 70), random.randint(50, 70), random.randint(50, 70), random.randint(50, 70), random.randint(50, 70)]
# choices = ['s', 'w', 'i', 'c', 'd']


# print('Ваши начальные статы')
# print()

# for i in range(-1, len(stat_names) - 1):
#     i += 1
#     print(f'{stat_names[i]} - {default_stats[i]}')

# print()

# print('Чтобы повысить стату, нажмите s  w  i  c  d')
# print()

# while True:
#     player_choice = input('Ваш выбор: ')
#     if player_choice in choices:
#         ind = choices.index(player_choice)
#         default_stats[ind] += random.randint(5, 10)
#         new_stats = default_stats
#         print('Статы повышены')
#         print()
#         break
#     else:
#         print('Неправильный выбор')
#         print()

# for i in range(-1, len(stat_names) - 1):
#     i += 1
#     print(f'{stat_names[i]} - {new_stats[i]}')

# # Завдання 7
# # Є 2 відсортованих за зростанням списки чисел.
# # Об'єднайте ці списки в один таким чином, щоб отримати
# # відсортований список.

# nums_1 = [1, 27, 54, 57, 60, 66, 67, 91, 93, 99]
# nums_2 = [3, 14, 26, 29, 39, 48, 70, 74, 77, 87]

# unsorted_nums = nums_1 + nums_2

# unsorted_nums.sort()

# print(unsorted_nums)

# Завдання 1
# Є деякий текст. Виведіть по ньому статистику:
#  кількість слів
#  середня довжина слова
#  найдовше слово
#  найкоротше слово
# Додатково: якщо найдовших(найкоротших) слів декілька
# то вивести усі

# some_str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
#
# words = some_str.split()
#
# words_amount = len(words)
#
# print(f'Количество слов - {words_amount}')
#
# no_comas_letters = some_str.replace(', ', '')
#
# only_words = no_comas_letters.split()
#
# only_letters = no_comas_letters.replace(' ', '')
#
# average_length = int(len(only_letters) / words_amount)
#
# print(f'Средняя длина слова - {average_length} целых букв')
#
# words_length = []
#
# for word in only_words:
#     words_length.append(len(word))
#
# max_len = max(words_length)
# min_len = min(words_length)
#
# longest_words = []
# shortest_words = []
#
# for word in only_words:
#     if len(word) == max_len:
#         longest_words.append(word)
#     elif len(word) == min_len:
#         shortest_words.append(word)
#
# longest_result = ', '.join(longest_words)
#
# shortest_result = ', '.join(shortest_words)
#
# print(f'Самые длинные слова: {longest_result}'[:-1])
#
# print(f'Самые короткие слова: {shortest_result}'[:-1])


# Завдання 2
# Є список з іменами. Видаліть лишні пробіли і переведіть
# їх у формат “Прізвище Ім’я”
# Приклад:
# Список: [
#  " іванов пЕТРО",
#  "сидорЕНКО марія ",
#  " Коваленко АНДРІЙ",
#  " мИХАЙЛЕНКО оЛЕНА "
# ]
# Результат: [
#  "Іванов Петро",
#  "Сидоренко Марія",
#  "Коваленко Андрій",
#  "Михайленко Олена"
# ]

# basic_names = [" іванов пЕТРО", "сидорЕНКО    марія ", " Коваленко  АНДРІЙ ", " мИХАЙЛЕНКО оЛЕНА "]
#
# stripped_names = []
#
# for name in basic_names:
#     stripped_names.append(name.strip())
#
# lower_names = []
#
# for name in stripped_names:
#     lower_names.append(name.lower())
#
# # print(lower_names)
#
# names_or_surnames = []
#
# for full_names in lower_names:
#     name_or_surname = full_names.split()
#     names_or_surnames.append(name_or_surname)
#
# # print(names_or_surnames)
#
# name_surname = []
#
# for i in range(len(names_or_surnames)):
#     str_lower = ''.join(' '.join(names_or_surnames[i]))
#     name_surname.append(str_lower)
#
# # print(name_surname)
#
# str = ', '.join(name_surname)
#
# # print(str)
#
# str_coma = str.replace(',', '')
#
# name_surname = str_coma.split()
#
# # print(name_surname)
#
# first_uppers = []
#
# for element in name_surname:
#     first_upper = element[0].upper() + element[1:]
#     first_uppers.append(first_upper)
#
# # print(first_uppers)
#
# # 0 + 1, 2 + 3, 4 + 5, 6 + 7
#
# name_surname_uppers = []
#
# for i in range(len(first_uppers) - 1):
#     name_surname_upper = first_uppers[i] + ' ' + first_uppers[i + 1]
#     name_surname_uppers.append(name_surname_upper)
#     i += 2
#
# final_results = []
#
# for name in name_surname_uppers:
#     if name_surname_uppers.index(name) % 2 == 0:
#         final_results.append(name)
#
# print(final_results)

# Завдання 3
# Є список який потенційно містить номери банківських
# карток. Для кожного елемента списку:
#  видаліть усі пробіли та дефіси
#  якщо рядок складається не з цифр або містить не 16
# символів – видаліть
#  створіть новий список куди добавте замасковані
# номери(лишаєте лише перші та останні 4 цифри а
# решту замінити на *, приклад 1234********7896
# Приклад: [
#  "1234 5678 9012 3456",
#  " 4444-3333-2222-1111",
#  "abcd efgh ijkl mnop",
#  "000011112222333",
#  "9999-8888-7777-6666",
#  "1111 2222 3333 4444 extra",
#  "5555-6666-7777-8888"
# ]
# Результат: [
# '1234********3456',
# '4444********1111',
# '9999********6666',
# '5555********8888'


# basic_list = ["1234 5678 9012 3456", " 4444-3333-2222-1111", "abcd efgh ijkl mnop", "000011112222333", "9999-8888-7777-6666", "1111 2222 3333 4444 extra", "5555-6666-7777-8888"]
#
# updated_list = []
#
# verified_list = []
#
# final_list = []
#
# for element in basic_list:
#     updated_element = element.replace(' ', '')
#     updated_element = updated_element.replace('-', '')
#     updated_list.append(updated_element)
#
# for element in updated_list:
#     if len(element) == 16 and element.isdigit():
#         verified_list.append(element)
#
#
# for element in verified_list:
#     stars = '*' * 8
#     masked_acc = element[:4] + stars + element[12:]
#     final_list.append(masked_acc)
#
# print(final_list)

# Завдання 4
# Є список з логами веб-сервісу у форматі
# [ІР-адреса] – [дата/час] – “[метод] [URL] [HTTP-версія]” –
# [статус]
#  розбийте усі логи на складові частини
#  виведіть унікальні URL адреси на які робились запити
#  скільки було зроблено запитів з методом POST GET та
# DELETE
#  виведіть ті логи які закінчились помилкою(статус не
# 200 OK)
# Приклад: [
#  '192.168.1.1 – 2025-06-01T12:00:00 – "GET /home
# HTTP/1.1" – 200 OK',
#  '192.168.1.2 – 2025-06-01T12:01:00 – "POST /login
# HTTP/1.1" – 403 Forbidden',
#  '192.168.1.3 – 2025-06-01T12:02:00 – "DELETE /user/123
# HTTP/1.1" – 200 OK',
#  '192.168.1.4 – 2025-06-01T12:03:00 – "GET /about
# HTTP/1.1" – 404 Not Found',
#  '192.168.1.1 – 2025-06-01T12:04:00 – "GET /home
# HTTP/1.1" – 200 OK',
#  '192.168.1.5 – 2025-06-01T12:05:00 – "POST /upload
# HTTP/1.1" – 500 Internal Server Error'
# ]

# logs = ['192.168.1.1 – 2025-06-01T12:00:00 – "GET /home HTTP/1.1" – 200', '192.168.1.2 – 2025-06-01T12:01:00 – "POST /login HTTP/1.1" – 403', '192.168.1.3 – 2025-06-01T12:02:00 – "DELETE /user/123 HTTP/1.1" – 200', '192.168.1.4 – 2025-06-01T12:03:00 – "GET /about HTTP/1.1" – 404', '192.168.1.1 – 2025-06-01T12:04:00 – "GET /home HTTP/1.1" – 200', '192.168.1.5 – 2025-06-01T12:05:00 – "POST /upload HTTP/1.1" – 500']
#
# properties = ["IP-адрес: ", "Дата/время: ", "Метод: ", "URL: ", "Версия HTTP: ", "Статус: "]
#
# logs_str = '\n'.join(logs)
#
# # print(logs_str)
#
# split_logs = logs_str.replace('–', '')
#
# split_logs = split_logs.replace('"', '').split()
#
# print(split_logs)
#
# log_1 = []
#
# log_2 = []
#
# log_3 = []
#
# log_4 = []
#
# log_5 = []
#
# log_6 = []
#
# for element in split_logs[0:6]:
#     log_1.append(element)
#
# for element in split_logs[6:12]:
#     log_2.append(element)
#
# for element in split_logs[12:18]:
#     log_3.append(element)
#
# for element in split_logs[18:24]:
#     log_4.append(element)
#
# for element in split_logs[24:30]:
#     log_5.append(element)
#
# for element in split_logs[30:36]:
#     log_6.append(element)
#
# for i in range(len(log_1)):
#     print(f'{properties[i] + log_1[i]}')
#
# print()
#
# for i in range(len(log_2)):
#     print(f'{properties[i] + log_2[i]}')
#
# print()
#
# for i in range(len(log_3)):
#     print(f'{properties[i] + log_3[i]}')
#
# print()
#
# for i in range(len(log_4)):
#     print(f'{properties[i] + log_4[i]}')
#
# print()
#
# for i in range(len(log_5)):
#     print(f'{properties[i] + log_5[i]}')
#
# print()
#
# for i in range(len(log_6)):
#     print(f'{properties[i] + log_6[i]}')
#
# # не знал, как сохранить в список текст статуса лога, поэтому оставил только номера статусов, также уверен,
# # что можно без кучи циклов всё сделать (полагаю, с использованием классов или списков в списке), но как смог
#
# unique_ips = []
#
# for element in split_logs:
#     if element.startswith('192.') and element not in unique_ips:
#         unique_ips.append(element)
#
# print(f'Уникальные IP-адреса: {unique_ips}')
#
# print()
#
# print((f'POST: {split_logs.count('POST')}'))
#
# print()
#
# print(f'GET: {split_logs.count('GET')}')
#
# print()
#
# print(f'DELETE: {split_logs.count('DELETE')}')
#
# print()
#
# all_logs = [log_1, log_2, log_3, log_4, log_5, log_6]
#
# for log in all_logs:
#     if log[-1] != '200':
#         print(log) # лог с ошибкой

# Завдання 5
# Створіть систему з роботою даними студентів. Кожен
# студент має: ім’я, прізвище, вік, спеціальність, та список
# оцінок
# Додайте такий функціонал:
# 1. додати нового студента
# 2. переглянути всіх студентів
# 3. знайти студента за прізвищем
# 4. додати оцінку студенту
# 5. показати середній бал студента
# 6. видалити студента
# 7. вихід

# Завдання 1
# Напишіть функцію, яка відображає наступний текст:
# “Don’t let the noise of others’ opinions
# drown out your own inner voice.”
# Steve Jobs

# def print_quote():
#     print('“Don’t let the noise of others’ opinions\n drown out your own inner voice.”\n                                Steve Jobs')
#
# print_quote()

# Завдання 2
# Напишіть функцію, яка отримує два числа та відображає
# усі парні числа між ними

# def print_even_nums(start, finish):
#     for num in range(start, finish + 1):
#         if num % 2 == 0:
#             print(num, end = ' ')
#
# print_even_nums(0, 10) # 0 2 4 6 8 10

# Завдання 3
# Напишіть функцію, яка відображає числа діапазону в
# зростаючому або спадаючому порядку.
# Функція отримує 3 аргументи: межі діапазону та булеву
# змінну:
#  якщо вона True – порядок зростаючий
#  якщо вона False – порядок спадаючий

# def print_nums(start, finish, is_positive):
#     if is_positive:
#         for num in range(start, finish + 1):
#             print(num, end = ' ')
#
#     else:
#         for num in range(finish, start -1, -1):
#             print(num, end = ' ')
#
#     print()
#
# print_nums(0, 10, True) # 0 1 2 3 4 5 6 7 8 9 10
# print_nums(0, 10, False) # 10 9 8 7 6 5 4 3 2 1 0

# Завдання 4
# Напишіть функцію, яка повертає найбільше серед 4-ох
# чисел. Числа передаються як параметри.

# def return_max_num(num_1, num_2, num_3, num_4):
#     max_number = max(num_1, num_2, num_3, num_4)
#
#     print(max_number)
#
# return_max_num(1, 2, 3, 4) # 4

# Завдання 5
# Напишіть функцію, яка обчислює суму чисел в певному
# діапазоні. Межі діапазону передаються як параметри.
# Якщо межі неправильні(наприклад числа від 10 до 5) то
# поміняйте їх місцями.

# def return_sum(num_1, num_2):
#     summa = 0
#     if num_2 > num_1:
#         for num in range(num_1, num_2 + 1):
#             summa += num
#
#     else:
#         for num in range(num_2, num_1 + 1):
#             summa += num
#
#     print(summa)
#
# return_sum(4, 0)

# Завдання 6
# Напишіть функцію, яка перевіряє чи є число простим.
# Число передається як параметр. Результатом має бути True або
# False.
# Число називають простим, якщо воно ділиться лише на
# себе та 1

# def check_num(num):
#     division_conter = 0
#
#     for i in range(1, num + 1):
#         if num % i == 0:
#             division_conter += 1
#
#     if division_conter > 2:
#         print('Число не простое')
#     else:
#         print('Число простое')
#
# check_num(11) # Число простое

# Завдання 7
# Напишіть функцію, яка перевіряє чи є шестизначне число
# «щасливим». Число передається як параметр. Результатом має
# бути True або False.
# Число називають «щасливим» якщо сума перших трьох
# цифр дорівнює сумі останніх трьох чисел. Наприклад, 123420
# – щасливе, бо 1+2+3 = 4+2+0, а число 723422 – не щасливе, бо
# 7+2+3 != 4+2+2

# def check_num(num):
#     num = str(num)
#     num_digits = []
#     for digit in num:
#         digit = int(digit)
#         num_digits.append(digit)
#
#     if sum(num_digits[:3]) == sum(num_digits[3:]):
#         result = True
#     else:
#         result = False
#
#     print(result)
#
#     return result
#
# check_num(123420) # True
# check_num(723422) # False

# Завдання 1
# Напишіть функцію distance(x1, y1, x2, y2), яка
# обчислює відстань між точкою та повертає результат.

# def distance(x1, y1, x2, y2):
#     dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#
#     print(f'Расстояние между двумя точками = {dist:.2f}')
#
#     return dist
#
#
# distance(150, 255, 650, 1000)

# Завдання 2
# Дано дійсне позитивне число a та ціле число n.
# Взведіть a в n степінь. Рішення оформіть у вигляді
# функції power(a, n). Стандартною функцією зведення в
# рівень користуватися не можна.

# def power(a, n):
#     n = int(n)
#
#     result = 1
#
#     for _ in range(n):
#         result *= a
#
#     print(result)
#
#
# power(3, 3) # 27

# Завдання 3
# Напишіть функцію, що обчислює факторіал
# кожного елемента списку цілих. Функція повертає
# новий список, який містить отримані факторіали

# def show_factorials(start, end):
#     nums_to_factorial = []
#
#     start = int(start)
#
#     end = int(end)
#
#     for num in range(start, end + 1):
#         nums_to_factorial.append(num)
#
#     factorials = []
#
#     for num in nums_to_factorial:
#         multiplier = 1
#
#         for i in range(1, num + 1):
#             multiplier *= i
#
#         factorials.append(multiplier)
#
#     return factorials
#
#
# print(show_factorials(0, 5)) # [1, 1, 2, 6, 24, 120]

# Завдання 4
# Напишіть функцію, яка шукає числа у списку
# цілих та повертає список їх індексів.

# def show_index(num_list):
#     index_list = []
#
#     for element in num_list:
#         if element.is_integer():
#             index_list.append(num_list.index(element))
#
#     return index_list
#
#
# print(show_index([3, 7, 4.5, 0])) # [0, 1, 3]
#
# # Как сделать так, чтобы можно было в списке проверять str?

# Завдання 5
# Напишіть функцію, що видаляє зі списку цілих
# деяке задане число. З функції потрібно повернути
# кількість видалених елементів та новий список без цих
# елементів.


# def delete_num(num_list, num_to_delete):
    # 1 option # new_list = []
    #
    # deleted_nums = 0
    #
    # for num in num_list:
    #     if num != num_to_delete:
    #         new_list.append(num)
    #     else:
    #         deleted_nums += 1
    #
    # return deleted_nums, new_list

    # or >>>

    # 2 option # deleted_nums = 0
    #
    # for num in num_list:
    #     if num == num_to_delete:
    #         num_list.remove(num)
    #         deleted_nums += 1
    #
    # return deleted_nums, num_list


# print(delete_num([0, 1, 2, 3, 4],3)) # (1, [0, 1, 2, 4])
# print(delete_num([0, 1, 2, 3, 4],2)) # (1, [0, 1, 3, 4])
#
# # Также вопрос, как сохранять числа, которые я удалил, и плюсовать количество удаленных элементов при дальнейших вызовах функции


# Завдання 1
# Напишіть функцію, яка буде приймати на вхід
# три числа в якості і повертати їх медіану. В основній
# програмі повинен виконуватися запит до користувача
# на предмет введення трьох чисел, а також виклик
# функцій і відображення результату.

# Мы сможем на занятии решить эту задачу? Потому что у меня не получается

# Завдання 2
# Такі слова, як перший, другий, третій, є
# чисельник. У цьому вправі вам необхідно написати
# функцію, що приймає на вхід в якості єдиного
# аргументу ціле число і повертається рядкове значення,
# що містить відповідний чисельник. Ваша функція
# повинна обробляти числа в діапазоні від 1 до 12.

# def show_adj(num):
#     numbers = [
#     "первый",
#     "второй",
#     "третий",
#     "четвёртый",
#     "пятый",
#     "шестой",
#     "седьмой",
#     "восьмой",
#     "девятый",
#     "десятый",
#     "одиннадцатый",
#     "двенадцатый"
# ]
#
#     return numbers[num - 1]
#
#
# print(show_adj(1)) # первый

# Завдання 3
# Напишіть функцію, яка буде приймати в якості
# параметрів рядок s, а також ширину вікна в символах –
# w. Функція повинна створити новий рядок, у який на
# початку додано необхідну кількість пробілів, щоб
# початковий рядок виявився розміщеним у центрі
# заданного вікна.

# def centralize_str(s, w):
#     total_spaces = w - len(s)
#
#     left_spaces = int(total_spaces / 2)
#
#     right_spaces = total_spaces - left_spaces
#
#     centralized_str = left_spaces * '_' + s + right_spaces * '_'
#
#     return centralized_str
#
#
# print(centralize_str('hello', 11)) # ___hello___

# Завдання 4
# Напишіть функцію, яка приймає ціле число та
# визначає, чи є воно числом Армстронга.


# def check_num(num):
#     num = str(num)
#
#     num_digits = []
#
#     for digit in num:
#         num_digits.append(int(digit))
#
#     sum_result = 0
#
#     for i in range(len(num_digits)):
#         sum_result += num_digits[i] ** (len(num_digits))
#
#     if sum_result == int(num):
#         result = True
#     else:
#         result = False
#
#     return result
#
#
# print(check_num(9474)) # True

# Завдання 5
# Напишіть функцію, яка приймає рядок та список
# символів, які потрібно видалити з рядка.

# def remove_symbols(some_str, sym):
#     symbols_list = []
#
#     for symbol in some_str:
#         symbols_list.append(symbol)
#
#     symbols_to_delete = []
#
#     for symbol in sym:
#         symbols_to_delete.append(symbol)
#
#     clean_list = []
#
#     for symbol in symbols_list:
#         if symbol not in symbols_to_delete:
#             clean_list.append(symbol)
#
#     clean_list_str = ''.join(clean_list)
#
#     return clean_list_str
#
#
# print(remove_symbols('It was one of those moments where time seemed to pause, giving space for quiet thoughts and a deep sense of calm.', ['a', 'o', 'e']))
# # It ws n f ths mmnts whr tim smd t pus, giving spc fr quit thughts nd  dp sns f clm.

# Завдання 1
# Напишіть функцію, яка повертає суму чисел з
# списку. Список передається як параметр.

# def return_sum(nums):
#     result = 0
#
#     for i in range(len(nums)):
#         result += nums[i]
#
#     return result
#
#
# print(return_sum([0, 1, 2]))

# Завдання 2
# Напишіть функцію, яка повертає найбільше число з
# списку. Список передається як параметр.

# def return_max(nums):
#     max_num = max(nums)
#
#     return max_num
#
#
# print(return_max([3, 0, 7]))

# Завдання 3
# Напишіть функцію, яка повертає кількість простих чисел з
# списку. Список передається як параметр.
# Для цього завдання вам потрібно написати функцію, яка
# отримує число як параметр, та повертає True якщо воно
# просте, та False в протилежному випадку

# def return_simple(nums):
#     simple_nums = []
#
#     for num in nums:
#         if check_num(num):
#             simple_nums.append(num)
#
#     result = len(simple_nums)
#
#     print(simple_nums)
#
#     return result
#
#
# def check_num(num):
#     division_counter = 0
#
#     for i in range(1, num + 1):
#         if num % i == 0:
#             division_counter += 1
#
#     return division_counter == 2
#
#
# print(return_simple([0, 1, 2, 3, 4, 7, 11, 23]))

# Завдання 4
# Напишіть функцію, яка видаляє всі від’ємні числа зі
# списку. Список передається як параметр. Функція має
# повернути кількість видалених чисел.

# def remove_negative(nums):
#     negative_nums = []
#
#     only_positive_nums = []
#
#     counter = 0
#
#     for num in nums:
#         if num < 0:
#             negative_nums.append(num)
#             counter += 1
#
#     for num in nums:
#         if num not in negative_nums:
#             only_positive_nums.append(num)
#
#     nums[:] = only_positive_nums
#
#     return counter
#
#
# nums = [-1, 2, 3, 4, -5]
#
# print(remove_negative(nums)) # 2
#
# print(nums)

# Завдання 5
# Напишіть функцію, яка шукає певне число в списку.
# Функція повинна повертати список усіх індексів цього
# числа в списку. Якщо числа немає в списку, то потрібно
# повернути порожній список. Список та число
# передаються як два параметри.

# def find_num(nums, num_to_find):
#     result = []
#
#     for i in range(len(nums)):
#         if nums[i] == num_to_find:
#             result.append(i)
#
#     return result
#
# print(find_num([1, 2, 3, 4, 1], 1)) # [0, 4]

# Завдання 6
# Напишіть функцію, рахує факторіал кожного
# елемента списку. Результатом має бути список з
# факторіалами.
# Факторіалом числа n (позначають n!) називаю
# добуток усіх чисел від 1 до n. Наприклад 6! =
# 1*2*3*4*5*6. Якщо число від’ємне, то вважайте що
# його факторіал рівний Nonе. Факторіал число 0 вважають
# рівним 1.

# def show_factorials(nums):
#     factorials = []
#
#     for num in nums:
#         if num >= 0:
#             multiplier = 1
#
#             for i in range(1, num + 1):
#                 multiplier *= i
#
#             factorials.append(multiplier)
#
#         else:
#             factorials.append(None)
#
#     return factorials
#
#
# print(show_factorials([0, 1, 2, -1, -3])) # [1, 1, 2, None, None]


    #     start, end):
    # nums_to_factorial = []
    #
    # start = int(start)
    #
    # end = int(end)
    #
    # for num in range(start, end + 1):
    #     nums_to_factorial.append(num)
    #
    # factorials = []
    #
    # for num in nums_to_factorial:
    #     multiplier = 1
    #
    #     for i in range(1, num + 1):
    #         multiplier *= i
    #
    #     factorials.append(multiplier)
    #
    # return factorials


# 18.06.2025

# Завдання 1
# Напишіть функцію, яка отримує назву мови
# програмування та виводить повідомлення:
# «You are learning [мова програмування]»
# За замовчуванням, має бути Python.

# def message(name='Python'):
#     if not isinstance(name, str):
#         print('Введите строку')
#         return
#
#     return print(f'«You are learning {name}»')
#
#
# message()
# message('JS')

# Завдання 2
# Напишіть функцію, яка отримує текст як параметр та
# виводить його на екран. Також має бути параметр
# lowercase:
#  Якщо він True, то текст потрібно перевести в
# нижній регістр
#  Якщо False, то текст не змінюється
# За замовчуванням False.

# def show_text(text, lowercase=False):
#     if not isinstance(text, str):
#         print('Введите строку')
#         return
#
#     if lowercase:
#         text = text.lower()
#
#     return print(text)
#
#
# show_text('SDFSDFDSFGSDGSDGSDG')
# show_text('KDSFHDKFNfkndslkfnsdfkdjsf', True)

# Завдання 3
# Напишіть функцію, яка отримує температуру та
# переводить її в градуси Цельсія або в Фаренгейта. Для
# цього є додатковий параметр unit_mapping:
#  Якщо він C_to_F, то функція повинна повернути
# градуси Фаренгейта
#  Якщо він F_to_C, то функція повинна повернути
# градуси Цельсія
#  Якщо він щось інше, то функція виводить
# повідомлення про помилку, та повертає число без
# змін
# За замовчуванням, C_to_F

# # Цельсий в Фаренгейт
# fahrenheit = (celsius * 9/5) + 32
#
# # Фаренгейт в Цельсий
# celsius = (fahrenheit - 32) * 5/9

# def change_measure(temp, unit_mapping='C_to_F'):
#     if not isinstance(temp, (int, float)):
#         print('Введите число')
#         return
#
#     if not isinstance(unit_mapping, str):
#         print('Введите строку')
#         return
#
#     if unit_mapping == 'C_to_F':
#         temp = temp = (temp * 9 / 5) + 32
#         return temp
#     elif unit_mapping == 'F_to_C':
#         temp = (temp - 32) * 5/9
#         return temp
#     else:
#         print('Введите правильный параметр')
#         return temp
#
#
# print(change_measure(30))

# Завдання 4
# Напишіть функцію, яка отримує список чисел як
# параметр та повертає кількість парних або непарних
# чисел в ньому, в залежності від параметра odd:
#  Якщо він True, то кількість непарних
#  Якщо False, то кількість парних
# За замовчуванням False.


# def check_values(nums, odd=False):
#     if not isinstance(nums, list):
#         print('Введите список чисел')
#         return
#
#     if not isinstance(odd, bool):
#         print('Введите правильный параметр или не вводите ничего')
#         return
#
#
#     for num in nums:
#         if not isinstance(num, (int, float)):
#             print('Введите список чисел')
#             return
#
#     new_nums = []
#
#     if odd:
#         for num in nums:
#             if num % 2 != 0:
#                 new_nums.append(num)
#         return new_nums
#     else:
#         for num in nums:
#             if num % 2 == 0:
#                 new_nums.append(num)
#         return new_nums
#
#
# print(check_values([0, 120, 111, 874, 14124, 551, 999], 'dsfdsfdsfds'))


# Завдання 5
# Напишіть функцію, яка отримує декілька чисел як
# параметрів.
#  Якщо числа 2, то повернути найбільше
#  Якщо числа 3, то повернути суму
#  Якщо чисел більше 3, то повернути їхній добуток

# def calculate(nums):
#     if not isinstance(nums, list):
#         print('Введите список чисел')
#         return
#
#     for num in nums:
#         if not isinstance(num, (float, int)):
#             print('В списке должны быть только числа')
#             return
#
#     result = 1
#
#     if len(nums) == 2:
#         result = max(nums)
#         return result
#     elif len(nums) == 3:
#         result = sum(nums)
#         return result
#     else:
#         for num in nums:
#             result *= num
#         return result
#
#
# print(calculate([1, 2, 30, 4]))



# 🟡 Середній рівень (11–20)
# Напиши функцію register_user(username, password, role='user'), яка зберігає користувача з роллю.


# Створи функцію draw_line(char='*', length=10), яка малює горизонтальну лінію.

# def draw_line(char='*', length=10):
#     for _ in range(length):
#         print(char, end='')
#
#
# draw_line(char='-', length=200)


# Створи функцію calculate_salary(base, bonus=0, tax_percent=20) для обчислення зарплати після податків.




# Напиши функцію format_date(day, month, year=2025) для форматування дати.

# def format_date(day, month, year=2025):
#     if not isinstance(day, int) and not 1 < day < 31:
#         print('Введите корректную дату')
#         return
#
#     if not isinstance(month, int) and not 1 < month < 31:
#         print('Введите корректный месяц')
#         return
#
#     if not isinstance(year, int):
#         print('Введите корректный год')
#         return
#
#     print(f'{day}-{month}-{year}')
#
#
# format_date(30, 12) # 30-12-2025
# Створи функцію send_email(to, subject, body='(порожньо)'), яка імітує надсилання листа.
# def send_email(to, subject, body=''):
#     return print(f'E-mail was sent to {to}. Subject: {subject}. E-mail content: {body}')
#
# Напиши функцію log(message, level='INFO'), яка друкує лог-повідомлення з рівнем.
#
# Створи функцію create_user(name, is_active=True, is_admin=False).
#
# Напиши функцію make_list(n=3, item=0), яка повертає список з n однакових елементів.

# def make_list(n=3, item=0):
#     list_template = []
#
#     for _ in range(n):
#         list_template.append(item)
#
#     new_list = list_template
#
#     return new_list
#
# print(make_list(n = 5, item = 3))


# Завдання 1
# Напишіть lambda-функції, які:
#  Підносить число до квадрату
#  Отримує довжини трикутника і повертає периметр
#  Отримує прізвище та ім’я і повертає рядок у форматі
# «Прізвище, ім’я»
#  Перевіряє чи є число парним

# power_2 = lambda num: num ** 2
#
# triangle_p = lambda side1, side2, side3: sum([side1, side2, side3])
#
# surname_name = lambda surname, name: f'{surname_name}, {name}'
#
# is_even = lambda num: num % 2 == 0

# Завдання 2
# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел та повертає список з лише
# додатніми числами
#  Отримує список слів та повертає список слів, в яких
# більше ніж 3 літери
#  Отримує список слів та літеру і повертає список тих
# слів, які починаються на цю літеру(регістр
# неважливий)

# nums = [1, -1, 2, -2, 3, -3]

# get_positives = filter(lambda num: num > 0, nums)
#
# result_get_positives = list(get_positives)

# words = ['Python', 'computer', 'cat', 'moon', 'win']
#
# get_words = filter(lambda word: len(word) > 3, words)
#
# result_get_words = list(get_words)

# words1 = ["House", "room", "Kitchen", "bed", "chair", "table", "Door", "window", 'apple']
# letter = 'a'
#
#
# get_words_letter = filter(lambda word: word.lower().startswith(letter), words1)
#
# result_get_words_letter = list(get_words_letter)
#
# print(result_get_words_letter)

# Завдання 3
# Напишіть функцію, яка отримує іншу функцію та
# параметри. Поверніть час роботи функції у секундах

# import time
#
# def count_time(func, *param):
#     start = time.time()
#
#     new_func = func(*param)
#
#     end = time.time()
#
#     return end - start


# def make_list(n=3, item=0):
#     list_template = []
#
#     for _ in range(n):
#         list_template.append(item)
#
#     new_list = list_template
#
#     return new_list
#
# print(count_time(make_list, 100000000, 1000000000))


# Завдання 4
# Напишіть функції, які:
#  Сортує список слів за останньою літерою
#  Сортує список чисел за кількістю цифр
#  Знаходить число зі списку, яке найближче до
# заданого(передається як параметр)
#  Знаходить слово у списку з найменшою довжиною
#  Сортує список чисел за кількістю цифр, якщо кількість
# цифр однакова, то сортує за значенням числа

# words = ['word', 'excel', 'length', 'apple', 'phone', 'chair', 'picture']
#
# first_func = sorted(words, key=lambda word: word[-1])
#
# print(first_func) # ['word', 'apple', 'phone', 'picture', 'length', 'excel', 'chair']
#
# nums = [0, 1, 45, 200, -100, 400, 555, 999, 10000, 10000001, -1, -100, 5, 1.5]
#
# second_func = sorted(nums, key=lambda num: len(str(num).replace('-', '').replace(',', '').replace('.', '')))
#
# print(second_func)

# nums = [0, 1, 45, 200, -100, 400, 555, 999, 10000, 10000001, -1, -100, 5, 1.5]
#
# nums.sort()
#
# def third_func(some_list, num):
#     return min(some_list, key=lambda x: abs(x - num))


# 02.07.2025

# Завдання 1
# Користувач вводить числа через кому. Збережіть їх у
# кортеж. Виведіть на екран:
#  Суму чисел
#  Найбільше та найменше число
#  Перші та останні 3 числа
#  Кількість чисел 7
#  Пари індекс – число
# Додатково, якщо користувач введе порожній рядок, то
# створіть власний кортеж з випадковими числами(12 шт).
# import random
#
# def get_numbers():
#     user_input = input("Введите числа через пробел: ")
#
#     empty_list = []
#
#     if not user_input:
#         for _ in range(12):
#             empty_list.append(random.randint(0, 100))
#         return tuple(empty_list)
#
#     numbers_tuple = tuple(map(float, user_input.split(',')))
#
#     return numbers_tuple
#
# def save_tuple():
#     numbers_tuple = get_numbers()
#
#     print(numbers_tuple)
#
#     print(f'Сумма чисел: {sum(numbers_tuple)}')
#
#     print(f'Максимальное число: {max(numbers_tuple)}')
#
#     print(f'Минимальное число: {min(numbers_tuple)}')
#
#     print(f'Первые три числа: {numbers_tuple[0:3]}')
#
#     print(f'Последние три числа: {numbers_tuple[-3:]}')
#
#     print(f'Количество чисел 7: {numbers_tuple.count(7)}')
#
#     print(f'{list(enumerate(numbers_tuple))}')
#
#
# save_tuple()

# Завдання 2
# Напишіть наступну програму: є кортеж з іменами
# зареєстрованих студентів. Користувач вводить ім’я студента
# після чого отримує повідомлення, чи студент зареєстрований.
# Програма закінчує роботу коли користувач введе порожній
# рядок

# students_names = ("Александр", "Мария", "Дмитрий", "Екатерина", "Иван", "Ольга", "Сергей", "Анна")
#
# def check_name():
#     while True:
#         user_input = input('Введите имя (чтобы остановить программу, нажмите Enter): ')
#
#         if user_input == '':
#             print('Выход из программы')
#             break
#
#         if user_input in students_names:
#             print(f'{user_input} зарегистрирован в списке сдуентов')
#         else:
#             print(f'{user_input} не зарегистрирован в списке студентов')
#
#
# check_name()

# Завдання 3
# Напишіть наступну програму: є кортеж з назвами фільмів.
# Користувач вводить назву фільму.
#  Якщо фільм знаходиться в першій половині кортежу,
# треба вивести ретро-фільм
#  Якщо в другій половині – сучасний фільм
#  Якщо один з останніх п'яти – новий фільм

# films = (
#     "Побег из Шоушенка",
#     "Зелёная миля",
#     "Форрест Гамп",
#     "Начало",
#     "Интерстеллар",
#     "Бойцовский клуб",
#     "Матрица",
#     "Список Шиндлера",
#     "1+1 (Неприкасаемые)",
#     "Леон"
# )
#
# def get_film_type():
#     print('Чтобы остановить программу, кликните Enter')
#
#     while True:
#         user_input = input('Введите название фильма: ')
#
#         if user_input == '':
#             break
#
#         if user_input not in films:
#             print(f'Фильма "{user_input}" нет в базе. Попробуйте еще раз')
#
#         if user_input in films[:(len(films)) // 2]:
#             print('Ретро-фильм')
#             continue
#         elif user_input in films[-5:]:
#             print('Новый фильм')
#             continue
#         elif user_input in films[(len(films)) // 2:]:
#             print('Современный фильм')
#
#
# get_film_type()


# Завдання 4
# Напишіть функцію, яка отримує кортеж з назвами фруктів
# та слово. Потрібно повернути скільки разів дане слово
# зустрічається в кортежі(регістр неважливий). Складні назви
# теж враховуються. Приклад:
# ("яблуко", "яблуко Сидоренко", "банан жовтий", "Яблуко")
# Яблуко зустрічається 3 рази


# fruits = ('груша', 'помидор', 'яблоко', 'Груша', 'яблокО', 'ПОМИДОР')
#
# searched_fruit = 'ПОМИДОР'
#
# def count_word(words, searched_word):
#     searched_word_counter = 0
#
#     for word in words:
#         if word.lower() == searched_word.lower():
#             searched_word_counter += 1
#
#     return f'Слово "{searched_word.lower()}" встречается {searched_word_counter} раз/а'
#
#
# print(count_word(fruits, searched_fruit))

# Завдання 5
# Напишіть функцію, яка отримує кортеж з числами та
# виводить на екран статистику по кількості чисел з різною
# кількістю цифр. Приклад:
# одноцифрових – 3 шт
# двоцифрових – 5 шт
# трицифрових – 2 шт

# nums = (0, -10, 23, -5354, 61, 234.5, 1312321, 61, 1, 2, -3, 22.1)
#
# def get_stats(numbers_tuple):
#     one_dig, two_dig, three_dig = 0, 0, 0
#
#     for num in numbers_tuple:
#         if abs(int(num)) in range(0, 10):
#             one_dig += 1
#         elif abs(int(num)) in range(10, 100):
#             two_dig += 1
#         elif abs(int(num)) in range(100, 1000):
#             three_dig += 1
#
#     return f'1-цифровых чисел: {one_dig}\n2-цифровых чисел: {two_dig}\n3-цифровых чисел: {three_dig}'
#
#
# print(get_stats(nums))

# Завдання 6
# Користувач вводить назви товарів через кому. Потрібно
# сформувати кортеж. Також вводяться ціни товарів, які теж
# треба зберегти у кортеж. Виведіть на екран пари товар – ціна.
# Також виведіть назви найдорожчого та найдешевшого товарів.

# def show_items_prices():
#     user_input_items = input('Введите товары через запятую: ')
#
#     items = tuple(user_input_items.split(','))
#
#     while True:
#         user_input_prices = input('Введите цены соответствующих товаров через запятую: ')
#
#         prices = tuple(user_input_prices.split(','))
#
#         for element in prices:
#             if not isinstance(element, (int, float)):
#                 print('Введите числа цен')
#                 continue

# 1

# import random
#
# user_input = input('Введите числа через запятую: ')
#
# nums = user_input.split(',')
#
# user_nums = []
#
# user_nums = set(map(int, nums))
#
# # for strings in nums:
# #     user_nums.append(int(strings))
#
# user_nums = set(user_nums)
#
# my_set = set()
#
# for _ in range(13):
#     my_set.add(random.randint(1, 100))
#
# print(f'Минимальное число пользователя: {min(user_nums)}; максимальное число пользвателя: {max(user_nums)}')
#
# print(f'Уникальные числа пользователя: {user_nums.difference(my_set)}')
#
# print(f'Общие числа пользователя, которые есть среди случайных: {user_nums.intersection(my_set)}')
#
# print(f'Числа, которые есть или там или там: {user_nums.union(my_set)}')


# 2

# guests = ["Олена", "Ігор", "Марія", "Олена", "Ігор", "Сергій"]
# event = "День народження"
#
#
# def send_invitation(lst, string):
#     new_set = set(lst)
#
#     result = []
#
#     for element in new_set:
#         result.append(f'{element}, приглашаю Вас на {string}')
#
#     return result
#
#
# print(send_invitation(lst=guests, string=event))

# 3

# def lists_to_set(list1, list2):
#     print(f'Товары, которые можно купить вместе: {set(list1).union(set(list2))}')
#
#     print(f'Товары, которые нужны первому человеку: {set(list1).difference(set(list2))}')
#
#     print(f'Товары, которые нужны второму человеку: {set(list2).difference(set(list1))}')
#
#
# lists_to_set(list1=["молоко", "хліб", "кава", "яблука", "чай"], list2=["кава", "сир", "хліб", "банани"])


# 4

# registered = ["Анна", "Богдан", "Олег", "Марина", "Світлана"]
# paid = ["Олег", "Марина", "Катерина", "Світлана"]
# confirmed = ["Олег", "Катерина", "Марина", "Іван"]
#
#
# def lists_to_set(list1, list2, list3):
#     print(f'Те, кто зарегистрировались, но не оплатили участие: {set(list1).difference(set(list2))}')
#
#     print(f'Те, кто подтвердил присутствие, но не зарегистрировался: {set(list3).difference(set(list1))}')
#
#     print(f'Те, кто оплатил участие, но не подтвердил присутствие: {set(list2).difference(set(list3))}')
#
#     print(f'Те, кто зарегистрировались и оплатили участие: {set(list1) & (set(list2))}')
#
#     print(f'Те, кто прошли все три этапа: {set(list1) & (set(list2)) & (set(list3))}')
#
#
# lists_to_set(registered, paid, confirmed)


# 5

# all_employees = ["Андрій", "Оксана", "Юрій", "Олексій", "Ірина", "Ігор", "Софія", "Марія"]
#
# group1 = ["Андрій", "Оксана", "Юрій"]
# group2 = ["Олексій", "Оксана", "Ірина"]
# group3 = ["Ігор", "Ірина", "Софія"]
#
# def check_lists(list1, list2, list3, list_set):
#     missing_names = []
#
#     groups_duplicates = []
#
#     # for name in list_set:
#     #     if name not in set(list1) | set(list2) | set(list3):
#     #         missing_names.append(name)
#
#         # elif name in set(list1) & set(list2) or set(list2) & set(list3) or set(list1) & set(list3):
#         #     groups_duplicates.append(name)
#
#     list_set = set(list_set)
#
#     missing_names = list_set - set(list1) - set(list2) - set(list3)
#
#     groups_duplicates = (set(list1) & set(list2)) | (set(list2) & set(list3)) | (set(list1) & set(list3))
#
#     print(f'Люди, которых нет в группах занятий: {missing_names}')
#
#     print(f'Люди, которые повторяются в группах: {groups_duplicates}')
#
#
# check_lists(group1, group2, group3, all_employees)


# Завдання 1
# Напишіть функцію, яка отримує 2 словника та об’єднує їх
# в один. Якщо ключі співпадають то потрібно додати
# відповідні їм значення.

# def merge_dicts(dict1, dict2):
#     result = dict1.copy()
#
#     # for key, value in dict1.items():
#     #     if key in result:
#     #         result[key] += value
#     #     else:
#     #         result[key] = value
#
#     for key, value in dict2.items():
#         if key in result:
#             result[key] += value
#         else:
#             result[key] = value
#
#     return result
#
# dic1 = {
#     "apple": 3,
#     "banana": 5,
#     "orange": 2
# }
#
# dic2 = {
#     "banana": 4,
#     "orange": 1,
#     "kiwi": 7
# }
# print(merge_dicts(dic1, dic2))

# Завдання 2
# Напишіть функцію, яка отримує словник та інвертує його,
# тобто повертає новий словник, де ключі та значення змінені
# місцями.


# def reverse_dict(dictionary):
#     result = {}
#
#     for key, value in dictionary.items():
#         result[value] = key
#
#     return result


# Завдання 3
# Користувач вводить назви товарів та їх ціни поки не введе
# порожній рядок. Збережіть дані у словник. Якщо користувач
# вводить товар повторно та треба додати стару та нову ціни.
# В кінці виведіть таблицею товар – ціна. Також виведіть
# загальну ціну.

# def get_item_and_prices():
#     print('Чтобы прекратить ввод, нажмите Enter')
#
#     result = {}
#
#     while True:
#         user_input_item= input('Введите товар: ')
#
#         if not user_input_item:
#             print('Ожидайте результаты!')
#             break
#
#         user_input_price = float(input('Введите цену на товар: '))
#
#         item = user_input_item
#         price = user_input_price
#
#         if item in result:
#             result[item] += price
#             continue
#
#         result[item] = price
#
#     all_values = result.values()
#
#     total_price = sum(all_values)
#
#     for key, value in result.items():
#         print(f'{key} --- {value} UAH')
#
#     print(f'Общая цена: {total_price}')
#
#
# get_item_and_prices()


# Завдання 4
# Напишіть функцію, яка отримує текст та повертає
# словник, де ключі – це слова, а значення – їхня кількість в
# тексті.
# Добавте параметр за замовчуванням який визначає, чи
# значення в словнику будуть кількостями слів, чи
# частотою(відсотком від загальної кількості).


# def convert_str(string):
#     string = string.replace(',', '').replace('.', '').replace(':', '').replace('!', '').replace('?', '').lower()
#
#     words = string.split(' ')
#
#     result = {}
#
#     for word in words:
#         if word in result:
#             result[word] += 1
#             continue
#
#         result[word] = 1
#
#     return result
#
#
# print(convert_str("apple banana APPLE orange banana kiwi apple"))

# Завдання 5
# Створіть словник, де ключі – це назви груп, а значення –
# списки студентів, що належать до цих груп.
# Реалізуйте 3 функції для додавання та видалення студентів
# з груп, а також для виведення даних на екран

# groups = {
#     "IT-01": ["Анна", "Богдан", "Катерина"],
#     "DS-02": ["Марія", "Іван", "Олег"],
#     "ME-03": ["Тарас", "Юлія", "Оксана", "Артем"],
# }
#
# def add_student(dictionary):
#     user_group_choice = input('Введите название группы, в которую хотите добавить студента: ').strip()
#
#     if user_group_choice not in dictionary:
#         print('Введите группу из доступных')
#         return
#
#     new_student = input('Введите имя нового студента: ').strip()
#
#     dictionary[user_group_choice].append(new_student)
#
#
# def delete_student(dictionary):
#     user_group_choice = input('Введите название группы, из которой хотите удалить студента: ').strip()
#
#     if user_group_choice not in dictionary:
#         print('Введите группу из доступных')
#         return
#
#     student_to_delete = input('Введите имя студента, которого хотите удалить: ').strip()
#
#     if student_to_delete not in dictionary[user_group_choice]:
#         print('Такого студента нет в этой группе')
#         return
#
#     dictionary[user_group_choice].remove(student_to_delete)
#
#
# def show_data(dictionary):
#     for key, value in dictionary.items():
#         print(f'Группа {key}: {', '.join(value)} ')
#
#
# delete_student(groups)
# show_data(groups)

# Завдання 6
# Напишіть функцію, яка запитує в користувача ім’я, вік,
# посаду та повертає ці дані у вигляді словника.
# Створіть іншу функцію, яка добавляє 5 людей у словник,
# де ключ ім’я, а значення – словник з попередньої функції.
# Після чого виведіть середній вік.

# def create_user():
#     user_name = input('Введите имя: ').strip()
#     if not isinstance(user_name, str):
#         print('Неверный формат')
#         return
#
#     user_age = input('Введите возраст: ').strip()
#     try:
#         user_name = int(user_age)
#     except TypeError:
#         print('Введите целое число')
#         return
#
#     user_position = input('Введите должность: ').strip()
#     if not isinstance(user_position, str):
#         print('Неверный формат')
#         return
#
#     result = {
#               'Имя': user_name,
#               'Возраст': user_age,
#               'Должность': user_position
#               }
#
#     for key, value in result.items():
#         print(f'{key}: {value}')
#
#
# create_user()

# Завдання 1
# Користувач вводить імена людей, поки не введе порожній
# рядок. Збережіть усі імена в множині. Якщо ім’я вводиться
# повторно, то вивести повідомлення про це.
# Виведіть кількість людей

# def add_people():
#     print('Чтобы остановить ввод, кликните Enter')
#
#     result = set()
#
#     while True:
#         user_input = input('Введите имя: ')
#
#         if not user_input:
#             break
#
#         if user_input in result:
#             print('Пользователь зарегистрирован')
#             continue
#
#         result.add(user_input)
#
#     print(len(result))
#
#     return result
#
#
# add_people()
        

# Завдання 2
# Студентів розбили на 2 групи, кожна з яких навчається у
# свій день. Перевірте чи не виникло помилки, а саме
#  Чи немає студентів які є в двох групах одночасно(якщо
# є, то вивести їх імена)
#  Чи немає студентів, про яких забули(якщо є, то вивести
# імена)
# Напишіть відповідну функцію, яка отримує два списки з
# іменами студентів кожної групи, та список усіх студентів.
# Додатково: змініть код, якщо груп 3

# group1 = ['Оля', 'Іван', 'Марія', 'Петро']
# group2 = ['Сергій', 'Іван', 'Анна', 'Олена']
# all_students = ['Оля', 'Іван', 'Марія', 'Петро', 'Сергій', 'Анна', 'Олена', 'Віктор', 'Альберт']
#
# def verify_groups(group_1: list, group_2: list, groups_set: list):
#     group_1 = set(group_1)
#     group_2 = set(group_2)
#     groups_set = set(groups_set)
#
#     if group_1 & group_2:
#         print(f'Студенты, которые есть в обеих группах: {', '.join(list(group_1 & group_2))}\n')
#     else:
#         print('Студентов в двух группах одновременно нет\n')
#
#     if groups_set - (group_1 | group_2):
#         print(f'Студенты, о которых забыли: {', '.join(list(groups_set - (group_1 | group_2)))}\n')
#     else:
#         print('Студентов, о которыъ забыли, нет\n')
#
#
# verify_groups(group1, group2, all_students)


# Завдання 3
# Є словник з цінами продуктів, де ключ – назва продукту, а
# значення – ціна за кг. Організуйте просту роботу магазину:
# користувач вводить назву продукту та вагу, потрібно вивести
# загальну ціну.

# prices = {
#     'яблука': 30.0,    # ціна за кг в гривнях
#     'банани': 25.5,
#     'апельсини': 28.0,
#     'картопля': 10.0,
#     'морква': 12.5
# }
#
# def get_receipt(items: dict):
#     print('Чтобы получить итоговый чек, нажмите Enter\n')
#
#     total_price = 0
#
#     while True:
#         item_choice = input('Введите товар: ').lower().strip()
#
#         if not item_choice:
#             return total_price
#
#         if item_choice not in items.keys():
#             print('Введите товар из ассортимента\n')
#             continue
#
#         item_weight = input('Введите вес товара: ').lower().strip().replace(',', '.')
#
#         try:
#             item_weight = float(item_weight)
#         except ValueError:
#             print('Неправильный формат записи\n')
#             continue
#
#         total_price += items[item_choice] * item_weight
#
#     return total_price
#
#
# print(get_receipt(prices))


# Завдання 4
# Є словник з інформацією про вміст вітаміну С в різних
# продуктах, де ключ – назва продукту, значення – вміст
# вітаміну С у мг. Користувач вводить свій раціон: список з
# назвами продуктів
# Обчисліть вміст вітаміну С в раціоні(якщо у словнику
# немає якогось продукту, вважайте вміст вітаміну рівним 0 мг).
# Виведіть продукт з найбільшим вмістом вітаміну С


# vitamin_c_content = {
#     "апельсин": 53,
#     "лимон": 77,
#     "полуниця": 59,
#     "яблуко": 5,
#     "шпинат": 28,
#     "капуста": 36,
#     "банан": 9,
# }
#
# def get_vit_c_info(products: dict):
#     print('Чтобы остановить ввод, кликните Enter\n''Продукты не могут повторяться\n')
#
#     total_vit_c_content = 0
#
#     added_products = []
#
#     while True:
#         user_data = input('Введите продукт: ').strip().lower()
#
#         if not user_data:
#             break
#
#         if user_data not in added_products:
#             added_products.append(user_data)
#         else:
#             print('Данный продукт был уже добавлен\n')
#             continue
#
#         if user_data in vitamin_c_content:
#             total_vit_c_content += vitamin_c_content[user_data]
#
#     return total_vit_c_content
#
#
# print(get_vit_c_info(vitamin_c_content))

# Завдання 5
# Склад футбольної команди розподіляється між такими
# позиціями:
#  воротар – 1
#  захисник – 4
#  півзахисник – 4
#  нападник – 2
# Користувач поступово вводить імена гравців та їх позиції.
# Потрібно зберегти ці дані у словник, де ключ – назва позиції,
# значення – список з іменами гравців на цю позицію. Перевірте
# чи склад команди правильний.
# Також виведіть імена всіх гравців.


# def complete_team():
#     positions_limits = {
#         'воротар': 1,
#         'захисник': 4,
#         'півзахисник': 4,
#         'нападник': 2
#     }
#
#     user_team_counter = {
#         'воротар': [],
#         'захисник': [],
#         'півзахисник': [],
#         'нападник': []
#     }
#
#     total_players = 0
#
#     while total_players < 11:
#         new_player = input('Введите имя нового игрока: ').strip().capitalize()
#
#         player_position = input('Введите позицию игрока: ').strip().lower()
#
#         if player_position in user_team_counter:
#             user_team_counter[player_position].append(new_player)
#             total_players += 1
#
#     for position, players in user_team_counter.items():
#         if len(players) != positions_limits[position]:
#             return False
#
#     return True
#
#
# print(complete_team())


# Користувач вводить список книг, які він прочитав. Є словник з назвами авторів та їхніми книгами.
# Визначте, скільки книг кожного автора користувач прочитав, і хто з авторів — його улюблений.

# authors_books = {
#     "Стівен Кінг": ["Сяйво", "Кладовище домашніх тварин", "Воно"],
#     "Джоан Роулінг": ["Гаррі Поттер і філософський камінь", "Гаррі Поттер і таємна кімната"],
#     "Ернест Гемінґвей": ["Старий і море", "По кому подзвін"],
#     "Рей Бредбері": ["451° за Фаренгейтом", "Кульбабове вино"]
# }
#
# read_books = [
#     "Сяйво",
#     "Гаррі Поттер і філософський камінь",
#     "Гаррі Поттер і таємна кімната",
#     "451° за Фаренгейтом",
#     "Старий і море",
# ]
#
# def favorite_book(author_book: dict, user_books: list):
#     preferences = []
#
#     for book in user_books:
#         for author, books in author_book.items():
#             if book in books:
#                 preferences.append(author)
#
#     top = []
#
#     for preference in preferences:
#         top.append((preference, preferences.count(preference)))
#
#     top = list(set(top))
#
#     top.sort(key=lambda couple: couple[1], reverse=True)
#
#     print(f'Любимый автор - {top[0][0]}\n')
#
#     for couple in top:
#         print(f'{couple[0]} - {couple[1]} книга (-и)')
#
#
# favorite_book(authors_books, read_books)

# or

# preferences = {}
#
#     for book in user_books:
#         for author, books in author_book.items():
#             if book in books:
#                 preferences[author] = preferences.get(author, 0) + 1
#
#     top_author = max(preferences.items(), key=lambda item: item[1])
#
#     print(f'Любимый автор - {top_author[0]}\n')


# def generate_password(length: int=12, use_uppercase: bool=True, use_digits: bool=True, use_special: bool=True, use_lowercase: bool=True):
#     import random
#     import string
#
#     uppercase_letters = list(string.ascii_uppercase)
#     lowercase_letters = list(string.ascii_lowercase)
#     digits = list(string.digits)
#     special_characters = list(string.punctuation)
#
#     all_parameters = (length, use_special, use_digits, use_uppercase, use_lowercase)
#
#     if length <= 0:
#         raise ValueError("Password can not have zero characters")
#     elif not any(all_parameters[1:]):
#         raise ValueError("No character types selected!")
#
#     what_to_use = []
#
#     if use_uppercase:
#         what_to_use.append(uppercase_letters)
#     if use_lowercase:
#         what_to_use.append(lowercase_letters)
#     if use_digits:
#         what_to_use.append(digits)
#     if use_special:
#         what_to_use.append(special_characters)
#
#     what_to_use_str = ''
#
#     for types in what_to_use:
#         for char in types:
#             what_to_use_str += char
#
#     password = ''
#
#     for _ in range(length):
#         password += random.choice(what_to_use_str)
#
#     return password
#
# print(generate_password(use_uppercase = False, use_digits = False, use_special = False, use_lowercase = False, length=0))


# 5. Словарь синонимов
# 💬 Пользователь вводит слово, и программа находит его синонимы, если они есть в словаре. Если нет — предлагает добавить.

# synonyms = {
#     "быстрый": ["скорый", "проворный", "резвый"],
#     "умный": ["разумный", "интеллектуальный", "смышлёный"]
# }
#
# def check_synonyms(data: dict):
#     data_lists = []
#
#     for word, rest_words in data.items():
#         data_lists.append([word] + rest_words)
#
#     print('Чтобы показать словарь, впишите слово "словарь"\n')
#
#     while True:
#         user_word = input('Напишите слово: ').strip().lower()
#
#         if user_word == 'словарь':
#             print(data)
#             print()
#             continue
#
#         for synonyms_list in data_lists:
#             if user_word in synonyms_list:
#                 output = synonyms_list.copy()
#
#                 output.remove(user_word)
#
#                 print(f'Синонимы слова "{user_word}": {', '.join(output)}')
#
#                 continue
#
#             else:
#                 user_request = input('Такого слова нет в словаре синонимов. Хотите добавить синонимы? ').strip().lower()
#
#                 if user_request == 'да':
#                     user_new_syns = input("Введите синонимы через запятую: ").strip().lower()
#
#                     syns = user_new_syns.split(', ')
#
#                     data.update({user_word: syns})
#
#                     break
#
#                 elif user_request == 'нет':
#                     break
#
#         continue
#
#
# check_synonyms(synonyms)


# 6. Валидатор email-адресов
# 📧 Проверяет, что email корректный по структуре: одна "@" + домен + разрешённые символы.

# user.name123@gmail.com

# def validate_email(data: str):
#     if data.count('@') != 1:
#         return False
#
#     special_syms = ('.', '_', '-')
#
#     name_invalid = ''
#
#     for sym in data:
#         if sym == '@':
#             break
#         name_invalid += sym
#
#     if not name_invalid:
#         return False
#
#     if name_invalid.startswith(special_syms) or name_invalid.endswith(special_syms):
#         return False
#
#     for i in range(len(name_invalid)):
#         if name_invalid[i] in special_syms and name_invalid[i + 1] in special_syms:
#             return False
#
#         if not (name_invalid[i].isalnum() or name_invalid[i] in special_syms):
#             return False
#
#     name_valid = name_invalid
#
#     no_name_data = data.removeprefix(name_valid)
#
#     if not '.' in no_name_data:
#         return False
#
#     domain_invalid = ''
#
#     for sym in no_name_data:
#         if sym == '.':
#             break
#         domain_invalid += sym
#
#     print(domain_invalid)
#
#     if domain_invalid.startswith('@-') or domain_invalid.endswith('-'):
#         return False
#
#     for i in range(1, len(domain_invalid)):
#         if domain_invalid[i] in '.' and domain_invalid[i + 1] in '.':
#             return False
#
#         if not (domain_invalid[i].isalnum() or domain_invalid[i] in '-') and not domain_invalid[i].islower():
#             return False
#
#     domain_valid = domain_invalid
#
#     domain_zone_invalid = data.removeprefix(name_valid + domain_valid)
#
#     if not domain_zone_invalid or len(domain_zone_invalid) < 3:
#         return False
#
#     for i in range(1, len(domain_zone_invalid)):
#         if not domain_zone_invalid[i].isalpha() and not domain_zone_invalid[i].islower():
#             return False
#
#
#     return True
#
#
# # print(validate_email('user.name123@gmail.com'))
# # print(validate_email('user.name123@gmail.com'))     # True
# # print(validate_email('vlad_work-22@openai.org'))    # True
# # print(validate_email('test.user@edu.pl'))           # True
# print(validate_email('name99@sub.domain.co.uk'))    # True
# # print(validate_email('m.y_n-a.m-e@service.ai'))     # True
# # print()
# # print(validate_email('user@@gmail.com'))            # False (две @)
# # print(validate_email('@gmail.com'))                 # False (пустое имя)
# # print(validate_email('vlad@'))                      # False (нет домена)
# # print(validate_email('vlad@gmail'))                 # False (нет доменной зоны)
# # print(validate_email('vlad..test@mail.com'))        # False (две точки подряд)
# # print(validate_email('vlad@-mail.com'))             # False (домен начинается с -)
# # print(validate_email('vlad@mail.'))                 # False (нет зоны)
# # print(validate_email('user@domain.c'))              # False (зона слишком короткая)
# # print(validate_email('user@domain.123'))
# print(validate_email('name99@sub.domain.co.uk'))


# повторение
# Дана строка s. Нужно найти длину самой длинной подстроки без повторяющихся символов.


# def longest_unique_substring(data: str):
#     all_uniques = [[data[0]]]
#
#     symbol_i = 1
#
#     while True:
#         if symbol_i == len(data):
#             break
#
#         if data[symbol_i] not in all_uniques[-1]:
#             all_uniques[-1].append(data[symbol_i])
#             symbol_i += 1
#         else:
#             all_uniques.append([data[symbol_i]])
#             symbol_i += 1
#
#     return len(max(all_uniques, key=lambda sub: len(sub)))
#
#
# print(longest_unique_substring('abcbde')) # почти

# Завдання 1
# Є список з товарами. Користувач вводить індекс товару,
# який треба вивести. Обробіть виняток

# products = ["хліб", "молоко", "сир", "масло", "яйця"]
#
# def get_index(data: list):
#     while True:
#
#         try:
#             ind = int(input('Введите индекс: '))
#         except ValueError:
#             print('Введите целое число\n')
#             continue
#
#         try:
#             return data[ind]
#         except IndexError:
#             print('Элемента с таким индексом нет\n')
#             continue
#
#
# print(get_index(products))


# Завдання 2
# Напишіть функцію, яка запитує користувача вік та
# повертає його. Якщо вік неправильний(<0 або >130)
# викликати виняток ValueError.
# Написати код try … except який використовує дану
# функцію.

# def get_age(verbose=True):
#     while True:
#         try:
#             age = int(input('Введите свой возраст: '))
#         except ValueError:
#             print('Введите целое число\n')
#             continue
#
#
#         if age < 0 or age > 130:
#             raise ValueError('Введите возраст в диапазоне от 0 до 130\n')
#
#         if verbose:
#             print(age)
#
#         return age
#
#
# get_age()

# Завдання 3
# Напишіть функцію, яка запитує користувача номер
# телефону та повертає його. Якщо номер не вірний, тобто не
# починається з +038 або в ньому не 11 символів то викликати
# виняток ValueError.
# Написати код try … except який використовує дану
# функцію.

# def get_phone_num(verbose=True):
#     while True:
#         phone_number = input('Введите номер телефона в формате (+038********): ').strip()
#
#         if len(phone_number) != 11 and not phone_number.startswith('+038'):
#             raise ValueError('Номер должен содержать 11 знаков и начинаться с "+038"')
#
#         try:
#             phone_number_int = int(phone_number)
#         except ValueError:
#             print('Неверный формат записи')
#             continue
#
#         if verbose:
#             print(f'Номер {phone_number} действителен')
#
#         return phone_number
#
#
# get_phone_num(verbose=True)


# Завдання 4
# Організуйте фільтр товарів в онлайн магазині. Усі товари
# діляться на певні категорії, причому один і той самий товар
# може відноситись до різних категорій. Є словник, де ключі –
# назви категорій, а значення – множини з товарами цієї
# категорії.
# Користувач вводить 2 категорії, виведіть ті товари, які
# відносяться одночасно до цих двох категорій.
# Обробіть виняток коли категорії немає в словнику.
# Додатково: змініть код якщо користувач вводить декілька
# категорій.

# categories = {
#     "електроніка": {"ноутбук", "смартфон", "планшет", "телевізор"},
#     "побутова техніка": {"пилосос", "телевізор", "праска", "пральна машина"},
#     "мобільні пристрої": {"смартфон", "планшет", "розумний годинник"},
#     "комп'ютери": {"ноутбук", "монітор", "клавіатура", "мишка"},
#     "гаджети": {"смартфон", "розумний годинник", "ноутбук"}
# }
#
# def get_common(data: dict, verbose=True):
#     while True:
#         category1 = input('Введите первую категорию: ')
#
#         try:
#             category1_items = data[category1]
#         except KeyError:
#             print(f'Категории {category1} нет\n')
#             continue
#
#         category2 = input('Введите вторую категорию: ')
#
#         try:
#             category2_items = data[category2]
#         except KeyError:
#             print(f'Категории {category2} нет\n')
#             continue
#
#         if verbose:
#             print(f'Товары из категорий {category1} и {category2}: {', '.join(category1_items & category2_items)}')
#
#         return category1_items & category2_items
#
#
# get_common(categories)
# пока только для двух сделал, хотел 5 задание успеть


# Завдання 5
# Організуйте базу даних «Співробітники». Усі дані мають
# зберігатись у словнику де ключ – ім’я людини, значення –
# зарплата. Реалізуйте такий функціонал(через функції):
#  Вивести дані на екран
#  Добавити співробітника
#  Видалити співробітника
#  Показати зарплату співробітника
#  Змінити зарплату співробітнику
# У випадку некоректних даних функції повинні викликати
# винятки з описом помилки

# employees = {
#     "Олена": 18000,
#     "Ігор": 22000,
#     "Марія": 20000,
#     "Андрій": 25000,
#     "Світлана": 21000
# }
#
# def input_employee():
#     while True:
#         employee = input('Введите имя сотрудника: ').capitalize().strip()
#
#         if not employee.isalpha():
#             print('Введите только буквы')
#         else:
#             break
#
#     return employee
#
#
# def input_salary():
#     while True:
#         salary = input('Впишите сумму, на которую хотели бы изменить сумму зарплата сотрудника')
#
#         if not salary.isdigit():
#             print('Введите только цифры')
#         else:
#             break
#
#     return int(salary)
#
# def add_employee(data: dict):
#     while True:
#         name = input_employee()
#
#         if name in employees:
#             print('Такой сотрудник уже есть')
#         else:
#             data[name] = 0
#             print(f'Сотрудник {name} добавлен')
#             break
#
#
# def remove_employee(data: dict):
#     while True:
#         name = input_employee()
#
#         if name not in employees:
#             print('Такого сотрудника нет')
#         else:
#             data.pop(name)
#             print(f'Сотрудник {name} удален')
#             break
#
#
# def change_salary(data: dict):
#     while True:
#         name = input_employee()
#
#         if name not in employees:
#             print('Такого сотрудника нет')
#         else:
#             salary = input_salary()
#
#             if data[name] == salary:
#                 print("Вы ввели ту же зарплату")
#             else:
#                 data[name] = salary
#                 print('Зарплата изменена')
#                 break


# Завдання 1
# Є текстовий файл. Виведіть кількість рядків та кількість
# символів в ньому

# def show_sym_count(file_name: str):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         content = f.read()
#
#         content = content.replace('\n', '')
#
#         return len(content)


# Завдання 2
# Користувач вводить ім’я та вік. Запишіть їх у файл. Назву
# файлу також вводить користувач(без розширення .txt)


# def get_data():
#     try:
#         user_name = input('Введите имя: ').strip().capitalize()
#         if not user_name.isalpha():
#             raise ValueError('Введите только буквы')
#
#         user_age = input('Введите возраст: ').strip()
#         if not user_age.isdigit():
#             raise ValueError('Введите только цифры')
#
#         file_name = input('Введите имя файла (без расширения): ').strip()
#         if file_name.endswith('.txt'):
#             raise ValueError('Введите имя файла без расширения')
#
#         with open(file=f'{file_name}.txt', mode='w', encoding='utf-8') as new_file:
#             new_file.write(f'{user_name}: {user_age} года/лет')
#
#     except ValueError as err:
#         print(f'Ошибка: {err}')
#
#
# get_data()


# Завдання 3
# Є текстовий файл. Запишіть його рядки в інший файл.

# def get_lines(file_name: str):
#     with open(file_name, 'r', encoding='utf-8') as source_file:
#         lines = source_file.readlines()
#
#     with open('lines_file.txt', 'w', encoding='utf-8') as new_file:
#         # for line in lines:
#         #     new_file.write(line)
#         new_file.writelines(lines)
#
#
# get_lines('log.txt')

# Завдання 4
# Користувач вводить літеру та назву файлу. Виведіть усі
# слова з файлу, які починаються на цю літеру.


# def get_words_start_with(verbose=True):
#     try:
#         file_name = input('Введите имя файла с расширением: ').strip()
#         if not file_name.endswith('.txt'):
#             raise ValueError('Введите имя файла с расширением')
#
#         target_letter = input('Введите букву: ').strip().lower()
#         if len(target_letter) != 1 and not target_letter.isalpha():
#             raise ValueError('Введите одну букву')
#
#         with open(file=file_name, mode='r', encoding='utf-8') as file:
#             content = file.read()
#
#         content = content.replace('\n', ' ')
#
#         words = content.split()
#
#         result = []
#
#         for word in words:
#             if word.lower().startswith(target_letter):
#                 result.append(word)
#
#         if verbose:
#             print(result)
#
#         return result
#
#     except ValueError as err:
#         print(f'Ошибка: {err}')
#
#
# get_words_start_with(verbose=True)


# Завдання 5
# Є текстовий файл. Замініть у ньому усі символи * на &, та
# навпаки.


# def replace_chars(file_name: str):
#     with open(file_name, 'r') as file:
#         content = file.read()
#
#     result = ''
#
#     for char in content:
#         if char == '*':
#             result += '&'
#
#         elif char == '&':
#             result += '*'
#
#         else:
#             result += char
#
#     with open('new_file.txt', 'w') as new_file:
#         new_file.write(result)
#
#
# replace_chars('log.txt')


# Завдання 6
# Напишіть функцію, яка отримує назву файлу та список
# чисел як параметри. Потрібно записати всі числа у файл,
# розмістивши кожне число на окремому рядку.
# Напишіть іншу функцію, яка отримує назву файл та читає
# з нього ці числа і повертає як список.

# def get_digits_to_file(file_name: str, data: list):
#     if not file_name.endswith('.txt'):
#         print('Неверный формат файла')
#         return
#
#     if not data:
#         print('Введите список чисел')
#         return
#
#     with open(file_name, 'w') as new_file:
#         for dig in data:
#             new_file.write(f'{dig}\n')
#
#
# def get_txt_to_list(file_name: str):
#     try:
#         with open(file_name, 'r') as src_file:
#             content = src_file.read()
#
#         result = []
#
#         for line in content.splitlines():
#             result.append(int(line))
#
#         print(result)
#
#     except FileNotFoundError:
#         print('Файл не найден')
#
#
#
# get_digits_to_file('digits.txt', [1, 2, 3])
#
#
# get_txt_to_list('digits.txt')


# Завдання 7
# Є 2 файли, запишіть у третій файл лише ті символи, які є в
# обох файлах одночасно


# def get_common(file1_name: str, file2_name: str):
#     with open(file1_name, 'r', encoding='utf-8') as file1:
#         file1_content = file1.read()
#
#     with open(file2_name, 'r', encoding='utf-8') as file2:
#         file2_content = file2.read()
#
#     file1_set = set(file1_content)
#     file2_set = set(file2_content)
#
#     common_chars = file1_set.intersection(file2_set)
#
#     res_str = str(common_chars)[1:-1].replace("'", '')
#
#     with open('common_chars.txt', 'w', encoding='utf-8') as new_file:
#         new_file.write(res_str)
#
#
# get_common('vlad.txt', 'log.txt')


# def chat(message: str):
#     message = input()
#
#     if message.capitalize() == 'Привет':
#         print('Привет! Как дела?')
#     elif message.capitalize() == 'Пока':
#         print('До встречи!')
#     else:
#         print('Я тебя не понял')
#
#
# def get_command(command: str):
#     command = input()
#
#     if command == '/start':
#         print('Бот успешно запущен')
#
#     elif command == '/help':
#         print('Здесь должно быть описание функционала бота')


# def process_input(text: str):
#     if text.startswith('/'):
#         get_command(text)
#     else:
#         get_response(text)


# import random
# import string
#
# password = ''
#
# for _ in range(12):
#     password += random.choice(string.punctuation + string.digits + string.ascii_lowercase + string.ascii_uppercase)
#
# print(password) # X(i_JP9ROnfC
































