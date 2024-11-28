class Vertex():
    def __init__(self):
        self.left: Vertex = None
        self.right: Vertex = None
        self.key = None
        self.priority = None

    def insert(self, key):
        pass

    def remove(self, key):
        pass

    def find(self, key):
        pass

    def print(self):
        pass



def split(root: Vertex, key: int):
    if root is None:
        return None , None
    
    if root.key <= key:
        root_a, root_b = split(root.right, key)
        root.right = root_a
        return root, root_b
    else:
        root_a, root_b = split(root.left, key)
        root.left= root_b
        return root_a, root
    
def merge(root1: Vertex, root2: Vertex) -> Vertex:
    if root1 is None:
        return root2  
    
    if root2 is None:
        return root1  

    if root1.priority > root2.priority:
        root1.right = merge(root1.right, root2)
        return root1
    else:
        root2.left = merge(root1, root2.left)
        return root2
