##Given a square matrix, calculate the absolute difference between the sums of its diagonals.
##
##For example, the square matrix  is shown below:
##
##1 2 3
##4 5 6
##9 8 9

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
##    left_diag_sum = arr[0][0] + arr[-1][-1]
##    right_diag_sum = arr[0][-1] + arr [-1][0]
##    return abs(left_diag_sum - right_diag_sum)
    # that doesn't work if the array has a line that is a different length
    # correction: that ONLY works if the array is 3x3 and we can ignore the
    # center number
    primary_diag_sum = 0
    secondary_diag_sum = 0
    for i in range(0, n):

        for j in range(0,n):

            # primary diagonal is elements where i == j
            if(i == j):
                primary_diag_sum += arr[i][j]

            # secondary diagonal is a little more complicated - let's see...
            # in a 4 x 4 matrix, we need the elements from bottom left to
            # top right. That translates to [0][3], [1][2], [2][1], and [3][0]
            # so we need an equation using i & j to give us those pairs.
            # when i == 0, we want j == 3 and we can use n from the input to
            # make this work, or check and get the length of the arrays to use.
            # Turns out the equation is pretty simple math!
            # i == n - j - 1
            # 0 == 4 - 3 - 1

            if(i == (n - j - 1)):
                secondary_diag_sum += arr[i][j]

    # return the absolute value of the difference
    return abs(primary_diag_sum - secondary_diag_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
