#!/usr/bin/python3

"""Defines a Pascal's triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of numbers
    representing the Pascal's triangle of n
    Args:
        n (int): integer whose Pascal's triangle is returned
    Returns:
        list of lists of numbers
        otherwise [] if n <= 0
    """
    if n <= 0:
        return []

    triangles = [[1]]
    for rows in range(1, n):
        row = triangles[-1]
        temp = [1]
        for i in range(len(row) - 1):
            temp.append(row[i] + row[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
