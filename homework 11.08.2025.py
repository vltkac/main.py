# Завдання 1
# Напишіть функцію, яка запитує користувача пароль та
# повертає його. Якщо пароль поганий, тобто менше 8 символів
# чи містить однакові символи то викликати виняток ValueError.
# Написати код try … except який використовує дану
# функцію.

# def verify_password(verbose=True):
#     """
#     :param verbose: вывести в консоль информацию о том, что пароль действителен
#     :return: функция возвращает только действительный пароль
#     """
#     user_data = input('Введите пароль: ')
#
#     if len(user_data) < 8 or len(user_data) != len(set(user_data)):
#         raise ValueError('Пароль должен быть длиннее 8 символов и содержать разные символы')
#
#     if verbose:
#         print(f'Пароль "{user_data}" действителен')
#
#     return user_data
#
#
# try:
#     verify_password()
# except Exception as err:
#     print(f'Ошибка: {err}')


# Завдання 2
# Є словник де ключ – логін, а значення – пароль. Напишіть
# функцію, яка запитує користувача логін та пароль. Якщо
# логіна немає в словнику, або невірний пароль, то викликати
# ValueError.
# Написати код try … except який використовує дану
# функцію.

# users = {
#     "admin": "admin123",
#     "user1": "qwerty",
#     "user2": "123456",
# }
#
# def verify_user(data: dict, verbose=True):
#     """
#     :param data: словарь с зарегистрированными пользователями
#     :param verbose: вывести в консоль информацию о том, что идентификация успешна
#     :return: если идентификация успешна, функция возвращает True
#     """
#
#     user_name = input('Введите имя пользователя: ')
#
#     if user_name not in data:
#         raise ValueError('Пользователь не зарегистрирован')
#
#     user_password = input('Введите пароль: ')
#
#     if data[user_name] != user_password:
#         raise ValueError('Неверный пароль')
#
#     if verbose:
#         print('Идентификация успешна')
#
#     return True
#
#
# try:
#     verify_user(users)
# except Exception as err:
#     print(f'Ошибка: {err}')