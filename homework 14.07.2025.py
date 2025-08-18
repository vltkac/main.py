clients = {
    "Анна": 1500,
    "Богдан": 3000,
    "Катерина": 500,
    "Дмитро": 0
}

def deposit_money(data):
    client = input('Введите имя клиента: ').strip()
    for sym in client:
        if sym.isdigit():
            print('Неправильный формат записи\n')
            return

    funds_to_add = input('Введите сумму для пополнения: ').strip().replace(',', '.')
    try:
        funds_to_add = float(funds_to_add)
    except ValueError:
        print('Неправильный формат записи\n')
        return

    if client in data:
        data[client] += funds_to_add
        print('Операция выполнена успешно\n')
    else:
        data[client] = funds_to_add
        print('Новый пользователь добавлен. Операция выполнена успешно\n')


def withdraw_money(data):
    client = input('Введите имя клиента: ').strip()
    for sym in client:
        if sym.isdigit():
            print('Неправильный формат записи\n')
            return

    if client not in data:
        print('Клиент не найден\n')
        return

    funds_to_withdraw = input('Введите сумму для снятия: ').strip().replace(',', '.')
    try:
        funds_to_withdraw = float(funds_to_withdraw)
    except ValueError:
        print('Неправильный формат записи\n')
        return

    if funds_to_withdraw > data[client]:
        print('Недостаточно средств для снятия\n')
        return
    else:
        data[client] -= funds_to_withdraw
        print('Операция выполнена успешно\n')


def main():
    print('Добро пожаловать в приложение банка!')
    print('Чтобы пополнить счет, нажмите (1)    Чтобы снять деньги, нажмите (2)    Чтобы завершить действие программы, нажмите (3)\n')

    while True:
        user_choice = input('Ваш выбор: ')

        try:
            user_choice = int(user_choice)
        except ValueError:
            print('Неверный формат записи\n')
            continue

        if user_choice == 1:
            deposit_money(clients)
        elif user_choice == 2:
            withdraw_money(clients)
        elif user_choice == 3:
            print('Спасибо, что пользуетесь нашими услугами. Хорошего дня!')
            return
        else:
            print('Неправильная опция\n')