from queue import Queue


class Stack:
    def __init__(self):
        self.queue = Queue()

    def peek(self):
        return self.queue.last.value if self.queue.last else None

    # O(1)
    def push(self, value):
        self.queue.enqueue(value)

    # O(n)
    def pop(self):
        if len(self.queue) == 0:
            return None
        temp = Queue()
        while len(self.queue) > 1:
            temp.enqueue(self.queue.dequeue())
        popped_element = self.queue.dequeue()
        self.queue = temp
        return popped_element
