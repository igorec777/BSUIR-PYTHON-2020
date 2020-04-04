import File_Working as _File
import unittest
import os

# путь r"C:\Test_Modules\ и имя файла поменять на свои

class Test_File_Methods(unittest.TestCase):
    f_ = _File.File(r"C:\Test_Modules\Nums.txt")

    def test_External_Sorting(self):
        
        f = Test_File_Methods.f_
        f.External_Sorting()
        f.file_name = (r"C:\Test_Modules\SORTED.txt")  
        i = 1
        current = f.Read(0, 1)
        leng = f.File_Len()
        while i < leng - 1:
            self.assertLessEqual(current, f.Read(i, i + 1))
            i += 1
    
    def test_Read(self):

        f = Test_File_Methods.f_
        f.file_name = r"C:\Test_Modules\Nums.txt"
        lst_for_check = [1, 2, 6, 3, 2, 8, 4]
        res_lst = f.Read()
        self.assertEqual(res_lst, lst_for_check)

    def test_Write(self):     

        f = Test_File_Methods.f_
        lst = [1, 2, 6, 3, 2, 8, 4]
        with open(r"C:\Test_Modules\File_for_check.txt", 'w') as handler:
            f.file_name = r"C:\Test_Modules\File_for_check.txt"
            f.Write(lst)
        lst_for_check = f.Read()
        self.assertEqual(lst, lst_for_check)

    def test_File_Len(self):    
        
        f = Test_File_Methods.f_
        f.file_name = r"C:\Test_Modules\Nums.txt"
        right_len = 7
        self.assertEqual(f.File_Len(), right_len)

    @classmethod
    def tearDownClass(cls):

        os.remove(r"C:\Test_Modules\File_for_check.txt")

if __name__ == '__main__':

    unittest.main()
