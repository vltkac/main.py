# transactions = [
#     {"date": "2025-06-01", "amount": -45.0, "category": "groceries"},
#     {"date": "2025-06-03", "amount": -15.9, "category": "transport"},
#     {"date": "2025-06-05", "amount": 2500.0, "category": "salary"},
#     {"date": "2025-06-10", "amount": -120.0, "category": "restaurants"},
#     {"date": "2025-06-12", "amount": -80.0, "category": "groceries"},
# ]

# Задача:
# 1. Посчитай общие доходы и расходы
# 2. Выведи итоговый баланс
# 3. Посчитай траты по категориям -

# def analyze_transactions(lst):
#     total_spendings = 0
#     total_income = 0
#     total_balance = 0
#
#     for transaction in lst:
#         if transaction['amount'] < 0:
#             total_spendings += transaction['amount']
#
#         elif transaction['amount'] > 0:
#             total_income += transaction['amount']
#
#
#     total_balance = total_income + total_spendings
#
#     print(total_spendings, total_income, total_balance)
#
#
# analyze_transactions(transactions)


# Входные данные
client = {
    "age": 30,
    "income": 4000,
    "loan_amount": 10000,
    "has_debt": True,
    "late_payments": 3,
}

# Задача:
# Напиши функцию `calculate_score(client)`, которая:
# - начисляет базовые 100 баллов
# - -10 баллов за каждый пропущенный платёж
# - -20 баллов, если есть долг
# - +0.5 балла за каждый доллар дохода
# - -0.3 балла за каждый доллар кредита
# Возвращает score от 0 до 100 (обрезанный) и risk level ("Low", "Medium", "High")


# def calculate_score(dic):
#     score = 100 - 10 * dic['late_payments'] - 20 * dic['has_debt'] + 0.5 * dic['income'] - 0.3 * dic['loan_amount']
#
#     if score > 100:
#         score = 100
#     elif score < 0:
#         score = 0
#
#     if 80 <= score <= 100:
#         risk_level = 'Low'
#     elif 50 <= score < 80:
#         risk_level = 'Medium'
#     else:
#         risk_level = 'High'
#
#     return (score, risk_level)
#
#
# print(calculate_score(client))

# transactions = [
#     {"id": 1, "amount": 100, "country": "PL"},
#     {"id": 2, "amount": 15000, "country": "RU"},
#     {"id": 3, "amount": 8000, "country": "US"},
#     {"id": 4, "amount": 30000, "country": "KP"},
# ]
#
# # Задача:
# # Вывести список подозрительных транзакций:
# # - сумма > 10 000
# # - или страна из ['RU', 'KP', 'IR']
#
#
# def get_suspicious(lst):
#     susp = []
#
#     for transaction in lst:
#         if transaction['amount'] > 10000 or transaction['country'] in ['RU', 'KP', 'IR']:
#             susp.append(transaction)
#
#
#     return susp
#
#
# print(get_suspicious(transactions))


# clients = [
#     {"name": "Anna", "income": "х*й вам"},
#     {"name": "Bob", "income": 4500},
#     {"name": "Cathy", "income": "3,800"},
# ]
#
#
# def check_income(dic):
#     for cl in dic:
#         if not isinstance(cl['income'], (int, float)):
#             try:
#                 cl['income'] = cl['income'].replace(',', '')
#                 cl['income'] = float(cl['income'])
#             except ValueError:
#                 print(f"Клиент {cl['name']} ввел не число")
#
#     return dic
#
#
# print(check_income(clients))


# clients = [
#     {"name": "Anna", "debt": 100},
#     {"name": "Bob", "debt": 0},
#     {"name": "Cathy", "debt": 400},
# ]
#
# def avg_debt(dic):
#     return round(sum(cl['debt'] for cl in dic) / len(dic), 1)
#
#
# print(avg_debt(clients))

# Задача 2: Клиенты без долгов
# Напиши функцию no_debt_clients(clients), которая возвращает список имён клиентов, у которых долг равен 0.

# clients = [
#     {"name": "Anna", "debt": 100},
#     {"name": "Bob", "debt": 0},
#     {"name": "Cathy", "debt": 400},
#     {"name": "David", "debt": 200},
# ]
#
# def no_debt_clients(lst):
#     result = []
#
#     for cl in lst:
#         if not cl['debt']:
#             result.append(cl['name'])
#
#     return result
#
#
# print(no_debt_clients(clients))

clients = [
    {"name": "Anna", "debt": 100},
    {"name": "Bob", "debt": 0},
    {"name": "Cathy", "debt": 400},
    {"name": "David", "debt": 200},
    {"name": "Eva", "debt": 50},
    {"name": "Frank", "debt": 600},
]


def group_by_debt_level(lst):
    result = {}
    low = []
    med = []
    high = []

    for cl in lst:
        name = cl['name']
        debt = cl['debt']

        if debt < 100:
            low.append(name)
            result.update({'low': low})
        elif 100 <= debt < 300:
            med.append(name)
            result.update({'medium': med})
        elif 300 <= debt:
            high.append(name)
            result.update({'high': high})

    return result


print(group_by_debt_level(clients))