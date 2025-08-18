import random

words_str = 'Apple Chair Table Grass Water Bread House Beach Cloud Stone Dress Plant Train Shelf Horse Store Heart Night Floor Block Brick Clock Brain World Glass'

words_str = words_str.lower()

words = words_str.split()

random_word = words[random.randint(0, len(words) - 1)]

random_word_letters = []

for i in range(len(random_word)):
    random_word_letters.append(random_word[i])

while True:
    user_guess = input('Впишите слово: ').strip().lower()
    print()

    if user_guess == 'end':
        print(f'Правильное слово - {random_word}. Удачи в следующей игре!')
        break

    elif user_guess == random_word:
        print(f'Поздравляю! Вы угадали слово {random_word}')
        break

    elif len(user_guess) == 5 and user_guess.isalpha():

        user_guess_letters = []

        for i in range(len(user_guess)):
            user_guess_letters.append(user_guess[i])

        user_index_and_letter_correct_counter = 0

        user_letter_correct_index_incorrect_counter = 0

        for i in range(len(user_guess_letters)):
            if user_guess_letters[i] == random_word_letters[i]:
                user_index_and_letter_correct_counter += 1

        for i in range(len(user_guess_letters)):
            if user_guess_letters[i] != random_word_letters[i] and user_guess_letters[i] in random_word_letters:
                user_letter_correct_index_incorrect_counter += 1

        print(f'Буквы сходятся и стоят на правильном месте: {user_index_and_letter_correct_counter}')
        print()

        print(f'Буквы сходятся, но стоят на другом месте: {user_letter_correct_index_incorrect_counter}')
        print()

    else:
        print('Впишите английское слово из 5 букв')
        print()