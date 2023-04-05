#!/usr/bin/python3
"""
Module - minioperation
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n <= 0:
        return 0
    if n == 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
