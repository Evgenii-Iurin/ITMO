from random import randint
import sys


class Vertex:
    def __init__(self, key=None, priority=None, value=None, left=None, right=None, size=1):
        self.key: int = key
        self.priority: int = priority
        self.value: int = value
        self.left: Vertex = left
        self.right: Vertex = right
        self.size: int = size

    def __str__(self):
        lines: dict = {}
        ans: list = []
        print_tree(v=self, skip=0, d=0, lines=lines)
        for i in range(len(lines)):
            if i in lines:
                ans.append(lines[i])
        return '\n'.join(ans)


def print_tree(v: Vertex, skip: int, d: int, lines: dict) -> int:
    if d not in lines:
        lines[d] = ''
    if v is None:
        cur: str = '(,)'
        lines[d] += ' ' * (skip - len(lines[d])) + cur
        return len(cur)
    cur: str = '(' + str(v.value) + ',' + str(v.priority) + ')'
    l: int = print_tree(v=v.left, skip=skip, d=(d + 1), lines=lines)
    lines[d] += ' ' * (skip + l - len(lines[d])) + cur
    r: int = print_tree(v=v.right, skip=(skip + l + len(cur)), d=(d + 1), lines=lines)
    return l + r + len(cur)


def size_of(v: Vertex) -> int:
    return v.size if v is not None else 0


def recalc(v: Vertex) -> Vertex:
    if v is not None:
        v.size = size_of(v.left) + size_of(v.right) + 1
    return v


def merge(root1: Vertex, root2: Vertex) -> Vertex:
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    if root1.priority < root2.priority:
        root1.right = merge(root1.right, root2)
        return recalc(root1)
    else:
        root2.left = merge(root1, root2.left)
        return recalc(root2)


def split(root: Vertex, value: int) -> (Vertex, Vertex):
    if root is None:
        return None, None
    if root.value < value:
        (root.right, other) = split(root.right, value)
        return recalc(root), other
    else:
        (other, root.left) = split(root.left, value)
        return other, recalc(root)


def insert(root: Vertex, key: int, value: int) -> Vertex:
    (a, b) = split(root, value)
    c = Vertex(key=key, priority=randint(1000, 9999), value=value)
    return merge(a, merge(c, b))


def fill_array(v: Vertex, res_arr: list):
    if v is None:
        return

    left_key = v.left.key + 1 if v.left is not None else -1
    right_key = v.right.key + 1 if v.right is not None else -1

    res_arr[v.key] = (v.value, left_key, right_key)

    fill_array(v.left, res_arr)
    fill_array(v.right, res_arr)


def main():
    tree: Vertex = None
    n = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(n):
        tree = insert(tree, i, arr[i])

    # Print the tree structure
    # print(tree)

    # Output for validation
    print(n)
    res_arr = [None] * n
    fill_array(tree, res_arr)

    for v in res_arr:
        print(f'{v[0]} {v[1]} {v[2]}')

    print(tree.key + 1)


if __name__ == '__main__':
    main()
