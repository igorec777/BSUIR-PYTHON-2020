import unittest
from class_vector import Vector


class TestVector(unittest.TestCase):
    v1 = Vector([1, 2, 8, 5])
    v2 = Vector([3, 6, 2, 0])
    v3 = Vector([1, 6, 7])
    v4 = Vector([1, 6, 7])

    def test_len(self):
        self.assertEqual(4, len(self.v1))

    def test_index(self):
        self.assertEqual(6, self.v2[1])
        self.assertRaises(IndexError, self.v1.__getitem__, 7)

    def test_str(self):
        self.assertEqual('[1, 2, 8, 5]', str(self.v1))

    def test_eq(self):
        self.assertEqual(False, self.v1 == self.v2)
        self.assertEqual(True, self.v3 == self.v4)
        self.assertEqual(False, self.v1 == self.v3)

    def test_add(self):
        res = Vector([4, 8, 10, 5])
        self.assertEqual(True, res == self.v1 + self.v2)
        self.assertRaises(ArithmeticError, self.v1.__add__, self.v3)

    def test_sub(self):
        res = Vector([2, 4, -6, -5])
        self.assertEqual(True, res == self.v2 - self.v1)
        self.assertRaises(ArithmeticError, self.v2.__sub__, self.v4)

    def test_mul(self):
        res1 = Vector([3, 18, 21])
        self.assertEqual(True, res1 == self.v3 * 3)
        res2 = 31
        self.assertEqual(res2, self.v1 * self.v2)
        self.assertRaises(ArithmeticError, self.v1.__mul__, self.v3)


if __name__ == '__main__':
    unittest.main()
