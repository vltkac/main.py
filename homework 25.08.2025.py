# 1

# class Cart:
#     def __init__(self, client: str, items=None):
#         self.client = client
#
#         items = list(map(lambda item: item.lower().strip(), items)) # ignore case and redundant spaces
#         self.items = items
#
#     def __str__(self):
#         return f"Client's name: {self.client}, cart: {', '.join(self.items)}"
#
#     def add_item(self, new_item: str):
#         self.items.append(new_item.lower())
#         return None
#
#     def remove_item(self, item_to_remove: str):
#         if item_to_remove.lower() in self.items:
#             self.items.remove(item_to_remove)
#             return None
#
#         print('No such item in your cart')
#         return None
#
#
# new_cart = Cart('Vlad', ['  Bread', 'Milk', 'Eggs'])
# print(new_cart) # show info
#
# new_cart.add_item('Water') # 'water' was added
# print(new_cart)
#
# new_cart.remove_item('milk') # 'milk' was removed
# print(new_cart)


# 2

# def is_valid(num: str):
#     import re
#
#     delete_spaces_num = num.replace(' ', '')
#
#     template = r'\+\d{8,15}'
#
#     if re.fullmatch(template, delete_spaces_num):
#         return delete_spaces_num
#
#     print('Wrong format: number must start with "+" and contain 8 to 15 digits (including country code)')
#     return None
#
#
# class Phone:
#     def __init__(self, number: str):
#         try:
#             if is_valid(number):
#                 self.number = number
#             else:
#                 raise ValueError
#
#             self.battery_level = 100
#
#         except ValueError:
#             print('Number was not saved. Please try again')
#
#     def __str__(self):
#         return f'Number: {self.number}, battery level: {self.battery_level}'
#
#     def reduce_energy(self, battery_value: int):
#         if battery_value > self.battery_level:
#             print('Your phone is not charged enough')
#             return None
#
#         self.battery_level -= battery_value
#
#         print(f'Your current battery level: {self.battery_level}%')
#
#         if self.battery_level < 20:
#             print('Your battery is lower than 20%. Put your phone on the charger')
#
#         return None