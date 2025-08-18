# Завдання 6
# Організуйте фільтр товарів в онлайн магазині. Усі товари
# діляться на певні категорії, причому один і той самий товар
# може відноситись до різних категорій. Є словник, де ключі –
# назви категорій, а значення – множини з товарами цієї
# категорії.
# Користувач вводить 2 категорії, виведіть ті товари, які
# відносяться одночасно до цих двох категорій.
# Додатково: змініть код якщо користувач вводить декілька
# категорій.

# catalog = {
#     "електроніка": {"ноутбук", "смартфон", "телевізор", "планшет"},
#     "акційні товари": {"планшет", "пилосос", "смартфон"},
#     "побутова техніка": {"холодильник", "пилосос", "мікрохвильовка", "телевізор"},
#     "офісна техніка": {"ноутбук", "принтер", "сканер"},
# }
#
#
# def get_common_items(items: dict, verbose=True):
#     print('Чтобы остановить ввод категорий, нажмите Enter\n')
#     print('Електроніка    Aкційні товари    Побутова техніка    Офісна техніка\n')
#
#     search_categories = []
#
#     result = set()
#
#     while True:
#         user_data = input('Введите категорию из доступных: ').strip().lower()
#
#         if not user_data:
#             break
#
#         if user_data not in items:
#             print('Введите категорию из списка\n')
#             continue
#
#         search_categories.append(user_data)
#
#     if len(search_categories) == 1:
#         print('Была введена только одна категория')
#         return None
#
#     for i in range(len(search_categories) - 1):
#         result = set(items[search_categories[i]]) & set(items[search_categories[i + 1]])
#
#     if verbose:
#         print(', '.join(list(result)))
#
#     return result
#
#
# get_common_items(catalog)


# Завдання 1
# Є словник з курсами валют, де ключ – назва валюти,
# значення – курс до гривні. Користувач вводить назву валюти,
# суму та назву нової валюти, в яку треба перевести суму.
# Підказка 1: для того щоб перевести, скажімо, 10 доларів у
# євро, спочатку треба перевести 10 доларів у гривні, після чого
# гривні переводити у євро.
# Підказка 2: щоб можна було переводити долари у
# гривні(або гривні у долари), потрібно щоб у словнику була
# інформація скільки гривень в 1 гривні

# currency_rates = {
#     'uah': 1.0,
#     'usd': 38.0,
#     'eur': 41.5,
#     'pln': 9.0
# }
#
# def exchange_currency(rates: dict):
#     print('Чтобы закрыть программу, при вводе валюты нажмите Enter\n')
#     print('UAH    USD    EUR    PLN\n')
#
#     while True:
#         currency = input('Введите валюту: ').strip().lower()
#
#         if not currency:
#             print('Конец программы')
#             break
#
#         if currency not in rates:
#             print('Введите валюту из доступных\n')
#             continue
#
#         sum_currency = input('Введите сумму: ').strip().replace(',', '.')
#
#         try:
#             sum_currency = float(sum_currency)
#         except ValueError:
#             print('Неверный формат записи\n')
#             continue
#
#         target_currency = input(f'Введите валюту, на которую хотите обменять {sum_currency} {currency.upper()}: ').strip().lower()
#
#         if target_currency not in rates:
#             print('Введите валюту из доступных\n')
#             continue
#
#         currency_to_uah = sum_currency * rates[currency]
#
#         uah_to_target_currency = currency_to_uah / rates[target_currency]
#
#         print(f'{sum_currency} {currency} --- {uah_to_target_currency:.2f} {target_currency}\n')
#
#
# exchange_currency(currency_rates)

# Завдання 2
# Напишіть функцію, яка отримує 2 множини з іменами
# працівників, які працюють в офісі та віддалено. Виведіть на
# екран:
#  Імена усіх працівників
#  Імена працівників, які працюють і в офісі, і віддалено
#  Відсоток працівників, які працюють і в офісі, і
# віддалено

# office_workers = {'Олена', 'Іван', 'Марія', 'Петро', 'Андрій'}
# remote_workers = {'Марія', 'Андрій', 'Світлана', 'Ірина'}
#
# def get_employees_stats(office: set, remote: set):
#     all_employees = office | remote
#
#     print(f'Все работники: {', '.join(all_employees)}')
#
#     hybrid_employees = office & remote
#
#     print(f'Гибридные работники: {', '.join(hybrid_employees)}')
#
#     print(f'Процент гибридных работников: {len(hybrid_employees) / len(all_employees) * 100:.2f} %')
#
# get_employees_stats(office_workers, remote_workers)









