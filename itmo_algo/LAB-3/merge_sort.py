"""
Merge sort implementation
"""

import sys

def merge(leftArray, rightArray, arr):
    j = i = pointer = 0
    # Until we iterate through at least one list
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:
            arr[pointer] = leftArray[i]
            i += 1
        else:
            arr[pointer] = rightArray[j]
            j += 1

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

    
def mergeSort(arr: list):
    if len(arr) > 1:
        middle = len(arr) // 2

        leftArray = arr[:middle]
        rightArray = arr[middle:]

        # Continue deviding
        mergeSort(leftArray)
        mergeSort(rightArray)

        # when all arrays are devided, we can start merging
        # arr here is list before deviding, 
        #   e.g. arr = [2, 7, 4] ; leftArray = [2] rightArray = [4, 7] (note: rightArray is already sorted)
        merge(leftArray, rightArray, arr)

    return arr

def main():
    _ = input()
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return mergeSort(arr)


if __name__ == "__main__":
    sorted_list = main()
    print(' '.join(map(str, sorted_list)))
    