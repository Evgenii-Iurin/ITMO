class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.center = None
        self.len = 0

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        self.len += 1

        if self.is_empty():
            self.head = self.tail = self.center = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

            # Обновляем center, смещаем его вправо, если len становится нечетным
            if self.len % 2 == 1:
                self.center = self.center.next

    def insert_after_center(self, data):
        new_node = Node(data)
        if self.center is None:
            self.append(data)
        else:
            new_node.prev = self.center
            new_node.next = self.center.next

            if self.center.next is not None:
                self.center.next.prev = new_node
            self.center.next = new_node

            self.len += 1
            
            # Обновляем center, смещаем его вправо, если len становится четным
            if self.len % 2 == 1:
                self.center = self.center.next

    def remove_first_element(self):
        if self.is_empty():
            return None

        removed_data = self.head.data
        self.len -= 1

        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
            self.center = None

        if self.len % 2 == 1 and self.center is not None:
            self.center = self.center.next

        return removed_data


def main():
    n_actions = int(input())
    queue = DoublyLinkedList()

    for _ in range(n_actions):
        request = input().split()

        if request[0] == '+':
            queue.append(int(request[1]))
        elif request[0] == '*':
            queue.insert_after_center(int(request[1]))
        elif request[0] == '-':
            print(queue.remove_first_element())


if __name__ == "__main__":
    main()
