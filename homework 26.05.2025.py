pillow = 450
blanket = 1200
lamp = 500
keychain = 60
total_price = 0

print('Main menu') # Главное меню статично. На самом верху
print('Please use digits to choose an option') # Инструкция пользования

while True:
    print('')
    user_choice = int(input('Add item          Delete item          Clear cart          Show total price of purchase          Leave the page '))

    if user_choice == 1: # Add item
        while True:
            print('')
            item_choice = int(input('Please choose an item to add: pillow       blanket       lamp       keychain '))
            print('')
            if item_choice == 1:
                amount_pillow = int(input('How many pillows do you want to purchase? '))
                total_price += pillow * amount_pillow
                add_new_item_question = int(input('Do you want to add a new item? (yes (1) / no (2)) '))
                if add_new_item_question == 1:
                    continue
                else:
                    break
            elif item_choice == 2:
                amount_blanket = int(input('How many blankets do you want to purchase? '))
                total_price += blanket * amount_blanket
                add_new_item_question = int(input('Do you want to add a new item? (yes (1) / no (2)) '))
                if add_new_item_question == 1:
                    continue
                else:
                    break
            elif item_choice == 3:
                amount_lamp = int(input('How many lamps do you want to purchase? '))
                total_price += lamp * amount_lamp
                add_new_item_question = int(input('Do you want to add a new item? (yes (1) / no (2)) '))
                if add_new_item_question == 1:
                    continue
                else:
                    break
            elif item_choice == 4:
                amount_keychain = int(input('How many keychains do you want to purchase? '))
                total_price += keychain * amount_keychain
                add_new_item_question = int(input('Do you want to add a new item? (yes (1) / no (2)) '))
                if add_new_item_question == 1:
                    continue
                else:
                    break
            else:
                print('Wrong choice. Please use digits from 1 to 4.')
                continue

    if user_choice == 2: # Delete item
        while True:
            print('')
            item_choice = int(input('Please choose an item to add: pillow       blanket       lamp       keychain '))
            print('')
            if item_choice == 1:
                amount_pillow = int(input('How many pillows do you want to delete? '))
                total_price -= pillow * amount_pillow
                delete_item_question = int(input('Do you want to delete another item? (yes (1) / no (2)) '))
                if delete_item_question == 1:
                    continue
                else:
                    break
            elif item_choice == 2:
                amount_blanket = int(input('How many blankets do you want to delete? '))
                total_price -= blanket * amount_blanket
                delete_item_question = int(input('Do you want to delete another item? (yes (1) / no (2)) '))
                if delete_item_question == 1:
                    continue
                else:
                    break
            elif item_choice == 3:
                amount_lamp = int(input('How many lamps do you want to delete? '))
                total_price -= lamp * amount_lamp
                delete_item_question = int(input('Do you want to delete another item? (yes (1) / no (2)) '))
                if delete_item_question == 1:
                    continue
                else:
                    break
            elif item_choice == 4:
                amount_keychain = int(input('How many keychains do you want to delete? '))
                total_price -= keychain * amount_keychain
                delete_item_question = int(input('Do you want to delete another item? (yes (1) / no (2)) '))
                if delete_item_question == 1:
                    continue
                else:
                    break
            else:
                print('Wrong choice. Please use digits from 1 to 4.')
                continue

    if user_choice == 3: # Clear cart
        total_price = 0
        print('')
        print('Your card is empty')
        print('')

        main_menu_request = int(input('Do you want to go to main menu? yes (1) / no (2) '))

        if main_menu_request == 1:
            continue
        else:
            break

    if user_choice == 4:  # Show total price of purchase
        print('')
        print(f'Total cost of your purchase would be {total_price} UAH')
        print('')

        main_menu_request = int(input('Do you want to go to main menu? yes (1) / no (2) '))

        if main_menu_request == 1:
            continue
        else:
            break

    if user_choice == 5: # Leave the page
        break