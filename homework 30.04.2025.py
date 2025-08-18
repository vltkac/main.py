#1.1

x1 = input("Please enter first number:")
x2 = input("Please enter second number:")
x3 = input("Please enter third number:")

x1 = float(x1)
x2 = float(x2)
x3 = float(x3)

sum = x1 + x2 + x3
multi = x1 * x2 * x3

print(f"Sum of your numbers:{sum}")
print(f"Multiplication of your numbers:{multi}")

#1.2

diagonal1 = input("Пожалуйста, введите длину первой диагонали:")
diagonal2 = input("Пожалуйста, введите длину второй диагонали:")

diagonal1 = float(diagonal1)
diagonal2 = float(diagonal2)

area = diagonal1 * diagonal2 * 0.5

print(f"Площадь ромба = {area}")

#2.3

zarplata = input("Пожалуйста, введите Вашу зарплату за месяц:")
kredit = input("Пожалуйста, введите Ваш месячный платеж по кредиту:")
dolg = input("Пожалуйста, введите Вашу задолженность за коммунальные услуги:")

zarplata = float(zarplata)
kredit = float(kredit)
dolg = float(dolg)

ostatok = zarplata - kredit - dolg

print(f"Сумма после всех оплат = {ostatok}")

#2.4

rasstoyanie = input("Пожалуйста, введите расстояние в километрах:")
rashod = input("Пожалуйста, введите расход бензина в литрах Вашего автомобиля на 100 км:")
cena = input("Пожалуйста, введите актуальную цену за литр бензина:")

rasstoyanie = float(rasstoyanie)
rashod = float(rashod)
cena = float(cena)

#формула: стоимость поездки = количество км * расход * цена / 100

stoimost = rasstoyanie * rashod * cena / 100

print(f"Стоимость бензина израсходованного во время Вашей поездки: {stoimost}")

#3.5

check = input("Пожалуйста, введите сумму счета:")
gosti = input("Пожалуйста, введите количество гостей:")

check = float(check)
gosti = int(gosti)

chaevye = check * 0.15
chaevye = float(chaevye)

print(f"Чаевые за Ваш счет: {chaevye}")

summa = check + chaevye
summa = float(summa)

print(f"Сумма (чаевые и счет): {summa}")

per_person = summa / gosti

print(f"С каждого гостя: {per_person}")




