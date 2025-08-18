# 1

# import math
#
# def get_new_temp(temp_initial, temp_environment, time_in_fridge, k_cooling=0.05):
#     new_temp = temp_environment + (temp_initial - temp_environment) * math.exp(-k_cooling * time_in_fridge)
#
#     new_temp = round(new_temp, 2)
#
#     return new_temp
#
#
# print(get_new_temp(30, 5, 10))  # 20.16

# 2

# import time
#
# def input_name(show_time=False):
#     start = time.time()
#
#     name = input('Введите свое имя: ')
#
#     end = time.time()
#
#     countdown = end - start
#
#     if show_time:
#         print(f'{countdown} секунд работала функция')
#
#     return name
#
#
# print(input_name(show_time=True))
#
# print(input_name())

# 3

# import date_utils
#
# date_utils.count_days_till_deadline()