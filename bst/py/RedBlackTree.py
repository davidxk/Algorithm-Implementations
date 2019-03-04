from BinarySearchTree import BinarySearchTree
from BinarySearchTree import TreeNode

BLACK, RED = "B", "R"

class RedBlackNode(TreeNode):
    def __init__(self):
        super().__init__()
        self.color = BLACK

class RedBlackTree(BinarySearchTree):
    def add(self, target):
        pass

    def remove(self, target):
        pass
