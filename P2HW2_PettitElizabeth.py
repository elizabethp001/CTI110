Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Elizabeth Pettit
#03/14/2025
#P2HW2
#Create a list that takes grades and displays them

#Pseudocode
#1. Ask the user to enter grades
#2. Store the entered grades in a list
#3. Calculate and display:
#   1. The lowest grade in the list
#   2. The highest grade in the list
>>> #   3. The sum of all grades from the list
>>> #   4. The average of all grades from the list
>>> 
>>> grades = []
>>> grades.append(float(input("Enter grades for Module 1: ")))
Enter grades for Module 1: 91
>>> grades.append(float(input("Enter grades for Module 2: ")))
Enter grades for Module 2: 87
>>> grades.append(float(input("Enter grades for Module 3: ")))
Enter grades for Module 3: 90
>>> grades.append(float(input("Enter grades for Module 4: ")))
Enter grades for Module 4: 90
>>> grades.append(float(input("Enter grades for Module 5: ")))
Enter grades for Module 5: 92
>>> grades.append(float(input("Enter grades for Module 6: ")))
Enter grades for Module 6: 89
>>> 
>>> lowest_grade = min(grades)
>>> highest_grade = max(grades)
>>> sum_of_grades = sum(grades)
>>> average_grade = sum_of_grades / len(grades)
>>> 
>>> print("----------Results----------")
----------Results----------
>>> print(f"Lowest Grade: {lowest_grade}")
Lowest Grade: 87.0
>>> print(f"Highest Grade: {highest_grade}")
Highest Grade: 92.0
>>> print(f"Sum Of Grades: {sum_of_grades}")
Sum Of Grades: 539.0
>>> print(f"Average: {average_grades}")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(f"Average: {average_grades}")
NameError: name 'average_grades' is not defined. Did you mean: 'average_grade'?
>>> print(f"Average: {average_grade}")
Average: 89.83333333333333
>>> print("---------------------")
---------------------
