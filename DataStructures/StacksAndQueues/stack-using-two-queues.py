from queue import Queue


class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def peek(self):
        return self.queue1.peek()

    # O(n)
    def push(self, value):
        self.queue2.enqueue(value)
        while len(self.queue1) > 0:
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self

    # O(1)
    def pop(self):
        return self.queue1.dequeue()
