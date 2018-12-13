# -*- Coding: utf-8 -*-
from time import time


def bubble_sort(to_be_sorted):
    if len(to_be_sorted) < 2:
        return to_be_sorted

    for ind1 in range(len(to_be_sorted) - 1, 0, -1):
        for ind2 in range(ind1):
            if to_be_sorted[ind2] > to_be_sorted[ind2 + 1]:
                temp = to_be_sorted[ind2]
                to_be_sorted[ind2] = to_be_sorted[ind2 + 1]
                to_be_sorted[ind2 + 1] = temp

    return to_be_sorted


def merge(left, right):
    temp = []

    while left and right:
        if left[0] < right[0]:
            temp.append(left[0])
            del left[0]
        else:
            temp.append(right[0])
            del right[0]

    if left:
        temp += left
        return temp

    temp += right
    return temp


def merge_sort(to_be_sorted):

    if len(to_be_sorted) < 2:
        return to_be_sorted

    mid = len(to_be_sorted) // 2

    left = to_be_sorted[:mid]
    right = to_be_sorted[mid:]

    sorted_left = merge_sort(to_be_sorted=left)
    sorted_right = merge_sort(to_be_sorted=right)

    return merge(left=sorted_left, right=sorted_right)


def insertion_sort(to_be_sorted):

    if len(to_be_sorted) < 2:
        return to_be_sorted

    for i in range(1, len(to_be_sorted)):
        j = i -1

        while to_be_sorted[j] > to_be_sorted[i]:
            j -= 1

        to_be_sorted.insert(j+1, to_be_sorted[i])
        del to_be_sorted[i + 1]

    return to_be_sorted


def shell_sort(to_be_sorted):

    if len(to_be_sorted) < 2:
        return to_be_sorted


if __name__ == '__main__':

    list_to_sort = [[], [1], [11, 11], [1, 2, 3], [3, 2, 1], [1, 7, 3, 6, 4, 5, -2]]

    for to_be_sorted in list_to_sort:
        print('to_be_sorted:', to_be_sorted)
        t = time()
        sorted_version = insertion_sort(to_be_sorted=to_be_sorted)
        t = time() - t

        print('time:', t)
        print('sorted_version:', sorted_version, end='\n\n')
