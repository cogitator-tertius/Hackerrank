#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
# Print two space-separated integers on one line: the minimum sum and the
# maximum sum of  of  elements.
# Note to self: come back to this, there is definitely a more elegant way! (10/20)
def miniMaxSum(arr):
    # sum total of all numbers in array
    original_array_sum = sum(arr)

    # to find the smallest sum we'll start with the sum of all numbers, subtract
    # each element and compare to the running minimum sum
    mini_sum = original_array_sum

    # to find the largest sum, we'll start at zero and work through permutations
    # until we get the biggest
    max_sum = 0

    # loop iterates through the array elements and checks two conditions:
    #   1. original sum - element less than minimum sum? if so replace
    #   2. original sum - element gt maximum sum? if so replace
    for i in arr:

        if original_array_sum - i < mini_sum:
            mini_sum = original_array_sum - i
        if original_array_sum - i > max_sum:
            max_sum = original_array_sum - i

    print(mini_sum,  max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
