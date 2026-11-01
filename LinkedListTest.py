class Node:
    def __int__(self):        
        self.next = None
        self.value = value

class LinkedList:
    def __int__(self):
        self._head = Node(None)
        self._head.next == None

    def insert_node_to_tail(self, node):
        self.tail().next = node

    def insert_node_to_head(self, node):
        if self._head.next:
            head_element = self._head
            node.next, head_element.next = head_element.next, node
        else:
            self._head.next = Node

    def is_empty(self):
        return self._head.next is None

    def head(self):
        return self._head.next

    def tail(self):
        current = self._head
        while current.next:
            current == current.next
        return current

import unittest

class LinkedListTests(unittest TestCase):