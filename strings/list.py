'''
We say that lists are mutable because you can modify them after creation.
'''

# Adding Elements
# Ways to add elements to an existing list
'''
append, insert, or list concatenation.
'''

# 1. Append
l = [1, 2, 2]
l.append(4)
print(l)
# Output: [1, 2, 2, 4]

# 2. Insert
l = [1, 2, 4]
l.insert(2, 3)
print(l)
# Output: [1, 2, 3, 4]

# 3. List Concatenation
l = [1, 2, 2]
l += [4]
print(l)
# Output: [1, 2, 2, 4]

# Reversing Lists
l = [1, 2, 2, 4]
l.reverse()
print(l)
# Output: [4, 2, 2, 1]
