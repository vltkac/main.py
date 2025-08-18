import string


def get_users(file_name: str):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            chat_content = file.read()

            users = set()

            for line in chat_content.splitlines():
                if ':' in line:
                    user = []

                    for char in line:
                        if char == ':':
                            break

                        user.append(char)

                    users.add(''.join(user))


            with open('users.txt', 'w', encoding='utf-8') as file:
                for user in users:
                    file.write(user + '\n')



    except Exception as err:
        print(f'Ошибка: {err}')


get_users('chat.txt')


def extract_users(file_user_names: str):
    try:
        with open(file_user_names, 'r', encoding='utf-8') as file:
            users_str = file.read()

            users = []

            for user in users_str.splitlines():
                users.append(user.strip())

            users = tuple(users)

            return users

    except Exception as err:
        print(f'Ошибка: {err}')
        return None


def check_mess_content(mess: str):
    from string import punctuation

    links = ('http', 'https', 'bit.ly', 't.me')

    mess = mess.strip()

    if not mess:
        return None

    if '  ' in mess:
        return None

    for link in links:
        if link in mess:
            return None

    if len(mess) < 3:
        return None

    for i in range(len(mess) - 1):
        if mess[i] in tuple(string.punctuation) and mess[i + 1] in tuple(string.punctuation):
            return None

    verified_mess = mess

    return verified_mess


def clear_chat(file_name: str):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            chat_content = file.read()

            users = []

            for user in extract_users('users.txt'):
                users.append(user)

            users = tuple(users)

            print(users)

            valid_lines = []

            for line in chat_content.splitlines():
                if line.startswith(users):  # Проверка, что строка от одного из пользователей
                    # Отделяем сообщение от имени
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        _, message = parts
                        checked = check_mess_content(message)
                        if checked:
                            valid_lines.append(line)

        with open('clean_chat.txt', 'w', encoding='utf-8') as file:
            for line in valid_lines:

                file.write(line + '\n')

    except Exception as err:
        print(f'Ошибка: {err}')
        return None

    return None

clear_chat('chat.txt')
