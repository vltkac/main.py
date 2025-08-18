# 1

price = float(input("Введите цену за единицу товара "))
item_qty = int(input("Введите количество товара "))

total_cost = price * item_qty

discount = 0.1

if total_cost >= 500 or item_qty >= 10:
    print(f"Сумма к оплате {total_cost - (total_cost * discount):.2f}")

else:
    print(f"Сумма к оплате {total_cost:.2f}")

# 2

grade1 = float(input("Введите первую оценку "))
grade2 = float(input("Введите вторую оценку "))

if grade1 >= 0 and grade2 >= 0:
    if grade1 >= 60 and grade2 >= 60:
        print("Сдал")

    elif grade1 >= 60 or grade2 >= 60:
        print("Пересдача")

    elif grade1 < 60 and grade2 < 60:
        print("Не сдал")
else:
    print("Результат не может быть отрицательным")

# 3

year = int(input("Введите год "))

if year % 4 == 0 and year % 100 != 0:
    print("Год високосный")

else:
    print("Год не високосный")

# 4

credit = float(input("Введите сумму кредита в долларах "))
year = int(input("Введите термин в годах "))
amount_of_month = year * 12

if credit >= 0 and year > 0:

    if credit <= 10000 and year <= 3:
        percent = 8
    elif credit <= 10000 and year > 3:
        percent = 10
    elif 10001 <= credit <= 50000:
        percent = 12
    elif credit > 50000:
        percent = 20

    total = credit * (1 + percent / 100) ** (year)

    print(f"Ваша процентная ставка по кредиту {percent} %")
    print(f"Ваша общая сумма кредита {total:.2f} $")
    print(f"Ваша месячная оплата {total / amount_of_month:.2f} $")

else:
    print("Введите корректные значения")



