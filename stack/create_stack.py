#We create a stack 
#will define a class named Stack 
# and will implement the Stack using python lists
# from tempfile import tempdir


from logging import exception


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

#Finally lets check the topmost element of a stack
    def top(self):
        try:
            if self.stackSize==0:
                raise Exception("Stack empty")
            return self.stackList[-1]
        except exception as e:
            print(str(e))


#Execution
s=Stack()
#push element
s.push(1)
#push element
s.push(2)
#push element
s.push(3)
print("popped element is:")
print(s.pop())
#push an element
s.push(4)
print("topmost element is:")
print(s.top())





