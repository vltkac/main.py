
# Напишіть гру Правда або Дія.
# Опис:
# 1. Спочатку, введіть імена гравців.
# 2. Кожен гравець по черзі обирає "Правда" або "Дія".
# 3. Якщо гравець обрав "Правда", йому задається
# запитання, на яке він повинен відповісти правдиво.
# 4. Якщо "Дія", гравець повинен виконати вказане
# завдання.
# 5. Після завершення кожного раунду, виведіть
# результати.
# Функції:
#  get_player_names(): Запитайте імена гравців і поверніть
# їх у вигляді списку.
#  ask_truth_or_dare(player): Функція, яка приймає ім'я
# гравця та запитує його, чи обирати "Правда" чи "Дія".
#  ask_truth_question(player): Функція, яка приймає ім'я
# гравця, виберє одне запитання випадковим чином та
# просить гравця дати відповідь.
#  perform_dare(player): Функція, яка приймає ім'я гравця
# та вибирає одне завдання випадковим чином та
# просить гравця виконаи його.
#  play_game(players): Функція, яка керує ходом гри.
# Послідовно запитайте кожного гравця, чи обирати
# "Правда" чи "Дія", а потім відповідно викликайте
# функцію ask_truth_question або perform_dare.
# Константи:
#  questions – список питань
#  dares – список завдань

import random

QUESTIONS = [
    "ты влюблялся(ась) в кого-то из друзей?",
    "какой у тебя самый странный страх?",
    "ты когда-нибудь завидовал(а) близкому другу?",
    "что ты скрываешь от родителей?",
    "кто тебе сейчас нравится?"
]

DARES = [
    "скажи комплимент каждому в комнате.",
    "сделай 10 приседаний.",
    "отправь смайлик последнему, кто тебе писал.",
    "говори шёпотом 3 минуты.",
    "сделай селфи с самым странным выражением лица."
]

def get_player_names():
    print('Чтобы остановить ввод игроков, впишите END\n')

    player_names = []

    while True:
        name_input = input('Введите имя игрока: ').strip()
        print()

        name_input_correct = name_input[0].upper() + name_input[1:].lower()

        if name_input.lower() == 'end':
            break
        else:
            player_names.append(name_input_correct)

    return player_names


list_of_names = get_player_names()


def ask_truth_or_dare():
    truth_or_dare = []

    i = 0

    while len(truth_or_dare) < len(list_of_names):
        player_choice = input(f'{list_of_names[i]}, правда или действие? ')
        print()

        if player_choice.lower() == 'правда' or player_choice.lower() == 'действие':
            truth_or_dare.append(player_choice)
            i += 1
        else:
            print('Введите "правда" или "действие"\n ')
            continue

    return truth_or_dare


truth_or_dare_list = ask_truth_or_dare()


truth_answers = []

def ask_truth_question():
    for player in list_of_names:
        if truth_or_dare_list[list_of_names.index(player)] == 'правда':
            random_question = QUESTIONS[random.randint(0, len(QUESTIONS) - 1)]

            player_answer = input(f'{player}, {random_question} ')
            print()

            truth_answer = [player, random_question, player_answer]

            truth_answers.append(truth_answer)

    return truth_answers


dares = []

def perform_dare():
    for player in list_of_names:
        if truth_or_dare_list[list_of_names.index(player)] == 'действие':
            random_dare = DARES[random.randint(0, len(DARES) - 1)]

            player_action = print(f'{player}, {random_dare}\n')

            dare = [player, random_dare]

            dares.append(dare)

    return dares


ask_truth_question()

perform_dare()

answer1_str = '---'.join(truth_answers)

print(answer1_str)

print('---'.join(dares))
