# import random
#
# field = []
#
# for i in range(0, 25):
#     field.append(str(i))
#
# field_str = '   '.join(field)
#
# print(field_str)
#
# treasure_cell_index = random.randint(0,len(field) - 1)
#
# tries_counter = 0
#
# checked_indexes = []
#
# while tries_counter < 7:
#
#     user_guess = input('Где находится сокровище? ')
#
#     if user_guess == field[treasure_cell_index]:
#         print('Вы угадали! Поздравляю!')
#
#         tries_counter += 1
#
#         break
#
#     if abs(int(user_guess) - treasure_cell_index) == 1:
#             print('Горячо!\n')
#
#             tries_counter += 1
#
#             checked_indexes.append(user_guess)
#
#             continue
#
#     if len(checked_indexes) > 0:
#         if abs(int(user_guess) - treasure_cell_index) < abs(int(checked_indexes[-1]) - treasure_cell_index):
#             print('Теплее!\n')
#
#             tries_counter += 1
#
#             checked_indexes.append(user_guess)
#
#             continue
#
#     if user_guess != field[treasure_cell_index]:
#         print('Холодно\n')
#
#         tries_counter += 1
#
#         checked_indexes.append(user_guess)
#
# if tries_counter == 7:
#     print(f'Вы проиграли 💀. Сокровище было в {treasure_cell_index}')