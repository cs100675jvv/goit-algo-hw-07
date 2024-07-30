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

# Рекурсивна функція для знаходження суми всіх значень у дереві
def sum_of_values(root):
    if root is None:
        return 0
    # Сума поточного вузла та сум його лівого і правого піддерев
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)

# Приклад використання
if __name__ == "__main__":
    root = TreeNode(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Сума всіх значень у дереві:", sum_of_values(root))
