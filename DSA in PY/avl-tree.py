# AVL tree
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def rebalance(self, node):
        if not node:
            return node
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        self.update_height(root)
        return self.rebalance(root)

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
        min_val = self.find_min_value(root.right)
        root.key = min_val
        root.right = self.delete(root.right, min_val)
        self.update_height(root)
        return self.rebalance(root)

    def find_min_value(self, node):
        while node.left:
            node = node.left
        return node.key

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.key, end=" ")
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.key, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.key, end=" ")


if __name__ == "__main__":
    tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        tree.root = tree.insert(tree.root, key)
    print("height of AVL tree = ", tree.root.height)
    print("In-order traversal of the AVL tree:")
    tree.in_order_traversal(tree.root)
    print()
    print("Pre-order traversal of the AVL tree:")
    tree.pre_order_traversal(tree.root)
    print()
    print("Post-order traversal of the AVL tree:")
    tree.post_order_traversal(tree.root)
    print()
    key_to_delete = 30
    tree.root = tree.delete(tree.root, key_to_delete)
    print(f"Deleted {key_to_delete}. In-order traversal after deletion:")
    tree.in_order_traversal(tree.root)
    print()
    print("Pre-order traversal of the AVL tree:")
    tree.pre_order_traversal(tree.root)
    print()
    print("Post-order traversal of the AVL tree:")
    tree.post_order_traversal(tree.root)
    print()
