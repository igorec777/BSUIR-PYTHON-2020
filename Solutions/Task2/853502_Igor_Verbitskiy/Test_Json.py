from Json_Working import To_Json
import unittest


class Test_Json_Methods(unittest.TestCase):
    
    def test_To_Json(self):
        A = type("A", (), {"name":"Ivan", "surname":"Petrov", "age":24, "addres":["Jukovo", 54]})
        obj = A()
        s_for_check = '{\n "addres": ["Jukovo", 54],\n "age": 24,\n "name": "Ivan",\n "surname": "Petrov"\n}'
        self.assertEqual(s_for_check, To_Json(obj))

if __name__ == '__main__':
    
    unittest.main()
