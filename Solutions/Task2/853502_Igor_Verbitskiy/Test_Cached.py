from Cached_Working import cached
import unittest

class Test_Cached_Decorator(unittest.TestCase):
   
    def test_Cached(self):
        @cached(500)
        def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n-1) + fib(n-2)
        self.assertEqual(99194853094755497, fib(83))

if __name__ == '__main__':
    
    unittest.main()
