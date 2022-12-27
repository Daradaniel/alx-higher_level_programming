#!/usr/bin/python3
""" matrix_divided module """
def matrix_divided(matrix, div):
    
    """ Divides all elements of matrix
        Args:
            matrix (list): list of list of integers
            div (int): integer to divide matrix by
        Returns:
            a new list with the divided matrix.
        """
    
    result = 0
    nuevo = []
    if matrix == [] or matrix == [[]]:
        raise TypeError("must be a matrix (list of lists) of integers/floats")
    if type(matrix) != list:
        raise TypeError("must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix and matrix[0]:
        for row in matrix:
            temp = []
            lenirow = matrix[0]
            if len(matrix) != 2:
                raise TypeError("must be a matrix (list of lists) of integers/floats")
            if len(row) == 0:
                raise TypeError("must be a matrix (list of lists) of integers/floats")
            if len(lenirow) != len(row):
                raise TypeError("Each row of the matrix must have the same size")
            for j in row:
                if type(j) != int and type(j) != float:
                    raise TypeError("must be a matrix (list of lists) of integers/floats")
                result = j / div
                result = round(result, 2)
                temp.append(result)
            nuevo.append(temp)
        return nuevo
    else:
        raise TypeError("must be a matrix (list of lists) of integers/floats")

