import math
import os
import random
import re
import sys
def gradingStudents(grade):
    rounded_grade = []
    for grade in grade:
        if grade < 38:
            rounded_grade.append(grade)
        else:
            multiple_of_five = math.ceil(grade/5)*5
            if multiple_of_five - grade < 3:
                rounded_grade.append(multiple_of_five)
            else:
                rounded_grade.append(grade)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()