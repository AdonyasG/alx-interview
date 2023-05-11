#!/udr/bin/python3
"""Module - rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix clockwise"""
    transposed = [element[:]for element in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = transposed[len(matrix) - j - 1][i]
