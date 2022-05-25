from queue import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue(10)
        self.queue2 = Queue(10)

    def push(self, val):
        self.queue1.get()

    def pop(self):
        pass

    def top(self):
        pass

    def empty(self):
        pass
