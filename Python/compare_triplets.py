import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    i = 0
    score_array = [0,0]
    while i < a.len() and i < b.len():
        if a[i] > b[i]:
            score_array[0] += 1
        if a[i] < b[i]:
            score_array[1] += 1
        i += 1
    return score_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
