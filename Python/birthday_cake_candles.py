#!/bin/python3
##
import math
import os
import random
import re
import sys

# You are in charge of the cake for a child's birthday. You have decided the
# cake will have one candle for each year of their total age. They will only be
# able to blow out the tallest of the candles. Count how many candles are tallest.
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # First find the tallest candle, then count the number of candles that are
    # the same height.
    tallest_candle = max(candles)
    tall_candle_count = candles.count(tallest_candle)
    # better off just using the built in count method?
##    for i in candles:
##        if i == tallest_candle:
##            tall_candle_count += 1

    return tall_candle_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
