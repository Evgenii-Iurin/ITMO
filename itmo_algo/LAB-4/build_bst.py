from random import randint
import sys

class Vertex:
    def __init__(self, key=None, priority=None, value=None, left=None, right=None, sz=1):
        self.key: int = key
        self.priority: int = priority
        self.value: int = value
        self.left: Vertex = left
        self.right: Vertex = right
        self.sz: int = sz  # !new!

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
    cur: str = '(' + str(v.key) + ',' + str(v.priority) + ')'
    l: int = print_tree(v=v.left, skip=skip, d=(d + 1), lines=lines)
    lines[d] += ' ' * (skip + l - len(lines[d])) + cur
    r: int = print_tree(v=v.right, skip=(skip + l + len(cur)), d=(d + 1), lines=lines)
    return l + r + len(cur)


def size_of(v: Vertex) -> int:
    return v.sz if v is not None else 0


def recalc(v: Vertex) -> Vertex:
    if v is not None:
        v.sz = size_of(v.left) + size_of(v.right) + 1
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


def split(root: Vertex, key0: int) -> (Vertex, Vertex):
    if root is None:
        return None, None
    if root.key < key0:
        (root.right, other) = split(root.right, key0)
        return recalc(root), other  # !new!
    else:
        (other, root.left) = split(root.left, key0)
        return other, recalc(root)  # !new!


def insert(root: Vertex, key0: int, value: int) -> Vertex:
    (a, b) = split(root, key0)
    (c, d) = split(b, key0 + 1)
    c = Vertex(key0, randint(1000, 9999), value)
    return merge(a, merge(c, d))


def main():
    tree: Vertex = None
    n = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split())) 
    print(n)
    for i in range(n):
        tree = insert(tree, i, arr[i])
    print(tree)
    print(1)


if __name__ == '__main__':
    main()