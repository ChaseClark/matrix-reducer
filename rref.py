# import
import numpy as np
from fractions import Fraction
from decimal import Decimal
import copy

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
matrix = [[1, 2, -3], [3, 0, 5], [4, 2, 3]]

num_cols = len(matrix[0])
num_rows = len(matrix)
print(f'matrix has {num_rows} rows and {num_cols} cols')


def solve():
    do_ref()


def do_ref():
    print_matrix()

    for r in range(num_rows):  # iterate over the cols - 1
        # sort the row by putting a non zero entry in the correct position
        if (r < num_rows-1):
            sort_rows(r)

        # check [c][c] needs to be scaled to 1
        leading = matrix[r][r]
        print(f'leading {leading}')
        if leading != 0:
            if leading != 1:
                # divide entire row by leading
                for c in range(num_cols):
                    matrix[r][c] = float(matrix[r][c]) / leading
            print_matrix()
            make_zeroes_below(r, r)

    # at this point we are in ref
    # we can check for no solutions now if leading variable is in the very last column
    if has_solution():
        print('has solution!')
    else:
        print('this matrix has no solution!')

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
        current_row = i + r + 1
        print(f'current row {current_row}')
        scale_amount = float(matrix[current_row][c])
        print(f'scale amount: {scale_amount}')
        for j in range(num_cols):
            if scale_amount != 0:  # subtract
                # subtract each value in current row by the scalar amount of the above value
                matrix[current_row][j] = matrix[current_row][j] - \
                    matrix[r][j] * scale_amount
        print_matrix()


# makes sure all leading values are on the left hand side of the matrix
def has_solution():
    valid = True
    for r in range(num_rows):
        print(lnz(r))
        if lnz(r) >= num_cols:
            valid = False
    return valid


# returns index of lnz
def lnz(row):
    for i in range(num_cols):
        current = matrix[row][i]
        if current != 0:
            return i + 1


def print_matrix():
    print()
    temp = copy.deepcopy(matrix)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i][j] = str(
                Fraction(temp[i][j]).limit_denominator(max_denominator=1000))
    print(np.matrix(temp))


solve()
print_matrix()
