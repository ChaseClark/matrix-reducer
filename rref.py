# import
import numpy as np
from fractions import Fraction
import copy

# TODO
# print out if the equations are linearly independent or dependent
# add in user input on startup


# input
# print('enter number number of rows:')
# rows = int(input())
# print('enter number number of cols(including right hand side):')
# cols = int(input())

# for i in range(rows):
#     print(f'enter row vals separated by spaces for row {i+1}')
#     r = str(input())
#     matrix.append(r.split(" "))


matrix = [[1, 2, 3, 4], [4, 6, 2, 6], [2, 4, 6, 8]]


num_cols = len(matrix[0])
num_rows = len(matrix)
print(f'matrix has {num_rows} rows and {num_cols} cols')


def solve():
    do_ref()


def do_ref():
    print_matrix('original augmented matrix')

    for r in range(num_rows):
        # sort the row by putting a non zero entry in the correct position
        if (r < num_rows-1):
            sort_rows(r)

        leading = matrix[r][r]
        if leading != 0:
            if leading != 1:
                # divide entire row by leading
                for c in range(num_cols):
                    matrix[r][c] = float(matrix[r][c]) / leading
            print_matrix(
                f'r{r+1} <- r{r+1} / {str(Fraction(leading).limit_denominator(max_denominator=1000))}')
            make_zeroes_below(r, r)

    # at this point we are in ref
    # we can check for no solutions now if leading variable is in the very last column
    if has_solution():
        print('has solution!')
        do_rref()
    else:
        print('this matrix has no solution!')


def do_rref():
    # already in ref form
    print('starting rref...')
    for r in range(num_rows-1, 0, -1):
        # matrix r r should be a 1 already
        make_zeroes_above(r, r)


def check_dependence():
    pass


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
    print_matrix(f'r{index_1+1} <-> r{index_2+1}')


def make_zeroes_below(r, c):
    # we know matrix[r][c] is a one
    for i in range(num_rows-r-1):
        current_row = i + r + 1
        scale_amount = float(matrix[current_row][c])
        if scale_amount != 0:
            for j in range(num_cols):
                # subtract each value in current row by the scalar amount of the above value
                matrix[current_row][j] = matrix[current_row][j] - \
                    matrix[r][j] * scale_amount
            print_matrix(
                f'r{current_row+1} <- r{current_row+1} - ({str(Fraction(scale_amount).limit_denominator(max_denominator=1000))})r{r+1}')


def make_zeroes_above(r, c):
    for i in range(r-1, -1, -1):
        scale_amount = float(matrix[i][c])
        if scale_amount != 0:
            for j in range(num_cols):
                # subtract each value in current row by the scalar amount of the above value
                matrix[i][j] = matrix[i][j] - \
                    matrix[r][j] * scale_amount
            print_matrix(
                f'r{i+1} <- r{i+1} - ({str(Fraction(scale_amount).limit_denominator(max_denominator=1000))})r{r+1}')


# makes sure all leading values are on the left hand side of the matrix
def has_solution():
    valid = True
    for r in range(num_rows):
        if lnz(r) is not None:
            if lnz(r) >= num_cols:
                valid = False
    return valid


# returns index of leading non zero value
def lnz(row):
    for i in range(num_cols):
        current = matrix[row][i]
        if current != 0:
            return i + 1


# converts floats to decimals and uses numpy to format the matrix
def print_matrix(annotation=''):
    print()
    print(annotation)
    temp = copy.deepcopy(matrix)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i][j] = str(
                Fraction(temp[i][j]).limit_denominator(max_denominator=1000))
    print(np.matrix(temp))


solve()
