# import
import numpy as np
from fractions import Fraction
from decimal import Decimal

# input
# print('enter number number of rows:')
# rows = int(input())
# print('enter number number of cols(including right hand side):')
# cols = int(input())

# for i in range(rows):
#     print(f'enter row vals separated by spaces for row {i+1}')
#     r = str(input())
#     matrix.append(r.split(" "))

steps_list = []  # this will hold all of the operations performed on the matrix
matrix = [[-4, 2, -3], [2, 1, 5], [3, 5, 6]]


def solve():
    do_ref()

# need func to check if matrix is rref or not
# also should check for no soution 0 0 0 | X

# convert to row echelon form


def do_ref():
    for i in range(len(matrix)):
        row = matrix[i]
        # print(lnz(matrix[i]))
        leading = lnz(row)
        if leading != 0 or leading is not None:
            # step 1 scale to 1
            # if not 1 divide whole row by leading
            if leading != 1:
                for j in range(len(row)):
                    matrix[i][j] = float(matrix[i][j]) / leading

                # step 2 eliminate all non zero entries below
                if i < len(matrix):
                    for x in range(len(matrix) - i):
                        next_index = i + x
                        # check if target row is negative or positive so we know whether to add or subtract
                        


# do rref reduced row echelon form
# assumes input is already in ref form


# method to check an array and return the leading non zero number
# (the last number is the right hand side so we ignore)


def lnz(row):
    for i in range(len(row)-1):
        current = row[i]
        if current != 0:
            return current

# rref = check_rref(matrix)
# rref steps


# def dec_to_fraction(dec):
#     n, d = Decimal(str(dec)).as_integer_ratio()

# use numpy for ez formatting (need to make sure to use fractions over decimals)
solve()
# convert dec to fractions

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = str(
            Fraction(matrix[i][j]).limit_denominator(max_denominator=1000))
print(np.matrix(matrix))
