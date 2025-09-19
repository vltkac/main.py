import main

class Shop:
    def __init__(self):
        self.queue1 = main.DoubleLinkedList()
        self.queue2 = main.DoubleLinkedList()
        self.queue3 = main.DoubleLinkedList()

        self.queues = [self.queue1, self.queue2, self.queue3]

    def add_buyer(self, name, idx):
        self.queues[idx - 1].push_end(name)

    def serve_buyer(self, idx):
        served_buyer = self.queues[idx - 1].pop_start()

        print(f'{served_buyer} from the queue {idx} was served.\n')

        if not self.queues[idx - 1].head and not self.queues[idx - 1].tail:
            self._reorder(idx)

            print(f'The queue {idx} was empty. Reordering was completed.\n')

    def _reorder(self, idx):
        for q in self.queues:
            if self.queues.index(q) == idx - 1:
                continue

            switched_buyer = q.pop_end()
            self.queues[idx - 1].push_end(switched_buyer)

    def display_info(self):
        for i in range(len(self.queues)):
            queue_str = str(self.queues[i])[:-8]

            print(f'Queue {i + 1}: {queue_str}')

        print()