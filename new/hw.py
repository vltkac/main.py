# Я так понял, что по условию задачи каждый узел - объект класса Car.
# Получается, что можно добавить только один автомобиль этой марки? Если я не так понял задание, дайте фидбэк, пожалуйста.

from bintrees import BinaryTree


class Car:
    def __init__(self, brand: str, model: str, year: int):
        if not isinstance(brand, str) or not isinstance(model, str) or not isinstance(year, int):
            raise TypeError('Please insert proper type object in the parameter field.')
        elif year < 1900:
            raise ValueError('Please insert correct value in the parameter field.')

        self.brand = brand.strip()
        self.model = model.strip()
        self.year = year

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} year'


class CarPark:
    def __init__(self):
        self.cars = BinaryTree()

    def __len__(self):
        return len(self.cars)

    def _brand_check(self, brand):
        if not brand in self.cars:
            print(f'No {brand} found in database.\n')
            return False
        return True

    def add(self, car: Car):
        if not isinstance(car, Car):
            raise TypeError('Please insert proper type object in the parameter field.')

        self.cars.insert(key=car.brand, value=car)

        print(f'{car} was added successfully.\n')

    def search(self, brand: str):
        if not self._brand_check(brand):
            return None

        this_car = self.cars[brand]

        print(f'{this_car} is in the database.\n')
        return this_car

    def remove(self, brand: str, verbose=True):
        self._brand_check(brand)
        self.cars.remove(brand)

        if verbose:
            print(f'Car was removed successfully.\n')

    def sell_car(self, client: str, brand: str):
        if not client.isalpha():
            raise ValueError("Please insert client's name.")

        self._brand_check(brand)

        print(f'{self.cars[brand]} was sold to {client}.\n')

        self.remove(brand, False)


car1 = Car('Toyota', 'Corolla', 2025)
car2 = Car('Porsche', 'Cayenne', 2025)
car3 = Car('Skoda', 'Octavia', 2020)

car_park = CarPark()

car_park.add(car1)
car_park.add(car2)
car_park.add(car3)

car_park.remove('Toyota')

car_park.search('Toyota')

car_park.sell_car('Oleg', 'Porsche')

print(len(car_park))