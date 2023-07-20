class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.length = 1
        self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def insert(self, value, index):

        if index < 0 or index > self.length:
            raise ValueError("Invalid position")

        if index == 0:
            self.prepend(value)
            return self
        elif index == self.length:
            self.append(value)
            return self.print_list()

        new_node = Node(value)
        leader = self.traverse_to_index(index - 1)
        holding_pointer = leader.next
        leader.next = new_node
        new_node.next = holding_pointer
        self.length += 1
        return self.print_list()

    def remove(self, value, index):
        if index < 0 or index > self.length:
            raise ValueError("Invalid position")

        leader = self.traverse_to_index(index - 1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next
        self.length -= 1
        return unwanted_node

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node
        
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node, end=' ')
            current_node = current_node.next
        print()


myList = LinkedList(3)
myList.append(4)
myList.prepend(5)
myList.insert(value=6, index=4)
myList.print_list()
