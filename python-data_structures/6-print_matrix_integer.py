#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
<<<<<<< HEAD
    for m in range(len(matrix)):
        for x in range(len(matrix[m])):
            if x != 0:
                print(" ", end='')
            print("{:d}".format(matrix[m][x]), end='')
        print()
=======
    for row in matrix:
        print(" ".join("{:d}".format(col) for col in row))
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
