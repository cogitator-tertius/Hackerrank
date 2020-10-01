##Function Description
##
##Complete the plusMinus function in the editor below.
##
##plusMinus has the following parameter(s):
##
##int arr[n]: an array of integers
##Print
##Print the ratios of positive, negative and zero values in the array. Each value
##should be printed on a separate line with  digits after the decimal. The
##function should not return a value.

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    positive_count = 0
    negative_count = 0
    for i in arr:

        #  count positives
        if i > 0:
            positive_count += 1

        # count negatives
        if i < 0:
            negative_count += 1

    # if the element is not positive or negative, it has to be 0, so no need to
    # count those entries. This could be in the main loop as an else I suppose.
    zero_count = n - positive_count - negative_count

    # Let's try casting these division results to a string and slicing to print
    # the specified number of decinmal places - being aware this creates
    # rounding errors. We'll need two elements to get past the decimal point,
    # plus 6 more for the problem statement. 2 + 6 - 1 = 7

    # ratio = str(positive_count / n)
    # print(ratio[0:7])

    # That didn't work... but there is no stipulation barring format()
    print(format(positive_count / n, '.6f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
