# Elizabeth Pettit
# 03/29/25
# P3HW1
# Correct the program given and complete it.


# This program takes a number of grades and determines the average and determins the letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
sum_of_grades = sum(grades)
avg = sum_of_grades / len(grades)


# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

print("----------Results----------")
print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum Of Grades: {sum_of_grades}")
print(f"Average: {avg:.2f}")
print("---------------------")





