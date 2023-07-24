class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    length: int

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value if self.first else None

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        unwanted_node = self.first
        self.first = self.first.next
        self.length -= 1
        return unwanted_node.value if unwanted_node else None

    def __len__(self):
        return self.length
