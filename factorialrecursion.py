""" A simple factorial recursion example 
"""

def factorial(n):
    if n == 0:
        print('n==0')
        return 1
    else:
        print(n)
        return n * factorial(n-1)
    
# sample usage

print(factorial(5))