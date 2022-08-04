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

#Problem - Get the height of the 
#The height of a binary search tree is the number 
# of edges between the tree's root and its furthest leaf
    def getHeight(self,root):
        #Write your code here
        return -1 if root is None else 1 + max(self.getHeight(root.left),
        self.getHeight(root.right))

    #Find the smallest element

    def findSmallestElement(root):
        #Lets check if the binary tree is empty
        if root == None:
            return False
            #Check if the current node is the left most
        elif root.leftChild==None:
            return root.data
        #Lets check the right subtree of current node
        else:
            return findSmallestElement(root.leftChild)
            
    def findLargestElement(root):
        if root ==None:
            return False
        elif root.rightChild == None:
            return root.data
        else:
            return findLargestElement(root.rightChild)

            
        
