# Сделай игру "Угадай число", в которой:
#
# Компьютер загадывает случайное число от 1 до 100.
#
# Игрок вводит свою догадку.
#
# После каждой догадки программа говорит, больше ли загаданное число, меньше или угадано.
#
# Игра продолжается, пока игрок не угадает число.
#
# В конце выведи, сколько попыток понадобилось.

import random

random_number = random.randint(1, 100)

user_guesses = []

guesses_counter = 1

while True:
    user_guess = input('Введите число от 0 до 100: ')
    print()

    if not user_guess.isdigit():
        print('Введите целое число от 0 до 100!\n')
    else:
        user_guess = int(user_guess)
        if user_guess == random_number:
            print(f'Поздравляю, вы угадали число {random_number}!\nВы угадывали {guesses_counter} раз!')
            break
        else:
            if user_guess not in user_guesses:
                user_guesses.append(user_guess)
                guesses_counter += 1
                if user_guess > random_number:
                    print(f'{user_guess} больше загаданного числа\n')
                else:
                    print(f'{user_guess} меньше загаданного числа\n')
            else:
                print(f'Вы уже писали это число!\n')
