"""
max-heap
"""

import sys

def propagate_up(idx: int, arr: list[int]) -> tuple[int, list[int]]:
    parentIdx = (idx - 1) // 2 # works even if (i - 1) = 0
    while parentIdx >= 0 and arr[parentIdx]  < arr[idx]:
        # replace parent and current element
        parent_buffer = arr[parentIdx]
        arr[parentIdx] = arr[idx]
        arr[idx] = parent_buffer

        # update idxes
        idx = parentIdx
        parentIdx = (idx - 1) // 2

    return idx, arr

def propagate_down(arr: list[int]):
    idx = 0
    leftChildIdx = idx * 2 + 1
    rightChildIdx = idx * 2 + 2

    def _get_idx_of_max(*args):
        return args.index(max(args))

    while True:
        current_values = [arr[idx]]
        current_values.append(arr[leftChildIdx] if leftChildIdx < len(arr) else -float('inf'))
        current_values.append(arr[rightChildIdx] if rightChildIdx < len(arr) else -float('inf'))

        idx_of_max = _get_idx_of_max(*current_values)

        if idx_of_max == 1:  # left is the largest one
            arr[idx], arr[leftChildIdx] = arr[leftChildIdx], arr[idx]

            idx = leftChildIdx
            leftChildIdx = idx * 2 + 1
            rightChildIdx = idx * 2 + 2

        elif idx_of_max == 2:  # right is the largest one
            arr[idx], arr[rightChildIdx] = arr[rightChildIdx], arr[idx]

            idx = rightChildIdx
            leftChildIdx = idx * 2 + 1
            rightChildIdx = idx * 2 + 2

        else:
            break

    return idx, arr

def max_heap(operation_number):
    arr = []
    for _ in range(operation_number):
        operation = list(map(int, sys.stdin.readline().strip().split()))
        
        if operation[0] == 0: # insert operation
            arr.append(operation[1])
            currentIdx = len(arr) - 1
            currentIdx, arr = propagate_up(currentIdx, arr)
            # print(arr)

        if operation[0] == 1:
            root_value = arr[0] # O(1)
            arr[0] = arr[-1]
            arr.pop() # remove the last one
            if arr:
                _, arr = propagate_down(arr)
            print(root_value)
    


def main():
    operation_number = int(input())
    max_heap(operation_number)


if __name__ == "__main__":
    main()