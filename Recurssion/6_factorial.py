from ast import Num


def factorial(n):
    if n<0:
        return n
    else:
        return n * factorial(n-1)
    
num = 6
if num < 0:
    print("Invalid input")
elif num == 0:

    print("Factorial of 0 is 1")
else:

    print("Factorial of number", num, "is", factorial(num))
     