import sys

def merge(leftArray, rightArray, arr):
    j = i = pointer = 0
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:
            arr[pointer] = leftArray[i]
            i += 1
        else:
            arr[pointer] = rightArray[j]
            j += 1

        pointer += 1

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

        mergeSort(leftArray)
        mergeSort(rightArray)
        merge(leftArray, rightArray, arr)

    return arr

def get_lowest_idx(arr: list[int], num: int) -> int:
    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer < right_pointer:
        middle_pointer = left_pointer + (right_pointer - left_pointer) // 2
        if arr[middle_pointer] < num:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer
    return left_pointer if arr[left_pointer] >= num else len(arr)

def get_highest_idx(arr: list[int], num: int) -> int:
    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer < right_pointer:
        middle_pointer = left_pointer + (right_pointer - left_pointer + 1) // 2
        if arr[middle_pointer] > num:
            right_pointer = middle_pointer - 1
        else:
            left_pointer = middle_pointer
    return right_pointer if arr[right_pointer] <= num else -1

def main():
    _ = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    sorted_arr = mergeSort(arr)
    
    number_of_requests = int(input())
    
    for _ in range(number_of_requests):
        l, r = map(int, sys.stdin.readline().strip().split())
        
        lower_idx = get_lowest_idx(sorted_arr, l)
        highest_idx = get_highest_idx(sorted_arr, r)
        
        if lower_idx <= highest_idx:
            count = highest_idx - lower_idx + 1
        else:
            count = 0
        
        print(count)
    

if __name__ == "__main__":
    main()
