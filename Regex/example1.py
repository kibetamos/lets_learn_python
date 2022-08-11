# Regular expressions are a powerful language
#  for matching text patterns.
# In Python a regular expression search
#  is typically written as:
# The 'r' at the start of the pattern string designates a python
#  "raw" string which passes through backslashes without 
# change which is very handy for regular expressions
import re

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group())  ## 'b@google'

else:
    print('Not found')