class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class QueueLinkedList:
    """Implements an efficient first-in first-out Abstract Data Type using a linked List"""

    def __init__(self, capacity):
        """Creates and empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.head = None  # expect an instance of type Node - This is the starting point of the linked list
        self.end = None
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity

    def enqueue(self, item):
        """Adds item to the queue at the end"""
        if self.num_items == self.capacity:
            return IndexError
        else:
            newItem = Node(item)
            newItem.prev = self.end
            self.end = newItem
            if self.num_items == 0:
                self.head = self.end
            self.num_items += 1
            return self.end.item

    def dequeue(self):
        """Returns the current front of the queue"""
        if self.num_items == 0:
            return IndexError
        else:
            self.head = self.head.next
            self.num_items -= 1
            return True

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        if self.size() == 0:
            return IndexError
        return self.head.item

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items
