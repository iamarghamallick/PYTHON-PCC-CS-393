# Threaded BST for in-order traversal


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.is_threaded = False


class ThreadedBST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = new_node
                        new_node.right = current
                        new_node.is_threaded = True
                        break
                    current = current.left
                else:
                    if current.is_threaded or current.right is None:
                        new_node.right = current.right
                        current.right = new_node
                        current.is_threaded = True
                        new_node.is_threaded = True
                        break
                    current = current.right

    def inorder_traversal(self):
        result = []
        current = self.leftmost_node(self.root)
        while current:
            result.append(current.key)
            if current.is_threaded:
                current = current.right
            else:
                current = self.leftmost_node(current.right)
        return result

    def leftmost_node(self, node):
        if not node:
            return None
        current = node
        while current.left:
            current = current.left
        return current


if __name__ == "__main__":
    bst = ThreadedBST()
    keys = [5, 2, 8, 1, 3, 7, 9]
    for key in keys:
        bst.insert(key)
    print("Inorder Traversal of Threaded Binary Search Tree:")
    print(bst.inorder_traversal())
