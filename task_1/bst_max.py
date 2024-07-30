# Алгоритм пошуку найбільшого значення в дереві використовує властивість 
# двійкового дерева пошуку, де найбільше значення завжди знаходиться у правому піддереві.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для вставки нового вузла з даним ключем
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Функція для знаходження найбільшого значення у дереві
def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Приклад використання
if __name__ == "__main__":
    root = TreeNode(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Найбільше значення у дереві:", find_max(root))

