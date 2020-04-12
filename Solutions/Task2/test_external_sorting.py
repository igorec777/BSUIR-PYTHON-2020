import unittest
import external_sorting as e_s


class TestExternalSort(unittest.TestCase):
    def test_right_sorting(self):
        size = 100000
        e_s.sorting(size)
        res_file = open('SORTED.txt', 'r', encoding='utf-8')
        i = 0
        previous_num = int(res_file.readline().rstrip('\n'))
        while i < size - 1:
            next_num = int(res_file.readline().rstrip('\n'))
            self.assertGreaterEqual(next_num, previous_num)
            previous_num = next_num
            i += 1
        res_file.close()

    def test_wrong_sorting(self):
        size = 1
        self.assertRaises(ValueError, e_s.create_file, size)


if __name__ == '__main__':
    unittest.main()

