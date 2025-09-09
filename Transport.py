class Transport:
    def __init__(self, speed: (int, float)):
        if isinstance(speed, (int, float)) and speed > 0:
            self.speed = speed
        else:
            raise TypeError('Please insert <int> or <float> object in the speed parameter. It must be positive value.')

    def move(self, destination: str, distance: (int, float)):
        if not isinstance(destination.strip(), str) or set(destination) == set(' '):
            raise TypeError('Please insert <str> object in the destination parameter.')

        if not isinstance(distance, (int, float)) or distance <= 0:
            raise TypeError('Please insert <int> or <float> object in the distance parameter. It must be positive value.')

        move_time = distance / self.speed

        if move_time <= 1:
            ending = ''
        else:
            ending = 's'

        print(f'\nWe have arrived to {destination.strip()}!\nThe route has taken {round(move_time, 1)} hour{ending}.\n')