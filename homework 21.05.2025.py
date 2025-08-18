# # 1
#
# while True:
#     grade = int(input('Please submit a grade (on scale of 1-5) '))
#     if grade == 1:
#         print('Very bad')
#     elif grade == 2:
#         print('Bad')
#     elif grade == 3:
#         print('Sufficient')
#     elif grade == 4:
#         print('Well')
#     elif grade == 5:
#         print('Excellent')
#     else:
#         print('Please submit a correct number')
#
# # 2
#
print('Welcome! List all of the votes one by one. Type "stop" to count amount of votes and their ratio.')

yes_counter = 0
no_counter = 0

while True:
    user_choice = input('Yes / No ')
    if user_choice == 'Yes' or user_choice == 'yes':
        yes_counter += 1
    elif user_choice == 'No' or user_choice == 'no':
        no_counter += 1
    elif user_choice == 'Stop' or user_choice == 'stop':
        break
    else:
        print('Error')
        pass

print(f'Total amount of "yes" - {yes_counter}')
print(f'Total amount of "no" - {no_counter}')

if yes_counter > no_counter:
    print('Yes is prevalent')
elif yes_counter == no_counter:
    print('Draw')
else:
    print('No is prevalent')
