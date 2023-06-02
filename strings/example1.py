##Most important string methods
y = " This is lazy\t\n "

# print(y.strip())
# # Remove Whitespace: 'This is lazy'
print(''.join(["F", "B", "I"]))
# Glues together all elements in the list using the separator string: F,B,I

# print("smartphone".startswith("smart"))
# Matches the string's prefix against the argument: True

# Here are some of the most important string methods:

#  1.   strip(): Removes leading and trailing whitespace from a string.

y = " This is lazy\t\n "
print(y.strip())  # Output: 'This is lazy'


#2.  join(): Glues together all elements in a list using the separator string.

print(''.join(["F", "B", "I"]))  # Output: 'FBI'


# 3 . startswith(): Checks if a string starts with a specific prefix and returns a boolean value.

print("smartphone".startswith("smart"))  # Output: True

