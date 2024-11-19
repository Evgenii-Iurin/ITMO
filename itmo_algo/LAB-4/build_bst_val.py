class TreeNode:
    """Класс узла бинарного дерева"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Класс бинарного дерева поиска"""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставка элемента в дерево"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """Вспомогательная функция для вставки"""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def inorder(self):
        """Обход дерева в порядке возрастания (in-order traversal)"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """Рекурсивный обход in-order"""
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

# Функция для построения BST из массива
def build_bst_from_array(n, array):
    bst = BST()
    for value in array:
        bst.insert(value)
    return bst
    return bst

# Пример использования
if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    bst = build_bst_from_array(n, array)
    
    # Вывод дерева в порядке возрастания
    print("Элементы в дереве (in-order):", bst.inorder())
