import random

while True:
    cell_amount = input('Введите число клеток (например, 9, 16, 25 и т.д.)\n')
    print()

    if not cell_amount.isdigit():
        print('Введите целое число!')
        continue

    cell_amount = int(cell_amount)

    edge = int(cell_amount ** 0.5) # длина поля

    coordinates = []

    cell_template = [] # [x, y]

    raw_template = []

    raw_counter = ['_']

    def add_raw():
        for i in range(1, edge + 1):
            cell = []

            cell.append(i)

            cell.append(len(raw_counter))

            raw_template.append(cell)

        raw_counter.append('_')


    for _ in range(edge):
        add_raw()

    bomb_amount = int(random.randint(1, int(cell_amount/edge)))

    coordinates = raw_template

    random_indexes = []

    while len(random_indexes) < bomb_amount:
        random_index = random.randint(1, cell_amount)

        if random_index not in random_indexes:
            random_indexes.append(random_index)

    for i in random_indexes:
        coordinates[i - 1] = 'bomb'

    used_coordinates = []

    print(f'На поле {bomb_amount} бомб\n')

    while True:
        click_coordinates = []

        x_str, y_str = input("Введите координаты через пробел (например, 2 3): ").split()

        x = int(x_str)

        y = int(y_str)

        click_coordinates.append(x)

        click_coordinates.append(y)

        if click_coordinates in coordinates:
            print('Здесь нет бомбы')
            used_coordinates.append(click_coordinates)
        else:
            print('Вы взорвались! Удачи в следующей игре!')
            break