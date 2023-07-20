class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.length = 1
        self.tail = self.head

    def append(self, value):

        # new_node = Node(value)
        new_node = dict(value=value, next=None)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = dict(value=value, next=self.head)
        self.head = new_node
        self.length += 1

    def __str__(self):
        return str(self.head)


myList = LinkedList(3)
myList.append(4)
print(myList)
