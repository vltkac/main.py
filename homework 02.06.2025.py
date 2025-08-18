# 1

user = input('Введите слово и индекс (от 0 до 9): ')

ind_of_digit = int(user.index(' ')) + 1 # индекс цифры в пробеле в инпуте юзера
i = int(user[ind_of_digit]) # цифра после пробела в инпуте юзера (индекс символа, который нужно заменить)
word_length = len(user[:user.index(' ')]) # длина слова

if i < word_length:
    x = (user[:i] + "*" + user[i+1:])
    print(x[:-2])
else:
    print('Индекс слишком большой')

# не знаю, как сделать, чтобы индекс был неограничен диапазоном 0-9

# 2

user = input('Введите слово: ')

print(user[0].upper() + user[1:-1] + user[-1].upper())

# 3
print('Чтобы вывести результаты впишите END')
print()

res_str = ''

while True:
    word = input('Введите слово: ')
    if word[0] == word[-1]:
        res_str += word + ', '
    elif word == 'END':
        break

print()
print(f'Слова с одинаковой первой и последней буквой: {res_str[0:-2]}')