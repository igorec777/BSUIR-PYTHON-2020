class Vector(object):

    def __init__(self, lst):
        self.__lst = lst
        self.__length = len(self.__lst)

    def Length(self):
        return self.__length

    def Get(self, index):
        try:
            elem = self.__lst[index]
            return elem
        except IndexError:
            return ("Vector index out of range")

    def To_Str(self):
        string = ''
        for elem in self.__lst:
            string += str(elem) + ','
        return string

    def Equals(self, object):
        if self.__length != object.__length:
            return False
        else:
            i = 0
            for num in self.__lst:
                if num != object.__lst[i]:
                    return False
                i += 1
            return True

    def Sum(self, object):
        if self.__length != object.__length:
            return "Vectors have different sizes"
        else:
            new_v = []
            i = 0
            for num in self.__lst:
                new_v.append(num + object.__lst[i])
                i += 1
            return Vector(new_v)

    def Sub(self, object):
        if self.__length != object.__length:
            return "Vectors have different sizes"
        else:
            new_v = []
            i = 0
            for num in self.__lst:
                new_v.append(num - object.__lst[i])
                i += 1
            return Vector(new_v)

    def Mul_To_Const(self, const):
        new_v = []
        for num in self.__lst:
            new_v.append(num * const)
        return Vector(new_v)

    def Scalar_Mul(self, object):
        if self.__length != object.__length:
            return "Vectors have different sizes"
        else:
            result = 0
            i = 0
            for num in self.__lst:
                result += num * object.__lst[i]
                i += 1
            return result

if __name__ == '__main__':
    print("Ok")
