# 1

# def get_unique_list():
#     user_input = input('Введите список товаров через запятую: ')
#
#     items = user_input.split(',')
#
#     items = list(map(lambda string: string.strip(), items))
#
#     for item in items:
#         if item.isdigit():
#             return 'Введите название товара'
#
#     result = list(set(items))
#
#     return result
#
#
# print(get_unique_list())

# 2

# received_coupons = ['Анна', 'Богдан', 'Катерина', 'Іван', 'Марія', 'Олег']
#
# used_coupons = ['Катерина', 'Олег', 'Ірина', 'Іван', 'Сергій']
#
# def analyze_customers(received, used):
#     set_received = set(received)
#
#     set_used = set(used)
#
#     received_but_not_used_names = set_received.difference(set_used)
#
#     received_but_not_used_amount = len(received_but_not_used_names)
#
#     fraud_names = set_used.difference(set_received)
#
#     print(f'Те, кто получил купон, но не воспользовался им: {', '.join(list(received_but_not_used_names))}\nИх количество: {received_but_not_used_amount}')
#
#     print(f'Имена мошенников: {', '.join(list(fraud_names))}')
#
#
# analyze_customers(received_coupons, used_coupons)