class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return self

    def pop(self):
        if not self.top:
            return None

        unwanted_node = self.top
        if self.length == 1:
            self.top = None
            self.length -= 1
            return unwanted_node

        self.top = self.top.next
        self.length -= 1

        return unwanted_node
