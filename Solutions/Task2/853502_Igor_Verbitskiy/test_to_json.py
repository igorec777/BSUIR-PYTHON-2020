import to_json as t_j
import unittest
import json

class TestToJson(unittest.TestCase):

    def test_to_json1(self):
        A = type("A", (), {"name": "Ivan", "surname": "Petrov", "age": 24, "addres": ["Jukovo", 54]})
        obj = A()
        res = '{\n "addres": ["Jukovo", 54],\n "age": 24,\n "name": "Ivan",\n "surname": "Petrov"\n}'
        self.assertEqual(res, t_j.convert_to_json(obj))

    def test_to_json2(self):
        A = type("A", (), {"numbers": {"home": 1029452, "mobile": "+375291894320"}, "wife": None, "is_working": True})
        obj = A()
        res = '{\n "is_working": true,\n "numbers": {"home": 1029452, "mobile": "+375291894320"},\n "wife": null\n}'
        self.assertEqual(res, t_j.convert_to_json(obj))


if __name__ == '__main__':
    unittest.main()
