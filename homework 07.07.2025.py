# 1

# cities = (
#     "New York", "London", "Paris", "Tokyo", "Berlin",
#     "New York", "Rome", "Madrid", "Paris", "Chicago",
#     "Los Angeles", "London", "Toronto", "Tokyo", "Barcelona",
#     "Rome", "Amsterdam", "Berlin", "Sydney", "New York",
#     "Vienna", "Seoul", "Paris", "London", "San Francisco",
#     "Toronto", "Tokyo", "Rome", "New York", "Chicago"
# )
#
#
# def get_cities():
#     new_cities = []
#
#     for city in cities:
#         if cities.count(city) > 1 and city not in new_cities:
#             new_cities.append(city)
#
#     return new_cities
#
#
# print(get_cities())

# 2

# tuple1 = (3, 7, 15, 22, 7, 8, 19, 3, 10, 24, 5, 18, 9, 15, 2, 6, 22, 1, 4, 11)
# tuple2 = (9, 14, 3, 25, 7, 18, 20, 5, 1, 8, 10, 22, 2, 13, 4, 17, 6, 9, 11, 3)
#
# def get_nums():
#     new_nums = []
#
#     for num in tuple1:
#         if num not in tuple2:
#             new_nums.append(num)
#
#     return new_nums
#
#
# print(get_nums())

# 3

# tuple_1 = (3, 7, 15, 22, 8, 19, 10, 14, 5, 18, 9, 2, 6, 1, 4, 11, 30, 25, 17, 13)
# tuple_2 = (30, 7, 99, 22, 8, 55, 10, 14, 5, 88, 9, 44, 6, 1, 4, 11, 66, 25, 77, 13)
#
# def get_equals(tuple1=(), tuple2=()):
#     if not isinstance(tuple1, tuple):
#         return 'Аргумент должен быть кортежем'
#
#     if not isinstance(tuple2, tuple):
#         return 'Аргумент должен быть кортежем'
#
#     if tuple1 == () or tuple2 == ():
#         return 'Оба кортежа не должны быть пустыми'
#
#     zipped_tuples = zip(tuple1, tuple2)
#
#     equal_elements = []
#
#     for i_tuple in zipped_tuples:
#         if i_tuple[0] == i_tuple[1]:
#             equal_elements.append(i_tuple)
#
#     return equal_elements
#
#
# print(get_equals(tuple_1, tuple_2)) # [(7, 7), (22, 22), (8, 8), (10, 10), (14, 14), (5, 5), (9, 9), (6, 6), (1, 1), (4, 4), (11, 11), (25, 25), (13, 13)]
