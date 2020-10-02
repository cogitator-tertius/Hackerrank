#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
# I think there is a solution using the powers of ten method from the
# trianglequest problem... but I want to play with strings :)
def staircase(n):

# Declare variables...
    staircase_string = ''
    stair_element =  '#'
    i = 0
    line_number = 0

# Construct the first string, using n -1 spaces and one pound sign...
# this is kinda janky and I'm sure there is a more elegant solution but *shrug*
##    while i <= n:
##        if i < n:
##            staircase_string += ' '
##        else:
##            staircase_string += '#'
##        i += 1

    while i < n -1:
        staircase_string += ' '
        i += 1

    staircase_string += stair_element
# now that the first string is ready, print it and set number of lines printed
# to 1. Then, add a stair to the end and print a sliced version of the string
# using the line number as the starting index.
    print(staircase_string)
    line_number = 1

    while line_number < n:
        staircase_string += stair_element
        print(staircase_string[line_number:])
        line_number += 1




if __name__ == '__main__':
    n = int(input())

    staircase(n)
