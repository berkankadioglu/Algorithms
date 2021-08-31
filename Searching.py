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
    """
    Improvement over binary search when the data is uniformly distributed...
    :param to_be_searched:
    :param searching_for:
    :return:
    """

    if to_be_searched:
        low = 0
        high = len(to_be_searched) - 1

        while low <= high and searching_for >= to_be_searched[low] and searching_for <= to_be_searched[high]:
            pos = low + int((searching_for - to_be_searched[low])*(high - low) /
                            (to_be_searched[high] - to_be_searched[low]))

            if searching_for == to_be_searched[pos]:
                return pos
            if searching_for < to_be_searched[pos]:
                high = pos - 1
            else:
                low = pos + 1

    return -1


if __name__ == '__main__':
    list_to_search = [[], [1], [11, 11], [1, 2, 3], [3, 2, 1], [1, 7, 3, 6, 4, 5, -2],
                      [0, 2, 4, 1, 3, 5, 99, 13, 45, 56, 77, 34, 121, 0, 2, 11134, 1]]

    # Testing search algorithms in UN-SORTED lists
    for to_be_searched in list_to_search:
        print('to_be_searched:', to_be_searched)
        t = time()
        # sorted_version = linear_search(to_be_searched=to_be_searched, searching_for=1)
        index = linear_search(to_be_searched=to_be_searched, searching_for=3)
        t = time() - t

        print('time:', t)
        print('index:', index, end='\n\n')

    print('\n\n\n\n\nBELOW ARE SORTED SEARCHS:')

    # Testing search algorithms in SORTED lists
    for to_be_searched in list_to_search:

        to_be_searched = insertion_sort(to_be_sorted=to_be_searched)

        print('to_be_searched:', to_be_searched)
        t = time()
        # sorted_version = linear_search(to_be_searched=to_be_searched, searching_for=1)
        index = interpolation_search(to_be_searched=to_be_searched, searching_for=3)
        t = time() - t

        print('time:', t)
        print('index:', index, end='\n\n')
