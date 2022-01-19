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

##Given the names and grades for each student in a class of  students, store them
## in a nested list and print the name(s) of any student(s) having the second
## lowest grade.
##Note: If there are multiple students with the second lowest grade, order their
## names alphabetically and print each name on a new line.

def getStudentScore(student):
        return student[1]

def main():
    pass

if __name__ == '__main__':
    main()
    student_grades_list = []
    lowest_score = 100
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #populate nested list with names and scores
        student_grades_list.append([name,score])


    #sort the list based on scores using key func
    student_grades_list.sort(key=getStudentScore)
    i = 1

    #check for duplicate lowest scores and move the target index
    while i < len(student_grades_list):
        if student_grades_list[i][1] > student_grades_list[i-1][1]:
            break
        else:
            i = i + 1


    #the second lowest score should be at the second index in the array but
    #check to see if there are multiple identical low scores
    second_lowest_score= student_grades_list[i][1]

    #re-sort list alphabetically because that's the best way I can figure to do
    #this without creating another list of student names
    student_grades_list.sort()

    #grab all the student names that have the second lowest score and print them
    for student in student_grades_list:
        if student[1] == second_lowest_score:
            print(student[0])
