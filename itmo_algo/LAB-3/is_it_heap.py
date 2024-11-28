"""
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
Структуру данных Heap можно реализовать на основе массива.

Для этого должно выполнятся основное свойство Heap'a, которое заключается в следующем. Для каждого 1⩽i⩽n
 выполняются следующие условия:

Если 2i⩽n
, то a[i]⩽a[2i]
Если 2i+1⩽n
, то a[i]⩽a[2i+1]
Дан массив целых чисел. Определите является ли он Heap'ом.

Входные данные
Первая строка входного файла содержит целое число n
 (1⩽n⩽105
). Вторая строка содержит n
 целых чисел по модулю не превосходящих 2⋅109
.

Выходные данные
Выведите «YES», если массив является Heap'ом и «NO» в противном случае.

Примеры
Входные данныеСкопировать
5
1 0 1 2 0
Выходные данныеСкопировать
NO
Входные данныеСкопировать
5
1 3 2 5 4
Выходные данныеСкопировать
YES

"""


import sys

def check_heap_structure(size: int, arr: list[int]) -> str:
    max_idx = size - 1
    for idx in range(max_idx):
        idxLeftChild = idx * 2 + 1
        idxRightChild = idx * 2 + 2

        if idxLeftChild <= max_idx:
            if arr[idx] < arr[idxLeftChild]:
                pass
            else:
                return 'NO'

        if idxRightChild <= max_idx:
            if arr[idx] < arr[idxRightChild]:
                pass
            else:
                return 'NO'

    return 'YES'


def main():
    size = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return check_heap_structure(size, arr)


if __name__ == "__main__":
    print(main())