'''
We say that lists are mutable because you can modify
them after creation.

'''
#Adding Elements
#Ways to add elements to anexisting list
'''
append, insert, or list concatenation.

'''
# 1. Append
l = [1, 2, 2]
'''append operation is the fastest 
because it neither has to traverse the list to insert 
an element at the correct position'''
l.append(4)
print(l)
# [1, 2, 2, 4]
# 2. Insert
l = [1, 2, 4]
l.insert(2, 3)
print(l)
# [1, 2, 3, 4]
# 3. List Concatenation
print([1, 2, 2] + [4])
# [1, 2, 2, 4]

#Reversing Lists
l = [1, 2, 2, 4]
l.reverse()
print(l)
# [4, 2, 2, 1]