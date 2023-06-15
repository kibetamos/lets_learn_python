from operator import truediv


class BinaryTreeSearch:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, root, newvalue):
        # if binary search tree is empty, create a new node and declare it as root
        if root is None:
            root = BinaryTreeSearch(newvalue)
            return root

        if newvalue < root.data:
            root.leftChild = self.insert(root.leftChild, newvalue)
        else:
            root.rightChild = self.insert(root.rightChild, newvalue)
        return root

    # we can now search the above tree
    def search(self, root, value):
        if root is None:
            return False
        elif root.data == value:
            return True
        elif root.data > value:
            return self.search(root.leftChild, value)
        else:
            return self.search(root.rightChild, value)

    # Problem - Get the height of the binary search tree
    # The height of a binary search tree is the number
    # of edges between the tree's root and its furthest leaf
    def getHeight(self, root):
        return -1 if root is None else 1 + max(self.getHeight(root.leftChild), self.getHeight(root.rightChild))

    # Find the smallest element
    def findSmallestElement(self, root):
        # Let's check if the binary tree is empty
        if root is None:
            return False
        # Check if the current node is the leftmost
        elif root.leftChild is None:
            return root.data
        # Let's check the left subtree of the current node
        else:
            return self.findSmallestElement(root.leftChild)

    def findLargestElement(self, root):
        if root is None:
            return False
        elif root.rightChild is None:
            return root.data
        else:
            return self.findLargestElement(root.rightChild)
