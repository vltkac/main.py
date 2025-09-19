# TASK 1
from queue import Queue
from datetime import datetime, timedelta
import time

class FastFoodQueue:
    def __init__(self):
        self.queues = [Queue(), Queue(), Queue(), Queue()]
        self.order_queue = Queue()
        self.service_duration_history = []
        self.queues_lens = [0, 0, 0, 0] # список с длинами очередей

    def add(self, client):
        queue_lengths = self.queues_lens
        min_len_queue_index = queue_lengths.index(min(queue_lengths))
        self.queues[min_len_queue_index].put(client)
        queue_lengths[min_len_queue_index] += 1

    def serve(self, idx):
        if idx in range(len(self.queues)):
            self.order_queue.put((self.queues[idx].get(), datetime.now()))
            self.queues_lens[idx] -= 1
        else:
            raise ValueError('Please insert correct queue number.\n')

    def make_order(self):
        order_and_time = self.order_queue.get()
        waiting_time = datetime.now() - order_and_time[1]
        self.service_duration_history.append(waiting_time)

    def show_statistics(self):
        if self.service_duration_history:
            print(f'Minimal service duration - {min(self.service_duration_history).total_seconds()} seconds\n'
              f'Maximum service duration - {max(self.service_duration_history).total_seconds()} seconds\n'
              f'Average service duration - {(sum(self.service_duration_history, timedelta()) / len(self.service_duration_history)).total_seconds()} seconds\n')
        else:
            print('No orders found.')


# TASK 2 + 3
from queue import PriorityQueue

ZONES = ('registration', 'security control', 'boarding')

class Passenger:
    def __init__(self, name, priority, baggage=None):
        self.name = name
        self.priority = priority
        self.baggage = baggage if baggage else []


class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add(self, passenger):
        self.passengers.put((passenger.priority, passenger))

    def serve_passenger(self):
        return self.passengers.get()


class RegistrationZone(Zone):
    def serve_passenger(self):
        _, passenger = super().serve_passenger()
        success = 'ticket' in passenger.baggage
        return passenger, success


class SecurityZone(Zone):
    DANGEROUS_ITEMS = {'knife', 'gun', 'explosive'}

    def serve_passenger(self):
        _, passenger = super().serve_passenger()
        success = not any(item in self.DANGEROUS_ITEMS for item in passenger.baggage)
        return passenger, success


class BoardingZone(Zone):
    def serve_passenger(self):
        _, passenger = super().serve_passenger()
        return passenger, True


class Airport:
    def __init__(self):
        self.zones = {
            'registration': RegistrationZone('registration'),
            'security control': SecurityZone('security control'),
            'boarding': BoardingZone('boarding')
        }
        self.passengers = []

    def add(self, passenger):
        self.zones['registration'].add(passenger)

    def serve_registration(self):
        if self.zones['registration'].passengers.qsize() > 0:
            passenger, success = self.zones['registration'].serve_passenger()
            if success:
                self.zones['security control'].add(passenger)

    def serve_security_control(self):
        if self.zones['security control'].passengers.qsize() > 0:
            passenger, success = self.zones['security control'].serve_passenger()
            if success:
                self.zones['boarding'].add(passenger)

    def serve_boarding(self):
        if self.zones['boarding'].passengers.qsize() > 0:
            passenger, _ = self.zones['boarding'].serve_passenger()
            self.passengers.append(passenger)

    def show_statistics(self):
        for name, zone in self.zones.items():
            print(f'{name.capitalize()}: {zone.passengers.qsize()}')
        print(f'Total passengers boarded: {len(self.passengers)}')