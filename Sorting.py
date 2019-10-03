# -*- Coding: utf-8 -*-
from time import time


def quick_sort(inp):

    
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

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    pl = 0
    pr = 0
    merged = []
    length = len(left) + len(right)

    while len(merged) < length:
        if left[pl] <= right[pr]:
            merged.append(left[pl])
            pl += 1
        else:
            merged.append(right[pr])
            pr += 1

        if pl == len(left):
            merged += right[pr:]
            return merged
        if pr == len(right):
            merged += left[pl:]

    return merged

def merge_sort(inp):

    length = len(inp)

    if length <= 1:
        return inp

    left, right = inp[:length//2], inp[length//2:]

    return merge_sorted_lists(merge_sort(left), merge_sort(right))

def insertion_sort(to_be_sorted):
    """
    Quadratic, i.e. O(n^2)
    :param to_be_sorted:
    :return:
    """

    if len(to_be_sorted) < 2:
        return to_be_sorted

    for i in range(1, len(to_be_sorted)):
        j = i - 1

        while to_be_sorted[j] > to_be_sorted[i]:
            j -= 1

        to_be_sorted.insert(j+1, to_be_sorted[i])
        del to_be_sorted[i + 1]

    return to_be_sorted


def shell_sort(to_be_sorted):
    """
    Subquadratic
    :param to_be_sorted:
    :return:
    """

    if len(to_be_sorted) < 2:
        return to_be_sorted

    gap = len(to_be_sorted) // 2

    while gap > 0:
        for i in range(gap, len(to_be_sorted)):
            j = i

            while to_be_sorted[j - gap] > to_be_sorted[j] and j >= gap:
                temp = to_be_sorted[j - gap]
                to_be_sorted[j - gap] = to_be_sorted[j]
                to_be_sorted[j] = temp
                j -= gap

        gap //= 2

    return to_be_sorted


def selection_sort(to_be_sorted):
    """
    O(n^2) as there are two nested loops
    :param to_be_sorted:
    :return:
    """

    if len(to_be_sorted) < 2:
        return to_be_sorted

    for i1 in range(len(to_be_sorted)):
        min = i1
        for i2 in range(i1 + 1, len(to_be_sorted)):
            if to_be_sorted[i2] < min:
                min = i2

        to_be_sorted[i1], to_be_sorted[min] = to_be_sorted[min], to_be_sorted[i1]

    return to_be_sorted


if __name__ == '__main__':

    list_to_sort = [[], [1], [11, 11], [1, 2, 3], [3, 2, 1], [1, 7, 3, 6, 4, 5, -2],
                    [0, 2, 4, 1, 3, 5, 99, 13, 45, 56, 77, 34, 121, 0, 2, 11134, 1]]

    for to_be_sorted in list_to_sort:
        print('to_be_sorted:', to_be_sorted)
        t = time()
        sorted_version = merge_sort(to_be_sorted)
        t = time() - t

        print('time:', t)
        print('sorted_version:', sorted_version, end='\n\n')
