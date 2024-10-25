import sys

def merge_sort(arr: list[int]):
    return None

def get_lowest_idx(arr: list[int], num):
    return None

def get_highest_idx(arr: list[int], num):
    return None

def main():
    _ = input()
    arr = list(map(int, sys.stdin.readline().strip().split()))
    sorted_arr = merge_sort(arr)
    number_of_requests = int(input())
    
    for _ in number_of_requests:
        request = list(map(int, sys.stdin.readline().strip().split()))
        from_num, to_num = request[0], request[1]

        lower_idx = get_lowest_idx(sorted_arr, from_num)
        highest_idx = get_highest_idx(sorted_arr, to_num)
        
        print(lower_idx - highest_idx)


if __name__ == "__main__":
    main()