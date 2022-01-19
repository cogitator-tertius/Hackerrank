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

if __name__ == '__main__':
    main()
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        print(name)
        print(line)
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #find the matching student name in the 2d array and collect their scores
    student_scores = student_marks[query_name]
    #sum the scores to find the total
    total_score = sum(student_scores)
    print(total_score)
    #divide by number of scores
    avg_score = total_score/len(student_scores)
    #print average score to 2 decimal points
    print("{:.2f}".format(avg_score))