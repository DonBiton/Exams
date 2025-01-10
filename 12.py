class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        # Если дерево пустое, создаем новый узел
        if root is None:
            return Node(key)

        # Иначе, рекурсивно спускаемся в дерево
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        return root

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.value, end=" ")
            self.in_order_traversal(root.right)

# Пример использования

# Создаем дерево
bst = BinarySearchTree()

# Вставляем элементы
elements = [3, 10, 1, 5]
for elem in elements:
    bst.root = bst.insert(bst.root, elem)

# Выполняем симметричный обход (in-order traversal)
print("Симметричный обход дерева:")
bst.in_order_traversal(bst.root)
