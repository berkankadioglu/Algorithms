from time import time
from Sorting import insertion_sort


def linear_search(to_be_searched, searching_for):
    i2 = 0

    while i2 < len(to_be_searched):
        if to_be_searched[i2] == searching_for:
            return i2
        i2 += 1

    return -1


def interpolation_search(to_be_searched, searching_for):
    return 1


if __name__ == '__main__':

    list_to_search = [[], [1], [11, 11], [1, 2, 3], [3, 2, 1], [1, 7, 3, 6, 4, 5, -2],
                      [0, 2, 4, 1, 3, 5, 99, 13, 45, 56, 77, 34, 121, 0, 2, 11134, 1]]

    for to_be_searched in list_to_search:
        print('to_be_searched:', to_be_searched)
        t = time()
        # sorted_version = linear_search(to_be_searched=to_be_searched, searching_for=1)
        sorted_version = interpolation_search(to_be_searched=insertion_sort(to_be_searched), searching_for=3)
        t = time() - t

        print('time:', t)
        print('sorted_version:', sorted_version, end='\n\n')
