# Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.
#
# The data structure is a multi-dimensional Array, i.e:
#
# [
#   [7,8,4,  1,5,9,  3,2,6],
#   [5,3,9,  6,7,2,  8,4,1],
#   [6,1,2,  4,3,8,  7,5,9],
#
#   [9,2,8,  7,1,5,  4,6,3],
#   [3,5,7,  8,4,6,  1,9,2],
#   [4,6,1,  9,2,3,  5,8,7],
#
#   [8,7,6,  3,9,4,  2,1,5],
#   [2,4,3,  5,6,1,  9,7,8],
#   [1,9,5,  2,8,7,  6,3,4]
# ]
# Rules for validation
#
# Data structure dimension: NxN where N > 0 and √N == integer
# Rows may only contain integers: 1..N (N included)
# Columns may only contain integers: 1..N (N included)
# 'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

class Sudoku(object):
    def __init__(self, board):
        self.__board = board

    def is_valid(self):

        # template for comparison with rows, columns and regions
        control_set = set()
        for i in self.__board:
            control_set.update(i)
            break

        # the length of the template to set the size of the regions later.
        length_control_set = len(control_set)

        regions = 0
        if length_control_set > 3:
            regions = 3

        if length_control_set == 4:
            regions = 2

        # if the template is 1 long, check whether it is a number or not
        try:
            if length_control_set == 1:
                for i in control_set:
                    if str(i) in set("1"):
                        return True
                    else:
                        return False

            # check rows
            # at the first inequality with the template, false is returned
            for i in range(0, length_control_set):
                if control_set != set(self.__board[i]):
                    return False

            # check columns
            # at the first inequality with the template, false is returned
            a = 0
            for i in range(0, length_control_set):
                temp_set = set()
                for i in range(0, length_control_set):
                    temp_set.add(self.__board[i][a])
                a += 1
                if control_set != temp_set:
                    return False

            # check regions.
            # at the first inequality with the template, false is returned
            # Checking if the template length is less than 9
            if length_control_set <= 9:
                for i in range(regions):
                    for j in range(regions):
                        temp_set = set()
                        for line in self.__board[i * regions:(i + 1) * regions]:
                            temp_set.update(line[j * regions:(j + 1) * regions])

                        if control_set != temp_set:
                            return False

            # if the check of the column, row and 3x3 matrix is passed,
            # True is returned
            return True

        except IndexError:
            # If the lengths of columns, rows or 3x3 matrices are not
            #  equal to the length of the template, an error is raised
            # and false is returned accordingly
            return False