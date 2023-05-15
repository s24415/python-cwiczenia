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

    def append(self, e, func=None):
        if self.head is None:
            self.head = Node(e)
            self.tail = self.head
            return

        if func is None:
            current = self.head
            while current.nextE is not None and current.nextE.data <= e:
                current = current.nextE
            next = current.nextE
            current.nextE = Node(e)
            current.nextE.nextE = next
        else:
            current = self.head
            while current.nextE is not None and func(current.nextE.data, e):
                current = current.nextE
            next = current.nextE
            current.nextE = Node(e)
            current.nextE.nextE = next

        self.size += 1

    def get(self, e):
        node = self.head
        while node.data is not e:
            node = node.nextE
        return node

    def delete(self, e):
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


test = LinkedList()
test.append("asd1")
test.append("asasdd2")
test.append("asdd3")
test.append("asd4")

print(test)