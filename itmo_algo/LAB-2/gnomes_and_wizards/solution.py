"""Гоблины Мглистых гор очень любят ходить к своим шаманам. Так как гоблинов много, к шаманам часто образуются очень длинные очереди. А поскольку много гоблинов в одном месте быстро образуют шумную толпу, которая мешает шаманам проводить сложные медицинские манипуляции, последние решили установить некоторые правила касательно порядка в очереди.

Обычные гоблины при посещении шаманов должны вставать в конец очереди. Привилегированные же гоблины, знающие особый пароль, встают ровно в ее середину, причем при нечетной длине очереди они встают сразу за центром.

Так как гоблины также широко известны своим непочтительным отношением ко всяческим правилам и законам, шаманы попросили вас написать программу, которая бы отслеживала порядок гоблинов в очереди.

Входные данные
В первой строке входных данный записано число N (1  ≤  N  ≤  5·10^5) - количество запросов к программе. Следующие N строк содержат описание запросов в формате:

,,+ i" - гоблин с номером i (1  ≤  i  ≤  N) встает в конец очереди.
,,* i" - привилегированный гоблин с номером i встает в середину очереди.
,,-" - первый гоблин из очереди уходит к шаманам. Гарантируется, что на момент такого запроса очередь не пуста.
Выходные данные
Для каждого запроса типа ,,-" программа должна вывести номер гоблина, который должен зайти к шаманам.
"""


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

            if new_node.next is None:
                self.tail = new_node

            self.len += 1

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
