"""
А в этой задаче вам нужно реализовать сортировку подсчетом. Использовать другие сортировки запрещается.

Дан массив из n элементов, которые принимают целые значения от 0 до 100. Отсортируйте этот массив в порядке неубывания элементов.

Входные данные
В первой строке содержится число n (1 ≤ n ≤ 200 000) — количество элементов в массиве. Во второй строке находятся n целых чисел, от 0 до 100 каждое.

Выходные данные
Выведите отсортированный массив.

Пример
Входные данные
5
7 3 4 2 5
Выходные данные
2 3 4 5 7 
"""

import sys

def count_sort(min_max_range: int, arr_size: int, arr: list[int]):
    buffer = [0] * min_max_range
    for i in range(arr_size):
        buffer[arr[i]] += 1

    pointer = 0
    for b in range(min_max_range): # iterate through the buffer
        if buffer[b] != 0:
            for _ in range(buffer[b]): # replace buffer[b] times value in the array with value b
                arr[pointer] = b
                pointer += 1

    return arr

def main():
    # assumption: we already know the data range: from 0 to 100
    lower_bound = 0
    higher_bound = 100
    size = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return count_sort(higher_bound - lower_bound + 1, size, arr)


if __name__ == "__main__":
    sorted_list = main()
    print(' '.join(map(str, sorted_list)))
    