class Passenger:
    def __init__(self, name: str, destination: str):
        if isinstance(name.strip(), str) and set(name) != set(' '):
            self.name = name.strip()
        else:
            raise TypeError('Please insert <str> object in the name parameter')

        if isinstance(destination.strip(), str) and set(destination) != set(' '):
            self.destination = destination.strip()
        else:
            raise TypeError('Please insert <str> object in the destination parameter.')