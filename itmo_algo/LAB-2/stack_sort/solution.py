"""
Даны два стека A и B. Изначально стек A содержит целые числа от 1 до n
 в некотором порядке, а стек B пуст. Вы можете выполнять два типа операций:

push: взять верхний элемент из стека A и поместить его в стек B,
pop: взять верхний элемент из стека B и вывести его в выходной поток.
Ваша задача - вывести все элементы стека A в отсортированном порядке.

Входные данные
Первая строка содержит целое число n
 (1≤n≤2000
). Вторая строка содержит n
 целых чисел - элементы в стеке A, при этом левый элемент является верхним в стеке.

Выходные данные
Выведите последовательность операций, которая выводит все элементы в отсортированном порядке. Если решения не существует, выведите impossible.
"""


class CircledDeque:
    def __init__(self, initial_capacity=4):
        self.items = [None] * initial_capacity
        self.capacity = initial_capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def append(self, item):
        if self.size == self.capacity:
            self._resize()
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def popleft(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def _resize(self):
        new_capacity = self.capacity * 2
        new_items = [None] * new_capacity

        for i in range(self.size):
            new_items[i] = self.items[(self.head + i) % self.capacity]

        self.items = new_items
        self.capacity = new_capacity
        self.head = 0
        self.tail = self.size

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0


def pop_from_stack_B(stack: list, look_for: int, result: list):
    stack.pop()
    look_for += 1
    result.append('pop')
    return stack, look_for, result


def main():
    N = int(input())  
    stack_A = CircledDeque()
    for item in map(int, input().split()):
        stack_A.append(item)
        
    stack_B = []
    look_for = 1
    result = []

    while stack_A or stack_B:
        if stack_B and stack_B[-1] == look_for:
            stack_B, look_for, result = pop_from_stack_B(stack_B, look_for, result)
        elif stack_A:
            new_el = stack_A.popleft()
            stack_B.append(new_el)
            result.append('push')
        else:
            return ['impossible']
    return result


if __name__ == "__main__":
    res = main()
    for i in res:
        print(i)
