import unittest
from singleton_pattern import MetaSingleton


class Example(metaclass=MetaSingleton):
    pass


class MyTestCase(unittest.TestCase):
    def test_singleton(self):
        object1 = Example()
        object2 = Example()
        self.assertEqual(object1, object2)


if __name__ == '__main__':
    unittest.main()
