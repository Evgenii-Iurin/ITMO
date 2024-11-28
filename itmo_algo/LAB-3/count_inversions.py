"""
C. Количество инверсий
ограничение по времени на тест5 секунд
ограничение по памяти на тест256 мегабайт
Напишите программу, которая для заданного массива A=⟨a1,a2,…,an⟩
 находит количество пар (i,j)
 таких, что i<j
 и ai>aj
.

Входные данные
Первая строка входного файла содержит натуральное число n
 (1≤n≤500000
) — количество элементов массива. Вторая строка содержит n
 попарно различных элементов массива A
 (0≤ai≤106
).

Выходные данные
В выходной файл выведите одно число — ответ на задачу.

Примеры
Входные данныеСкопировать
4
1 2 4 5
Выходные данныеСкопировать
0
Входные данныеСкопировать
4
5 4 2 1
Выходные данныеСкопировать
6

"""
import sys

def merge(leftArray, rightArray, arr):
    j = i = pointer = inversions = 0
    # Until we iterate through at least one list
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:
            arr[pointer] = leftArray[i]
            i += 1
        else:
            arr[pointer] = rightArray[j]
            j += 1
            inversions += len(leftArray) - i # [4, (6), 90] --> 3 - 1 = 2 inversion, cause 90 also higher

        pointer += 1
    
    # in the case where we have [2, 4] and [1, 6], i = 2, j = 1 we still have [1, (6)] to be used.
    #   so, we need to fill arr with remaining elements

    while i < len(leftArray):
        arr[pointer] = leftArray[i]
        i += 1
        pointer += 1

    while j < len(rightArray):
        arr[pointer] = rightArray[j]
        j += 1
        pointer += 1

    return inversions

    
def mergeSort(arr: list):
    if len(arr) > 1:
        middle = len(arr) // 2

        leftArray = arr[:middle]
        rightArray = arr[middle:]

        # Continue deviding
        inversions = mergeSort(leftArray)
        inversions += mergeSort(rightArray)

        # when all arrays are devided, we can start merging
        # arr here is list before deviding, 
        #   e.g. arr = [2, 7, 4] ; leftArray = [2] rightArray = [4, 7] (note: rightArray is already sorted)
        inversions += merge(leftArray, rightArray, arr)

        return inversions

    return 0

def main():
    _ = input()
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return mergeSort(arr)


if __name__ == "__main__":
    inversions = main()
    print(inversions)