import sys

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



def main():
    _ = list(map(int, sys.stdin.readline().strip().split()))
    sorted_list = list(map(int, sys.stdin.readline().strip().split()))
    numbers_to_check = list(map(int, sys.stdin.readline().strip().split()))
    
    
    for bound in numbers_to_check:
        
        lower_idx = get_lowest_idx(sorted_list, bound)

        if lower_idx == len(sorted_list):
            closest = sorted_list[lower_idx - 1]
            lower_idx -= 1
        else:
            closest = sorted_list[lower_idx]
            
        if lower_idx > 0:
            left_candidate = sorted_list[lower_idx - 1]
            if abs(left_candidate - bound) < abs(closest - bound) or \
               (abs(left_candidate - bound) == abs(closest - bound) and left_candidate < closest):
                closest = left_candidate

            
        print(closest)
  

if __name__ == "__main__":
    main()
