# https://www.python-course.eu/python3_recursive_functions.php

def exercise1(n):
    """
    Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3.
    """

    if n > 0:
        return 3 + exercise1(n - 1)
    else:
        return 0

def exercise2(n):
    """
    Write a recursive Python function that returns the sum of the first n integers.
    """

    if n > 0:
        return n + exercise2(n - 1)
    else:
        return 0

def exercise3(n):
    """
    Write a function which implements the Pascal's triangle:

    1
    1    1
    1    2    1
    1    3    3    1
    1    4    6    4    1
    1    5    10    10    5    1
    """

    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    else:
        cont = [1]
        prev = exercise3(n-1)
        prev_line = prev[-1]
        for i in range(n-2):
            cont.append(prev_line[i] + prev_line[i+1])
        cont.append(1)

        prev.append(cont)

        return prev

def exercise4(n):
    """
    The Fibonacci numbers are hidden inside of Pascal's triangle. If you sum up the coloured numbers of the following triangle, you will get the 7th Fibonacci number:
    1
    1    1
    1    2    1
    1    3    3    -1
    1    4    -6    4    1
    1    -5    10    10    5    1
    -1    6    15    20    15    6    1

    Write a recursive program to calculate the Fibonacci numbers, using Pascal's triangle. 
    """


if __name__ == '__main__':
    print(exercise3(1))
    print(exercise3(2))
    print(exercise3(3))
