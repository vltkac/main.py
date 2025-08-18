# 2

# import math
#
# def triangle_area(side_a, side_b, angle_in_between):
#     radian = math.radians(angle_in_between)
#
#     area = 0.5 * side_a * side_b * math.sin(radian)
#
#     return area
#
#
# print(triangle_area(1, 2, 90)) # 1

# 3

# import time
#
# def count_time():
#     start = time.time()
#
#     total = 0
#
#     for num in range(1, 10000001):
#         total += num
#
#     end = time.time()
#
#     result = end - start
#
#     return result

# 4

# import datetime
#
# def get_age(user_dob):
#     user_dob_obj = datetime.date.fromisoformat(user_dob)
#
#     today_obj = datetime.date.today()
#
#     years = today_obj.year - user_dob_obj.year
#
#     return years
#
# print(get_age('2003-02-15'))
