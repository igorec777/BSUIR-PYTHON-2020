class Vector(object):

    def __init__(self, lst):
        self.__lst = lst

    def __len__(self):
        return len(self.__lst)

    def __getitem__(self, index):
        if index >= len(self.__lst):
            raise IndexError
        elem = self.__lst[index]
        return elem

    def __str__(self):
        return str(self.__lst)

    def __eq__(self, other):
        if len(self.__lst) != len(other):
            return False
        else:
            i = 0
            for num in self.__lst:
                if num != other.__lst[i]:
                    return False
                i += 1
            return True

    def __add__(self, other):

        if len(self.__lst) != len(other):
            raise ArithmeticError
        else:
            new_v = []
            i = 0
            for num in self.__lst:
                new_v.append(num + other.__lst[i])
                i += 1
            return Vector(new_v)

    def __sub__(self, other):
        if len(self.__lst) != len(other):
            raise ArithmeticError
        else:
            new_v = []
            i = 0
            for num in self.__lst:
                new_v.append(num - other.__lst[i])
                i += 1
            return Vector(new_v)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            new_v = []
            for num in self.__lst:
                new_v.append(num * other)
            return Vector(new_v)
        else:
            if len(self.__lst) != len(other):
                raise ArithmeticError
            else:
                result = 0
                i = 0
                for num in self.__lst:
                    result += num * other.__lst[i]
                    i += 1
                return result


if __name__ == '__main__':
    print("There is a class 'vector'")