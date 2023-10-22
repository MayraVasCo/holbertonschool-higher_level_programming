#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = []
        for numb in row:
            squared_row.append(numb ** 2)
        result.append(squared_row)
    return result
