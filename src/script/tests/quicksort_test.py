#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


def swap(lst, x, y):
    temp = lst[x]
    lst[x] = lst[y]
    lst[y] = temp


def partition(lst, left, right, pivot_index):
    pivot = lst[pivot_index]
    swap(lst, right, pivot_index)
    store_index = left

    for index, item in enumerate(lst[left: right]):
        if item < pivot:
            swap(lst, store_index, left + index)
            store_index += 1

    new_pivot_index = store_index
    swap(lst, new_pivot_index, right)

    return new_pivot_index


def quick_sort(lst, left, right):
    if left < right:
        pivot_index = left + int(len(lst[left: right]) / 2)
        new_pivot_index = partition(lst, left, right, pivot_index)
        quick_sort(lst, left, new_pivot_index - 1)
        quick_sort(lst, new_pivot_index + 1, right)


if __name__ == "__main__":
    l = [7, 2, 8, 5, 3, 19, 1, 21, 59, 101, 99, 7]
    # l = [7, 2, 5, 3]
    quick_sort(l, 0, len(l) - 1)

    print(l)
