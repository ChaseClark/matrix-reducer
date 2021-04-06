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

steps_list = []
# matrix = [[0, 2, -3], [2, 0, 5], [1, 4, 6], [0, 1, 3]]
matrix = [[0, 2, -3], [5, 0, 5], [1, 2, 3]]

num_cols = len(matrix[0])
num_rows = len(matrix)
print(f'matrix has {num_rows} rows and {num_cols} cols')


def solve():
    do_ref()


def do_ref():
    print()

    for r in range(num_rows):  # iterate over the cols - 1
        # sort the row by putting a non zero entry in the correct position
        if (r < num_rows-1):
            sort_rows(r)

        # check [c][c] needs to be scaled to 1
        leading = matrix[r][r]
        if leading != 0:
            if leading != 1:
                # divide entire row by leading
                for c in range(num_cols):
                    matrix[r][c] = float(matrix[r][c]) / leading

            make_zeroes_below(r, r)

        # for r in range(num_rows):
        #     found_leading = False
        #     # print(matrix[r][c])
        #     x = matrix[r][c]  # this is the ideal leading position
        #     if x != 0 and not found_leading:
        #         # create a 1 in this spot
        #         if x != 1:
        #             for j in range(num_cols-c):
        #                 matrix[r][j+c] = float(matrix[r][j+c]) / x
        #         found_leading = True


# this method attempts to place a nonzero leading number
# at the top most position in the matrix


def sort_rows(c):
    target = matrix[c][c]  # this should be a non zero number after sorting
    if target == 0:
        # need to look below
        found = False
        for i in range(num_rows-c-1):
            if not found:
                val = matrix[c+i+1][c]
                if val != 0:
                    found = True
                    swap_rows(c, c+i+1)


def swap_rows(index_1, index_2):
    temp = matrix[index_1]
    matrix[index_1] = matrix[index_2]
    matrix[index_2] = temp


def make_zeroes_below(r, c):
    # we know matrix[r][c] is a one
    for i in range(num_rows-r-1):
        print(matrix[i])
        scale_amount = matrix[i+r][c]
        for j in range(len(matrix[i+r])):
            print('set me to zero and subtract from right values by the scaled amount')


def lnz(row):
    for i in range(len(row)-1):
        current = row[i]
        if current != 0:
            return current


# use numpy for ez formatting (need to make sure to use fractions over decimals)
solve()
# convert dec to fractions

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = str(
            Fraction(matrix[i][j]).limit_denominator(max_denominator=1000))
print(np.matrix(matrix))
