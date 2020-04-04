import os

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyError(Exception):
    def __init__(self, text):
        self.text = text

class File(metaclass = MetaSingleton):

    def __init__(self, file_name):
        self.file_name = file_name

    def Read(self, start = 0, end = 0):     
        try:
            if start > end:
                raise MyError("Wrong positions in 'Read' method")
        except MyError as mr:
            print(mr)
            exit(0)
        except FileNotFoundError:
            print("File not found")
            exit(0)
        if start == end:
            start = 0
            end = self.File_Len()
        lst = []
        with open(self.file_name, 'r', encoding = 'utf-8') as handler:
            try:
                for i, line in enumerate(handler):
                    if i >= start and i < end:
                        line = line.rstrip('\n')
                        lst.append(int(line))
                    if i >= end:
                        break
            except MemoryError:
                print("Out of memory")
                return lst.clear()
        return lst

    def Write(self, iterable):
        i = 0
        try:
            iterable = list(iterable)
        except TypeError:
            print("The object is not iterable")
            return 0    
        with open(self.file_name, 'w', encoding='utf-8') as handler:
            while i < len(iterable):
                if i == len(iterable) - 1:
                    handler.write(str(iterable[i]))
                    break
                handler.write(str(iterable[i]) + '\n')
                i += 1

    def  File_Len(self):
        try:
            with open(self.file_name) as f:
                count = 0
                for i, l in enumerate(f):
                    count = i
            return count + 1
        except FileNotFoundError:
            print("File not found")
            exit(0)

    def __File_Merge(self, current_dir):
        try:
            fh1 = open(current_dir + "Half1.txt", 'r')
            fh2 = open(current_dir + "Half2.txt", 'r')
            l = r = a = 0
            l_len = r_len = 0
            r_len = self.File_Len()
            self.file_name = current_dir + "Half1.txt"
            l_len = self.File_Len()
            handler = open(current_dir + "SORTED.txt", 'w', encoding='utf-8')
            L = fh1.readline().rstrip('\n')
            R = fh2.readline().rstrip('\n')
            while l < l_len and r < r_len:
                if int(L) < int(R):
                    handler.write(str(L) + '\n')
                    l += 1
                    L = fh1.readline().rstrip('\n')
                else:
                    handler.write(str(R) + '\n')
                    r += 1
                    R = fh2.readline().rstrip('\n')
                a += 1
            while l < l_len:
                handler.write(str(L) + '\n')
                l += 1
                L = fh1.readline().rstrip('\n')
                a += 1
            while r < r_len:
                handler.write(str(R) + '\n')
                r += 1
                R = fh2.readline().rstrip('\n')
                a += 1
            fh1.close()
            fh2.close()
            handler.close()
            os.remove(current_dir + "Half1.txt")
            os.remove(current_dir + "Half2.txt")
        except MemoryError:
            print("OutOfMemory")
            exit(0)
        except PermissionError:
            pass

    def External_Sorting(self):
        N = 0
        N = self.File_Len()
        try:
            if N <= 1:
                raise MyError("File is empty")
            m = int(N / 2)
            if m > 51000000:
                raise MyError("File is too large")
        except MyError as mr:
            print(mr)
            exit(0)
        i = len(self.file_name) - 1
        j = 0
        current_dir = ''
        while True:
            if self.file_name[i] == "\\":
                break
            i -= 1
        while j < i:
            current_dir += self.file_name[j]
            j += 1
        current_dir += "\\"      
        main_file = self.file_name
        half1 = self.Read(0, m)
        half1.sort()
        self.file_name = current_dir + "Half1.txt"
        self.Write(half1)
        half1.clear()
        self.file_name = main_file
        half2 = self.Read(m, N)
        half2.sort()
        self.file_name = current_dir + "Half2.txt"
        self.Write(half2)
        half2.clear()
        self.__File_Merge(current_dir)

if __name__ == '__main__':
    
    print("OK")