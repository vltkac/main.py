# 1.1

number1 = float(input("Please submit first number: "))
number2 = float(input("Please submit second number: "))
number3 = float(input("Please submit third number: "))

summa = number1 + number2 + number3
multi = number1 * number2 * number3

operation = int(input("Please choose an operation: sum or multiplication (1 or 2) "))


if operation == 1:
    print(summa)

elif operation == 2:
    print(multi)

else:
    print("Wrong choice")

# 1.2

number1 = float(input("Please submit first number: "))
number2 = float(input("Please submit second number: "))
number3 = float(input("Please submit third number: "))

average = (number1 + number2 + number3) / 3

operation_choice = int(input("Please choose operation: max, min or average (1-3)"))

if operation_choice == 1:

    if number1 > number2 and number1 > number3:
        print(number1)

    elif number2 > number1 and number2 > number3:
        print(number2)

    elif number3 > number2 and number3 > number1:
        print(number3)

elif operation_choice == 2:

    if number1 < number2 and number1 < number3:
        print(number1)

    elif number2 < number1 and number2 < number3:
        print(number2)

    elif number3 < number2 and number3 < number1:
        print(number3)

# max_number = max(number1, number2, number3)
# print(max_number)
# min_number = min(number1, number2, number3)
# print(min_number)
#
# Я бы использовал принты этих комманд, но мы их еще не проходили))

elif operation_choice == 3:

    print(average)

else:
    print("Wrong choice")

# 2.3

grade = int(input("Введите оценку от 1 до 5 "))

if grade == 1:
    print("Очень плохо")

elif grade == 2:
    print("Плохо")

elif grade == 3:
    print("Удовлетворительно")

elif grade == 4:
    print("Хорошо")

elif grade == 5:
    print("Идеально")

2.4

metr = float(input("Введите количество метров: "))

k_milya = 1609.344
k_dyjm = 0.0254
k_yard = 0.9144


# 1 миля = 1 609.344 метра
# 1 дюйм = 0.0254 метра
# 1 ярд = 0.9144 метра


metr_milya = metr / k_milya
metr_dyjm = metr / k_dyjm
metr_yard = metr / k_yard

metr_km = metr / 1000
metr_sm = metr * 100


user_option = int(input("Выберите варианты перевода: перевести в одну из единиц по выбору: мили, дюймы или ярды; перевести сразу во все три единицы и вывести результаты для каждой; перевести в километры и сантиметры (1-3) "))

if user_option == 1:
    user_choice = int(input("Выберите: миля, дюйм, ярд (1-3) "))
    if user_choice == 1:
        print(f"{metr_milya} миль")
    elif user_choice == 2:
        print(f"{metr_dyjm} дюймов")
    elif user_choice == 3:
        print(f"{metr_yard} ярдов")

elif user_option == 2:
    print(f"{metr_milya} миль")
    print(f"{metr_dyjm} дюймов")
    print(f"{metr_yard} ярдов")

elif user_option == 3:
    print(f"{metr_km} километров")
    print(f"{metr_sm} сантиметров")

else:
    print("Неверный выбор")