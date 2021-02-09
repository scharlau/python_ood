""" A bad and a good version of a fibonacci method with recursion """
import unittest

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

class TestFibonacci(unittest.TestCase):
    
    def test_bad_fibonacci(self):
        wanted_result = [0,1,1,2,3,5,8,13,21,34,55,89]
        test_result = []
        for i in range (12):
            test_result.append(bad_fibonacci(i))
        self.assertEqual(wanted_result,test_result)
     
if __name__ == "__main__":
    unittest.main()
