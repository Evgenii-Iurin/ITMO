import sys

def is_bst(tree, node_index, min_value, max_value):
    # (1) Выход из рекурсии
    if node_index < 0:
        return True
    
    node_value, left_idx, right_idx = tree[node_index]
        
    # (2) Выход из рекурсии
    if not (min_value < node_value < max_value):
        return False

    return (is_bst(tree, left_idx, min_value, node_value) and
            is_bst(tree, right_idx, node_value, max_value))

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        val, l, r = list(map(int, sys.stdin.readline().strip().split()))
        arr.append(list((val, l-1, r-1))) # Нулевая индексация, чтобы гулять по массиву
    root_idx = int(input()) - 1

    # print(f'tree : {arr}')
        
    if is_bst(arr, root_idx, float('-inf'), float('inf')):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
