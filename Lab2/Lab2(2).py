class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def _get_height(self, root):
        return root.height if root else 0

    def _rotate_right(self, y):
        x = y.left
        T = x.right

        = y
        y.left = T

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _rotate_left(self, x):
        y = x.right
        T = y.left

        y.left = x
        x.right = T

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_balance(self, root):
        return self._get_height(root.left) - self._get_height(root.right) if root else 0

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        # Балансування
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def pre_order(self, root):
        if root:
            print(root.key, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)


# Використання AVL дерева
tree = AVLTree()
root = None

elements = [10, 20, 30, 40, 50, 25]
for el in elements:
    root = tree.insert(root, el)

print("Прямий обхід AVL дерева:")
tree.pre_order(root)
