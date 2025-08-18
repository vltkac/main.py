# 1

# user_str = input('Please type something: ')
#
# vowels_count = 0
#
# for letter in user_str:
#     if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'u' or letter == 'U' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O':
#         vowels_count += 1
#
# print(f'Number of vowels in your text: {vowels_count}')
#
# # Не знал, как-по другому сделать
#
# # -------------------------------

# 2

# user_str = input('Введите текст: ')
#
# while True:
#     word_to_replace = input('Введите слово чтобы заменить или впишите EXIT, чтобы показать результаты и прекратить работу программы: ')
#
#     if word_to_replace == 'EXIT':
#         print(f'Редактированный текст {new_text}')
#         break
#     else:
#         if word_to_replace in user_str:
#             new_text = user_str.replace(word_to_replace, word_to_replace.upper())
#             user_str = new_text
#             print(f'Редактированный текст {new_text}')

# 3

# user_str = input('Введите текст: ')
#
# dot_count = user_str.count('.')
# exclamation_count = user_str.count('!')
# question_count = user_str.count('?')
#
# sentence_count = dot_count + exclamation_count + question_count
#
# print(f'Количество предложений в тексте: {sentence_count}')