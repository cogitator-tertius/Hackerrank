#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aidan
#
# Created:     28/10/2020
# Copyright:   (c) aidan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##Let's learn about list comprehensions! You are given three integers x  y and z
##representing the dimensions of a cuboid along with an integer . Print a list of
##all possible coordinates given by (i,j,k)  on a 3D grid where the sum of i+j+k
##is not equal to 10. Please use list comprehensions rather than multiple loops,
##as a learning exercise.


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# hopefully this is correct sytactically, it should print every z combined with
# every y combined with every x in the ranges given, then only print the sets
# where the sum is not equal to n.

print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n])