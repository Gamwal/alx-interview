#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Function that returns list of lists of integers
    representing the Pascal's triangle

    Args:
      n: number of levels
    Returns:
      integers: pascal's triangle
    """

    if n <= 0:
        return []
    final_list = []
    curr_list = [1]

    while n > 0:
        final_list.append(curr_list)
        curr_list = [0] + curr_list + [0]
        curr_list = [(curr_list[i] + curr_list[i+1])
                     for i in range(len(curr_list) - 1)]
        n -= 1
        if n == 0:
            break
    return final_list
