#We create a stack 
#will define a class named Stack 
# and will implement the Stack using python lists
# from tempfile import tempdir


class Stack:
    def __init__ (self):
        self.stackList = []
        self.stackSize =0

        #Lets push to stack
    def push(self, item):
        self.stackList.append(item)
        self.stackSize+=1
 
#      Pop items from a stack in python
#     To remove an item from the stack i.e. 
#     to pop an element from the stack, we have to remove the
#      element from the stack which was added last to it
    def pop(self):
        try:
            if self.stackSize ==0:
                raise Exception("Stack is Empty")
            temp = self.stackList.pop()
            self.stackSize-=1
            return temp
        except Exception as e:
            print(str(e))

    #function to check the sixe of the stack
    def size(self):
        return self.stackSize

    #lets check if the stack is empty

    def isEmpty(self):
        if self.stackSize==0:
            return True
        else:
            return False







