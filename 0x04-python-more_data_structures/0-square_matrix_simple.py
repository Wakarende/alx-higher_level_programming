#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix2 = []
    matrix2 = [[j**2 for j in i]for i in matrix]
    return matrix2
