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

def main():
    pass

##Consider a list (list = []). You can perform the following commands:
##
## insert i e: Insert integer  at position .
## print: Print the list.
## remove e: Delete the first occurrence of integer .
## append e: Insert integer  at the end of the list.
## sort: Sort the list.
## pop: Pop the last element from the list.
## reverse: Reverse the list.
## Initialize your list and read in the value of  followed by  lines of commands
## where each command will be of the  types listed above. Iterate through each
## command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    #initialize empty variables - not necessary but how my brain works
    arguments = []
    workinglist = []
    cmd_args = []
    cmd_count = 0
    #this loop will iterate n times up to the number provided by the user
    while cmd_count < N:
        #split the input into command and integer given with command
        #the insert command comes with 2 arguments so we won't rely on splitting
        #to only one argument
        command, *arguments = input().split()
        #convert the arguments to list of integers
        cmd_args = list(map(int,arguments))
        #This is going to be messy and not very elegant but...
        if command == "insert":
            #insert i e:  integer e at position i
            workinglist.insert(cmd_args[0], cmd_args[1])
        if command == "print":
            #print the list
            print(workinglist)
        if command == "remove":
            #delete the first occurence of integer
            workinglist.remove(cmd_args[0])
        if command == "append":
            #append integer to list
            workinglist.append(cmd_args[0])
        if command == "sort":
            #sort the list
            workinglist.sort()
        if command == "pop":
            #remove the last element in the list
            workinglist.pop()
        if command == "reverse":
            #reverse the list
            workinglist.reverse()
        cmd_count = cmd_count + 1

#note to self - while this works it is not extensible very easily, consider
#using eval() and some string parsing techniques to read the commands directly
#and execute them without needing all the conditional statements

