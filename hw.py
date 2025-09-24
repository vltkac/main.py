import json, random

game_stats = {
    'Victories': 0,
    'Losses': 0
    }

def play():
    random_number = random.randint(1, 100)
    guess_counter = 1

    guess_nums = []

    while guess_counter != 6:
        user_guess = input('Try to guess a number: ').strip()

        try:
            user_guess = int(user_guess)

            if user_guess not in range(1, 101):
                raise ValueError

            if user_guess in guess_nums:
                raise TypeError()

        except ValueError:
            print('Please type a number from 1 to 100.\n')
            continue
        except TypeError:
            print('Try another number. You have already checked this one.\n')

        if user_guess == random_number:
            print(f'Congrats! You guessed {random_number} from the {guess_counter} time!\n')
            game_stats['Victories'] += 1
            return
        else:
            if not guess_nums:
                print('Nice try!\n')
            else:
                if abs(random_number - guess_nums[-1]) > abs(random_number - user_guess):
                    print('Closer than the last time!\n')
                elif abs(random_number - guess_nums[-1]) == abs(random_number - user_guess):
                    print('You are on the same distance away from the target number as the last guess!\n')
                else:
                    print('More far than the last time!\n')

            guess_nums.append(user_guess)
            guess_counter += 1

    print(f'Almost! Have a good luck next time! Target number was {random_number}.\n')
    game_stats['Losses'] += 1


def show_stats():
    print('\t --- Your game statistics --- \t')

    for k, v in game_stats.items():
        print(f'{k}\t{v}',end='\t\t\t\t\t')

    print()
    print()


def save_stats_to_json():
    with open('game_stats.json', 'w', encoding='utf-8') as file:
        json.dump(game_stats, file)


def parse_stats_to_dict():
    file_name = input('Please enter a file name in the current directory: ')
    print()

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            stats_data = json.load(file)
            game_stats['Victories'] = stats_data['Victories']
            game_stats['Losses'] = stats_data['Losses']

            print('Your last stats was uploaded successfully! Enjoy your game!\n')

    except FileNotFoundError:
        print('No such file found in the current directory.\n')


def main():
    while True:
        user_choice = input('To play click (1)\tTo show general stats click (2)\tTo save stats click (3)\tTo upload stats click (4)\tTo exit click (5) ').strip()
        print()

        if user_choice == '1':
            play()
        elif user_choice == '2':
            show_stats()
        elif user_choice == '3':
            save_stats_to_json()
        elif user_choice == '4':
            parse_stats_to_dict()
        elif user_choice == '5':
            break
        else:
            print('Unknown command. Please try again.\n')


if __name__ == '__main__':
    main()