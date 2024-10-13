from collections import deque

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
    first_gamer  = deque(map(int, input().split()))
    second_gamer = deque(map(int, input().split()))

    turn = 0
    last_card = total_cards - 1
    
    while True:
        if turn > 2*10e5:
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
