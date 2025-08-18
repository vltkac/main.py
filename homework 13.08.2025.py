### 1


# def get_stats(file_name: str):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as src_file:
#             file_content = src_file.read()
#
#         if not file_content:
#             raise ValueError('Файл пуст')
#
#         stats = {
#             'количество символов': 0,
#             'количество строк': 0,
#             'количество цифр': 0,
#             'количество гласных': 0
#         }
#
#         vowels = 'aeuio'
#
#         stats['количество строк'] = file_content.count('\n') + 1
#
#         file_content = file_content.replace('\n', '')
#
#         for char in file_content:
#             stats['количество символов'] += 1
#
#             if char.isdigit():
#                 stats['количество цифр'] += 1
#
#             elif char.lower() in vowels:
#                 stats['количество гласных'] += 1
#
#         output = ''
#
#         for k, v in stats.items():
#             output += f'{k}: {v},\n'
#
#         output = output[0:-2] # для того чтобы убрать последнюю пустую строку и запятую последнюю
#
#         with open('file_stats.txt', 'w', encoding='utf-8') as new_file:
#             new_file.write(output)
#
#     except FileNotFoundError:
#         print('файл не найден')
#
#     except ValueError:
#         print('Файл пустой')


### 2


# import string
#
# def delete_last_char_punctuation(word: str):
#     if word[-1] in string.punctuation:
#         word = word[0:-1]
#
#     return word
#
#
# def count_words(verbose=True):
#     try:
#         target_word = input('Введите слово для поиска: ').strip().lower()
#
#         if not target_word:
#             raise ValueError('Введите слово')
#
#         file_name = input('Введите имя файла: ').strip()
#
#         with open(file_name, 'r', encoding='utf-8') as src_file:
#             content = src_file.read()
#
#         content = content.replace('\n', ' ')
#
#         words = content.split()
#
#         words_no_punct = list(map(lambda word:delete_last_char_punctuation(word), words))
#
#         if verbose:
#             print(f'{words_no_punct.count(target_word)}')
#
#         return words_no_punct.count(target_word)
#
#     except Exception as err:
#         print(f'Ошибка: {err}')


### 3


# def delete_last_line(file_name: str):
#     '''
#     :param file_name:  имя исходного файла
#     Будет создан новый файл в той же папке под именем 'no_last_line.txt' - полная копия исходного файла без последней строки.
#     '''
#
#     with open(file_name, 'r', encoding='utf-8') as src_file:
#         lines = src_file.readlines()
#
#     lines.pop(-1)
#
#     no_last_line = ''.join(lines)[:-1]
#
#     with open('no_last_line.txt', 'w', encoding='utf-8') as new_file:
#         new_file.write(no_last_line)