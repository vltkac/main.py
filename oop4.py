import datetime
import time

class Message:
    def __init__(self, user: str, text: str):
        self.user = user
        self.text = text
        self.time = datetime.datetime.now()

    def __str__(self):
        return f'Time: {self.time.strftime('%H:%M:%S')}, user: {self.user}, message: "{self.text}"'

    def __len__(self):
        return len(self.text)

    def __gt__(self, other):
        if isinstance(other, Message):
            return self.time > other.time
        else:
            raise TypeError(f'Нельзя сравнить > типа Message с типом {type(other)}')


mess1 = Message('Vlad', "Hello")
print(mess1)
print(len(mess1))

time.sleep(2)

mess2 = Message('Liza', 'Poka')
print(mess2)

print(mess1 > mess2)

time.sleep(2)

mess3 = Message('Olena', 'Wassup')

messes = [mess3, mess1, mess2]

earliest_mess = min(messes)

print(earliest_mess)

sorted_messes = sorted(messes)

for mess in sorted_messes:
    print(mess)