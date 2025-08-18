# 1

# def message(name='Vlad'):
#     print(f'«You are welcome, {name}»')
#
#
# message('Student')

# 2

# def do_operation(num1, num2, operation='add'):
#     if not isinstance(num1, (int, float)):
#         print('Параметр должен быть числом')
#         return
#
#     if not isinstance(num2, (int, float)):
#         print('Параметр должен быть числом')
#         return
#
#     if not isinstance(operation, str):
#         print('Параметр должен быть текстом')
#         return
#
#     operation = operation.lower().strip()
#
#     if operation == 'add':
#         result = num1 + num2
#         return result
#     elif operation == 'diff':
#         result = num1 - num2
#         return result
#     elif operation == 'mult':
#         result = num1 * num2
#         return result
#     else:
#         print('Введите параметр из списка доступных')
#         return
#
#
# print(do_operation(1, 4, 'diff'))
# print(do_operation(num1=100, num2 = 500, operation='mulT'))
# print(do_operation(operation='  mULt  ', num1=100, num2 = 300))
# print(do_operation(num2=1000000, num1=-10000))

# 3

# def correct_name(string):
#     for symbol in string:
#         first_upper_rest_lower_name = string[0].upper() + string[1:].lower()
#
#     return first_upper_rest_lower_name
#
#
# def send_invitation(holiday, names=''):
#     if not isinstance(holiday, str):
#         print('The name of the holiday must be in text form.')
#         return
#
#     if not isinstance(names, str):
#         print('Enter the names separated by commas.')
#         return
#
#     if names == '':
#         print('No guests')
#         return
#
#     names = names.replace(',', '')
#
#     names = names.strip()
#
#     names_list = names.split()
#
#     correct_names = []
#
#     for name in names_list:
#         correct_names.append(correct_name(name))
#
#     for name in correct_names:
#         print(f'{name}, you are invited to {holiday}\n')
#
#
# send_invitation(holiday='New Year Party', names='Alice, bOB, CHARLIE, diana, Edward, fRaNcEs, george, HANNAH, isaac, JULIA')
# send_invitation(holiday='New Year Party') # No guests





