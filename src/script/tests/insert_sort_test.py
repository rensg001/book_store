#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


def insert_sort(lst):
    n = len(lst)
    for i in range(1, n):
        temp = lst[i]
        index = i
        for j in range(i, -1, -1):
            index = j
            if j > 0 and temp < lst[j - 1]:
                lst[j] = lst[j - 1]
            else:
                break
        lst[index] = temp


l = [46, 38, 95, 2, 3, 17, 88, 66]

if __name__ == "__main__":
    insert_sort(l)
    print(l)
