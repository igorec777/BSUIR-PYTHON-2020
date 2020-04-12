from cached_decorator import cached
import unittest


class TestCachedDecorator(unittest.TestCase):

    def test_cached(self):
        @cached(80)
        def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n - 1) + fib(n - 2)

        self.assertEqual(99194853094755497, fib(83))

    def test_wrong_cached(self):
        @cached(-4)
        def some_func():
            pass
        self.assertRaises(TypeError, some_func)


if __name__ == '__main__':
    unittest.main()