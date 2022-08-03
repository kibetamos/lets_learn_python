"""A palindrome is a word, phrase, number, 
or other sequence of characters which reads the same backwards and forwards. 
Can you determine if a given string, , is a palindrome?

To solve this challenge, we must first take each character in ,
 enqueue it in a queue, and also push that same character 
 onto a stack
 """
class Solution(object):
    # Write your code here
     # constructor
    def __init__ (self):
        self.__stack = []
        self.__queue = []
        
    def pushCharacter(self, ch):
        self.__stack.append(ch)

    def enqueueCharacter(self, ch):
        self.__queue.insert(0, ch)
    
    def popCharacter(self):
        return self.__stack.pop()
    
    def dequeueCharacter(self):
        return self.__queue.pop()


# Read the string s
s = input()
# Create the Solution class object
obj = Solution()   

l = len(s)
# Push / Enqueue all the characters of string s to stack
for i in range(l):
	obj.pushCharacter(s[i])
	obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
	if obj.popCharacter() != obj.dequeueCharacter():
		isPalindrome=False
		break

# Finally print whether string s is palindrome or not.
if isPalindrome:
	print("The word,", s, ", is a palindrome.")
else:
	print("The word,", s, ", is not a palindrome.")