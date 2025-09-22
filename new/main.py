# Створіть програму роботи зі словником. Наприклад,
# англо-іспанський, французько-німецький або інша мовна пара.
# Програма має:
#  надавати початкове введення даних для словника
#  відображати слово та його переклади
#  дозволяти додавати, змінювати, видаляти переклади
# слова

import bintrees


class Translation:
    def __init__(self, word: str, usage_example=None):
        self.word = word
        if usage_example:
            self.usage_example = usage_example
        else:
            self.usage_example = ''

    def __str__(self):
        return f'Translation: {self.word}, usage example: {self.usage_example}'

class WordsCouples:
    def __init__(self, word: str):
        self.word = word
        self.translations = {}
        #self.usage_example =

    def add_translation(self, trans_word: str, usage_example=None):
        this_translation = Translation(trans_word, usage_example)

        self.translations[trans_word] = this_translation

    def delete_translation(self, trans_word: str):
        self.translations.pop(trans_word)

    def __str__(self):
        all_translations = ', '.join(self.translations)
        #all_usage_examples = ', '.join(self.translations.values())
        all_usage_examples = ''

        for t in self.translations.values():
            all_usage_examples += str(t) + ', \n'


        return f'Word: {self.word}, translations: {all_translations}, usage examples: {all_usage_examples}'

class Dictionary:
    def __init__(self):
        self.words = bintrees.AVLTree()

    def add_word(self, word: str):
        this_word = WordsCouples(word)
        self.words.insert(key=word, value=this_word)

    def delete_word(self, word: str):
        if word in self.words:
            self.words.remove(key=word)

    def add_translation(self, key_word: str, translation: str, usage_examples=None):
        if key_word in self.words:
            self.words[key_word].add_translation(translation)
            return

        print(f'No {key_word} in the dictionary found.')

    def delete_translation(self, key_word: str, translation: str):
        if key_word in self.words:
            self.words[key_word].delete_translation(translation)
            return

        print(f'No {key_word} in the dictionary found.')

    def display_word(self, key_word: str):
        if key_word in self.words:
            print(self.words[key_word])
            return

        print(f'No {key_word} in the dictionary found.')


dict1 = Dictionary()

dict1.add_word('Apple')
dict1.add_translation('Apple', 'Яблоко', 'Яблоко упало.')
dict1.add_translation('Apple', 'Яблочко')

dict1.add_word('Word')
dict1.add_translation('Word', 'Слово')

dict1.delete_word('Word')

dict1.display_word('Apple')
dict1.display_word('Word')

dict1.delete_translation('Apple', 'Яблочко')
dict1.display_word('Apple')







