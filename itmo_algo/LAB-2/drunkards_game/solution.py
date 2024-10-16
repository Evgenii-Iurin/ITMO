"""
ограничение по времени на тест 2 секунды
ограничение по памяти на тест 256 мегабайт
В игре в пьяницу карточная колода раздаётся поровну двум игрокам. Далее они вскрывают по одной верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты, которые кладутся под низ его колоды. Тот, кто остаётся без карт — проигрывает.

Для простоты будем считать, что все карты различны по номиналу, а также, что самая младшая карта побеждает самую старшую карту («шестерка берет туза»).

Игрок, который забирает себе карты, сначала кладёт под низ своей колоды карту первого игрока, затем карту второго игрока (то есть карта второго игрока оказывается внизу колоды).

Напишите программу, которая моделирует игру в пьяницу и определяет, кто выигрывает. В игре участвует n карт, имеющих значения от 0 до n - 1, большая карта побеждает меньшую, карта со значением 0 побеждает карту n - 1.

Входные данные
Программа получает на вход три строки. В первой строке содержится целое чётное число n (2 ≤ n ≤ 100000). Вторая строка содержит  чисел — карты первого игрока, а третья —  карт второго игрока. Карты перечислены сверху вниз, то есть каждая строка начинается с той карты, которая будет открыта первой. Гарантируется, что каждая из карт встречается в колодах игроков ровно один раз.

Выходные данные
Программа должна определить, кто выигрывает при данной раздаче, и вывести слово «first» или «second», после чего вывести количество ходов, сделанных до выигрыша. Если на протяжении 2·10^5 ходов игра не заканчивается, программа должна вывести слово «draw».
"""

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
