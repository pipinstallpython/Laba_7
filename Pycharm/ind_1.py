#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    lst = list(map(int, input().split(' ')))
    lst_krat2 = [i for i in lst if i % 2 == 0]

    print(f"Сумма: {sum(lst_krat2)}, кол-во: {len(lst_krat2)}")
