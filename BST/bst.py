from operator import truediv


class BinaryTreeSearch:
    def __init__ (self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(root,newvalue):
        # if binary search tree is empty, create a new node and declare it as root
        if root is None:
            root = BinaryTreeSearch(newvalue)
            return root

        if newvalue<root.data:
            root.leftchild = insert(root.leftChild,newvalue)
        else:

            root.rightchild = insert(root.rightchild,newvalue)
        return root
#we can now search the above tree
    def search(root,value):
        if root is None:
            return False
        elif root.data == value:
            return True

        elif root.data> value:
            return search(root.leftChild, value)
        else:
            return search(root.rightChild,value)
        
