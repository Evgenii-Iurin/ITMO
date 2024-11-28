from random import randint

class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None, sz=1):
        self.key: int = key
        self.priority: int = priority
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


# !new!
def size_of(v: Vertex) -> int:
    return v.sz if v is not None else 0


# !new!
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
        return recalc(root1)  # !new!
    else:
        root2.left = merge(root1, root2.left)
        return recalc(root2)  # !new!


def split(root: Vertex, key0: int) -> tuple[Vertex, Vertex]:
    if root is None:
        return None, None
    if root.key < key0:
        (root.right, other) = split(root.right, key0)
        return recalc(root), other  # !new!
    else:
        (other, root.left) = split(root.left, key0)
        return other, recalc(root)  # !new!


def insert(root: Vertex, key0: int) -> Vertex:
    (a, b) = split(root, key0)
    (c, d) = split(b, key0 + 1)
    c = Vertex(key0, randint(1000, 9999))
    return merge(a, merge(c, d))


def remove(root: Vertex, key0: int) -> Vertex:
    (a, b) = split(root, key0)
    (c, d) = split(b, key0 + 1)
    return merge(a, d)


def find(root: Vertex, key0: int) -> tuple[bool, Vertex]:
    (a, b) = split(root, key0)
    (c, d) = split(b, key0 + 1)
    flag: bool = c if c is not None else None
    return flag, merge(a, merge(c, d))


def get_upper_bound(root: Vertex, key: int) -> tuple[int, Vertex]:
    # Smallest larger
    if root is None:
        return None
    
    cur_candidate = root.key if root.key > key else None
    if root.key <= key:
        new_candidate = get_upper_bound(root.right, key)
    else:
        new_candidate = get_upper_bound(root.left, key)
    
    if cur_candidate and new_candidate:
        return min(cur_candidate, new_candidate)
    else:
        return cur_candidate if new_candidate is None else new_candidate
    

def get_lower_bound(root: Vertex, key: int) -> tuple[int, Vertex]:
    # Largest lower
    if root is None:
        return None

    cur_candidate = root.key if root.key < key else None
    if root.key >= key:
        new_candidate = get_upper_bound(root.left, key)
    else:
        new_candidate = get_upper_bound(root.right, key)
    
    if cur_candidate and new_candidate:
        return min(cur_candidate, new_candidate)
    else:
        return cur_candidate if new_candidate is None else new_candidate
    
  

# !new!
def kth(root: Vertex, k: int) -> int:
    left_size: int = size_of(root.left)
    if k == left_size:
        return root.key
    elif k < left_size:
        return kth(root.left, k)
    else:
        return kth(root.right, k - left_size - 1)


def main():
    tree: Vertex = None
    tree = insert(tree, 1)
    tree = insert(tree, 7)
    tree = insert(tree, 3)
    tree = insert(tree, 8)
    tree = insert(tree, 2)
    tree = insert(tree, 4)
    # tree = insert(tree, 5)


    print("------TREE-------")
    print(tree)

    upper_bound = get_upper_bound(tree, 10)
    print(f"upper bound : {upper_bound}")

    # print('kth:')
    # print(kth(tree, 0))
    # print(kth(tree, 1))
    # print(kth(tree, 2))
    # print(kth(tree, 3))
    # node, tree = find(tree, 2)
    # print(f'exist : {True if node is not None else False}')

    # node, tree = find(tree, 2)
    # print(f'exist : {True if node is not None else False}')

    # node, tree = find(tree, 4)
    # if node:
    #     print(f'exist : {node.right.key if node.right is not None else None}')
    # else:
    #     print(None)

    # node, tree = find(tree, 4)
    # if node:
    #     print(f'exist : {node.left.key if node.left is not None else None}')
    # else: 
    #     print(None)
    
    # tree = remove(tree, 5)

    # node, tree = find(tree, 4)
    # if node:
    #     print(f'exist : {node.right.key if node.right is not None else None}')
    # else:
    #     print(None)

    # node, tree = find(tree, 4)
    # if node:
    #     print(f'exist : {node.left.key if node.left is not None else None}')
    # else: 
    #     print(None)
    


"""
insert 2
insert 5
insert 3
exists 2
exists 4
next 4
prev 4
delete 5
next 4
prev 4
"""


if __name__ == '__main__':
    main()