#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    lst_number = list(map(float, input().split()))
    a, b = map(int, input().split())

    # max item
    print(max(lst_number))

    # сумма до последнего положительного
    lst = lst_number[::-1]
    for i, var in enumerate(lst):
        if var >= 0:
            print(sum(lst[i::]))
            break

    # сжатие списка
    for i in range(len(lst_number)):
        if a <= abs(i) <= b:
            lst_number[i] = 0
    print(lst_number)




