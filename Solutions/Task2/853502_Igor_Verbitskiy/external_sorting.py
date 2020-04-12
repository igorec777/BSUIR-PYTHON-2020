import os
import random


def create_file(size):
    if size <= 1 or int(size / 2) >= 51000000:
        raise ValueError
    with open('Numbers.txt', 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(size))


def read(start, end):
    lst = []
    with open('Numbers.txt', 'r', encoding='utf-8') as handler:
        for i, line in enumerate(handler):
            if start <= i < end:
                line = line.rstrip('\n')
                lst.append(int(line))
            if i >= end:
                break
    return lst


def write(file_name, lst):
    i = 0
    with open(file_name, 'w', encoding='utf-8') as handler:
        while i < len(lst):
            if i == len(lst) - 1:
                handler.write(str(lst[i]))
                break
            handler.write(str(lst[i]) + '\n')
            i += 1


def sorting(size):
    create_file(size)
    middle = int(size / 2)
    half1 = read(0, middle)
    half1.sort()
    write('Half1.txt', half1)
    half1.clear()
    half2 = read(middle, size)
    half2.sort()
    write('Half2.txt', half2)
    half2.clear()
    file_merge(size)


def file_merge(size):
    l = r = a = 0
    l_len = r_len = 0
    r_len = size - int(size / 2)
    l_len = int(size / 2)
    handler = open("SORTED.txt", 'w', encoding='utf-8')
    fh1 = open('Half1.txt', 'r', encoding='utf-8')
    fh2 = open('Half2.txt', 'r', encoding='utf-8')
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
    os.remove("Half1.txt")
    os.remove("Half2.txt")


if __name__ == '__main__':
    print("There are a functions for external sorting")
