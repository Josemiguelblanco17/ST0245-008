class Node:
    def __init__(self, head):
        self.head = head
        self.next = None


class SingleLinkedList:
    def __init__(self, now):
        self.now = now

    def insert(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.now
            self.now = new_node
        else:
            current = self.now
            k = 1
            while current.next is not None and k < pos:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    def lenght(self):
        current = self.now
        if current is not None:
            cont = 1
            while current is not None:
                cont += 1
                current = current.next
            return cont
        else:
            return 0

    def show(self):
        dato = self.now
        while dato is not None:
            print(dato.head, end=" ")
            dato = dato.next
        print("")

    def reverse(self, k):
        for j in range(k):
            prev = None
            current = self.now
            aux = self.now
            while current.next is not None:
                prev = current
                current = current.next
            self.now = current
            self.now.next = aux
            prev.next = None


lista = SingleLinkedList(Node(1))
for i in range(2, 6):
    lista.insert(i, i+1)

lista.show()
a = int(7)
lista.reverse(a)
lista.show()
