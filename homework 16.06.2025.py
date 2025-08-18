# 1

# def print_quote():
#     print('“Don’t compare yourself with anyone in this world… \nif you do so, you are insulting yourself.”\n                                Bill Gates')
#
# print_quote()

# 2

# def show_nums(start, finish):
#     for num in range(start, finish + 1):
#         if num % 2 != 0:
#             print(num, end = ' ')
#
# show_nums(10, 20) # 11 13 15 17 19

# 3

# def show_nums(start, end, end_is_included):
#     if end_is_included:
#         for num in range(start, end + 1):
#             print(num, end = ' ')
#     else:
#         for num in range(start, end):
#             print(num, end = ' ')
#
# show_nums(25, 50, False) # 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49

# 4

# def show_min_num(num_1, num_2, num_3, num_4, num_5):
#     min_num = min(num_1, num_2, num_3, num_4, num_5)
#
#     # print(min_num)
#
#     return min_num
#
# # show_min_num(1000, 555, 999, 10, 1000000) # 10

# 5

# def multipy_range(start, end):
#     one_to_multiply = 1
#
#     if start < end:
#         for num in range(start, end + 1):
#             one_to_multiply *= num
#     else:
#         for num in range(end, start + 1):
#             one_to_multiply *= num
#
#     result = one_to_multiply
#
#     print(result)
#
#     return result
#
# multipy_range(5, 10) # 151200
# multipy_range(10, 5) # 151200