from Passenger import Passenger
from Transport import Transport

class Bus(Transport):
    def __init__(self, passengers: list, capacity: int, speed: (int, float)):
        super().__init__(speed)

        if isinstance(passengers, list) and all(type(passenger) == Passenger for passenger in passengers):
            self.passengers = passengers
        else:
            raise TypeError('Please insert <list> object in the passengers parameter. All elements in the list must belong to the <Passenger> class.')

        if len(passengers) > capacity:
            raise ValueError('Passengers list exceeds actual capacity of the bus. The bus can\'t start.')

        if isinstance(capacity, int) and capacity > 0:
            self.capacity = capacity
        else:
            raise TypeError('Please insert <int> object in the capacity parameter. It must be positive value.')

    def board_passenger(self, passenger: Passenger):
        if not type(passenger) == Passenger:
            raise TypeError('Please insert <Passenger> object in the passenger parameter.')

        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
        else:
            print('Sorry but the bus is full')

    def move(self, destination: str, distance: (int, float)):
        if not isinstance(destination.strip(), str) or set(destination) == set(' '):
            raise TypeError('Please insert <str> object in the destination parameter.')

        if not isinstance(distance, (int, float)) or distance <= 0:
            raise TypeError(
                'Please insert <int> or <float> object in the distance parameter. It must be positive value.')

        passengers_left_in_the_bus = list(filter(lambda passenger: passenger.destination != destination, self.passengers))
        passengers_leaving_qty = len(self.passengers) - len(passengers_left_in_the_bus)

        if passengers_leaving_qty == 1:
            ending = ''
        else:
            ending = ''

        print(f'\n{passengers_leaving_qty} passenger{ending} left the bus.\n')
        super().move(destination=destination, distance=distance)

        self.passengers = passengers_left_in_the_bus