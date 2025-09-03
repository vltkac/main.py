from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name: str, satiety=50, energy=50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
        self.energy = 100

    def eat(self, food_amount: int):
        self.satiety += food_amount

        if self.satiety > 100:
            self.satiety = 100

    @abstractmethod
    def play(self, activity_level: int):
        pass

    def make_sound(self): # почему бы этот метод тоже не сделать абстрактным?
        pass


class Cat(Pet):
    def play(self, activity_level: int):
        if self.satiety > 60:
            print('A cat is playing')
            self.energy -= 2 * activity_level
            self.satiety -= activity_level
        else:
            print('A cat is not playing because it is starving')

    def make_sound(self):
        print('Meow')

    def catch_mouse(self):
        if self.energy > 30:
            print('A cat has caught a mouse')

            if self.satiety > 40:
                print('A cat is playing with the mouse')
            else:
                print('The mouse is doomed')
        else:
            print('A cat is observing a mouse but not catching it')


class Dog(Pet):
    def play(self, activity_level: int):
        if self.satiety > 15:
            print('A dog is playing')
            self.energy -= activity_level // 2
            self.satiety -= activity_level // 2
        else:
            print('A dog is not playing because it is starving')

    def make_sound(self):
        print('Woof')

    def fetch_ball(self):
        if self.satiety > 10:
            print('A dog is fetching a ball')
            self.energy -= 5
        else:
            print('A dog is doing nothing because it is starving')