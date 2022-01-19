#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aidan
#
# Created:     11/01/2022
# Copyright:   (c) aidan 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Given an integer, n , and n space-separated integers as input, create a tuple,
#t, of those n integers. Then compute and print the result of hash(t).
def main():
    pass

if __name__ == '__main__':
    main()
    n = int(input())
    integer_list = map(int, input().split())
    int_tuple = tuple(integer_list)
    print(hash(int_tuple))