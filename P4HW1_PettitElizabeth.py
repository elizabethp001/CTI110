# Elizabeth Pettit
# 04/10/2025
# P4HW1
# This program collects scores, validates them, drops the lowest, calculates an average, and determines a letter grade.



#Pseudocode
#1. Ask the user to enter grades
#2. Store the entered grades in a list
#3. Calculate and display:
# 1. The lowest grade in the list
# 2. The highest grade in the list
# 3. The sum of all grades from the list
# 4. The average of all grades from the list
 
num_grades = int(input("Enter the number of grades you want to input: "))
grades = []

for i in range(num_grades):
    grade = float(input(f"Enter grade {i+1}: "))

    while grade < 0 or grade > 100:
        print("Invalid grade! Please enter a grade between 0 and 100.")
        grade = float(input(f"Enter grade {i+1}: "))

    grades.append(grade)

lowest_grade = min(grades)
grades.remove(lowest_grade)

average_grade = sum(grades) / len(grades)

if average_grade >= 90:
    letter_grade = "A"
elif average_grade >= 80:
    letter_grade = "B"
elif average_grade >= 70:
    letter_grade = "C"
elif average_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("\n---------- Results ----------")
print(f"Lowest Grade: {lowest_grade}")
print(f"Modified List: {grades}")
print(f"Grades Average: {average_grade:.2f}")
print(f"Grade: {letter_grade}")
print("------------------------------")
