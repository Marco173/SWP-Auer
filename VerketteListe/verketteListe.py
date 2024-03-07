from collections.abc import Iterator
import  random

class LinkedList(Iterator):
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value)

    def insert_at(self, position, value):
        raise NotImplemented

    def pop(self):
        if self.head.next is None:
            raise Exception

        p_node = None
        node = self.head
        while node.next is not None:
            p_node = node
            node = node.next
        p_node.next = None
        return node.value

    def remove_at(self, position):
        index = 0
        prev_node = None
        node = self.head
        while index != position:
            if node.next is None:
                raise Exception

            index += 1
            node = node.next
        prev_node.next = node.next

    def __next__(self):
        if self.head is None:
            raise StopIteration
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def __len__(self):
        length = 1
        node = self.head
        while node.next is not None:
            node = node.next
            length += 1
        return length

    def __str__(self):
        node = self.head
        string = f"{node.value}"
        while node.next is not None:
            node = node.next
            string += f" -> {node.value}"
        return string


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def main():
    #Erstellen der Liste
    liste = LinkedList()
    #Hinzufügen von Zahlen in die Liste
    for i in (random.randint(0, 100) for _ in range(10)):
        liste.append(i)

    print(liste)
    print(f"length: {len(liste)}")

    print("List:")
    for element in liste:
        print(element)


if __name__ == "__main__":
    main()