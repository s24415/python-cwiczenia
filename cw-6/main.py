class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.nextE
        nodes.append("None")
        return " -> ".join(nodes)

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.nextE = node
            self.tail = node
        self.size += 1

    def get(self, e):
        node = self.head
        while node.data is not e:
            node = node.nextE
        return node

    def __delete__(self, e):
        if e is self.head.data:
            self.head = self.head.nextE
            return

        node = self.head
        while node.nextE.data is not e:
            node = node.nextE
        node.nextE = node.nextE.nextE


class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextE = None

    def __repr__(self):
        return self.data

