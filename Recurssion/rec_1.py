def factorial(n):
    # Write your code here
    if n <= 1:
      return n
    else:
        result = n*(factorial(n-1))
        return result
