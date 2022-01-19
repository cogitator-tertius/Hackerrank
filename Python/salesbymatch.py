#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aidan
#
# Created:     19/01/2022
# Copyright:   (c) aidan 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # the number of items in the list doesn't really matter for this problem
    # so I won't consider it for now except for finding unique socks
    # my approach is to count the number of each sock color in the list
    # first I'll construct a new array with each unique sock color in the list
    sock_pile = ar
    total_pairs_sellable = 0
    sock_color_list = []
    number_socks_of_given_color = 0
    for sock_color in sock_pile:
        # if the sock color is not already in the unique list, add it
        if sock_color not in sock_color_list:
            sock_color_list.append(sock_color)
    #check the list of unique colors in the list, for debug
    #print(sock_color_list)

    #count the number of unique sock instances in the sock pile using the sock
    #color list, for each color. Use floor division to return a whole number,
    #rounded down, of socks. then divide by 2 for
    #total number of sellable pairs, add to total, and move to next unique
    #color...

    for sock_color in sock_color_list:
        number_socks_of_given_color = sock_pile.count(sock_color)
        sock_pair_count = number_socks_of_given_color // 2
        output_string = "there are {} pairs of sock color {}".format(sock_pair_count,sock_color)
        #print(output_string)
        total_pairs_sellable =  total_pairs_sellable + sock_pair_count
        #print.format("there are now {} pairs of socks to sell.", total_pairs_sellable)

    return total_pairs_sellable



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
