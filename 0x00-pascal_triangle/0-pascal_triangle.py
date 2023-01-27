#!/usr/bin/python3
"""Module to return pascal triangle"""


def pascal_triangle(n):
    """
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    """
    result = []
    if n == 0:
        return result
    for i in range(n):
        result.append([])
        result[i].append(1)
        if i > 0:
            for j in range(1, i):
                result[i].append(result[i - 1][j - 1] + result[i - 1][j])
            result[i].append(1)
    return result
