from Vector_Working import Vector
import unittest

class Test_Vector_Methods(unittest.TestCase):
    
    def test_Scalar_Mul(self):
        v1 = Vector([2, 5, 6])
        v2 = Vector([9, 3, 5])
        self.assertEqual(v1.Scalar_Mul(v2), 63)

    def test_Mul_To_Const(self):
        v1 = Vector([4, 6, 9])
        v1 = v1.Mul_To_Const(6)
        s1 = v1.To_Str()
        new_v = Vector([24, 36, 54])
        s2 = new_v.To_Str()
        self.assertEqual(s1, s2)

    def test_Length(self):
        v1 = Vector([4, 2, 6, 5, 2, 9])
        self.assertEqual(v1.Length(), 6)

    def test_Get(self):
        v1 = Vector([1, 4, 92, 5])
        self.assertEqual(v1.Get(2), 92)

    def test_To_Str(self):
        v1 = Vector([2, 5, 2, 9])
        str_for_check = '2,5,2,9,'
        self.assertEqual(v1.To_Str(), str_for_check)

    def test_Equals(self):
        v1 = Vector([1, 5, 9, 2, 5, 2])
        v2 = Vector([2, 5, 6, 2, 5, 7])
        self.assertFalse(v1.Equals(v2))
        v2 = v1
        self.assertTrue(v1.Equals(v2))

    def test_Sum(self):
        v1 = Vector([2, 5, 6])
        v2 = Vector([2, 8, 4])
        new_v = v1.Sum(v2)
        v_for_check = Vector([4, 13, 10])
        self.assertEqual(v_for_check.To_Str(), new_v.To_Str())

    def test_Sub(self):
        v1 = Vector([5, 3, 7])
        v2 = Vector([2, 8, 1])
        new_v = v1.Sub(v2)
        v_for_check = Vector([3, -5, 6])
        self.assertEqual(v_for_check.To_Str(), new_v.To_Str())

if __name__ == '__main__':
    unittest.main()
