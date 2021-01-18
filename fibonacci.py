""" A bad and a good version of a fibonacci method with recursion """

def bad_fibonacci(n):
    print("bad_fibonacci called")
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)
    
def good_fibonacci(n):
    print("good_fibonacci called")
    if n <= 1:
        return (n, 0)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b, a)

# sample usage
print("Fibonacci sequence")
for i in range (12):
    print(good_fibonacci(i))