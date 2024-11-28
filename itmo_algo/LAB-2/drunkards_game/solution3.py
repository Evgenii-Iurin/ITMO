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


def get_winner(first_gamer_card: int, second_gamer_card: int, last_card: int):
    if (first_gamer_card == 0 and second_gamer_card == last_card):
        return 'first'
    if (first_gamer_card == last_card and second_gamer_card == 0):
        return 'second'
    
    if first_gamer_card > second_gamer_card:
        return 'first'
    else:
        return 'second'

def main():
    total_cards = int(input())
    first_gamer = Deque()
    second_gamer = Deque()

    for card in map(int, input().split()):
        first_gamer.append(card)
    for card in map(int, input().split()):
        second_gamer.append(card)

    turn = 0
    last_card = total_cards - 1

    while True:
        if turn > 2 * 10**5:
            return "draw"

        turn += 1

        first_gamer_card = first_gamer.popleft()
        second_gamer_card = second_gamer.popleft()

        winner = get_winner(first_gamer_card, second_gamer_card, last_card)
        if winner == 'first':
            first_gamer.append(first_gamer_card)
            first_gamer.append(second_gamer_card)
        else:
            second_gamer.append(first_gamer_card)
            second_gamer.append(second_gamer_card)

        if not first_gamer:
            return f'second {turn}'
        if not second_gamer:
            return f'first {turn}'

if __name__ == "__main__":
    print(main())
