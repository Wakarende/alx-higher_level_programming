#!/usr/bin/python3

from threading import main_thread
from unittest import result


def square_matrix_simple(matrix=[]):
    matrix2 = []
    matrix2 = [[j**2 for j in i]for i in matrix]
    return matrix2


# def square_matrix_simple(matrix=[]):
#     matrix2 = []
#     for i in matrix:
#         result = list(map(lambda x: x**2, i))
#         matrix2.append(result)
#     return matrix2

