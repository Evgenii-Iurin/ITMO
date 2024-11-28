class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def popleft(self):
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return value

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0


def move_from_dead_end_to_output(stack: list, look_for: int, result: list):
    stack.pop()
    look_for += 1
    result.append('2 1')
    return stack, look_for, result


def main():
    N = int(input())
    input_seq = Deque()

    for card in map(int, input().split()):
        input_seq.append(card)

    stack = []
    result = []
    look_for = 1

    while input_seq or stack:
        if stack and stack[-1] == look_for:
            stack, look_for, result = move_from_dead_end_to_output(stack, look_for, result)

        elif input_seq:
            cariage = input_seq.popleft()
            stack.append(cariage)
            result.append('1 1')
        else:
            return '0'

    return result


if __name__ == "__main__":
    result = main()
    for x in result:
        print(x)
