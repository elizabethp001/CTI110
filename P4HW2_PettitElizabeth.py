# Elizabeth Pettit
# 4/11/205
# P34HW2
# Assess student understanding of decision structures

#Pseudocode:
#1. Asks the user to enter name of employee.
#2. Ask user to enter number of hours the employee worked this week.
#3. Ask user to enter employee's pay rate.
#4. Evaluate if employee has worked overtime (more than 40 hours). If so, calculate the amount owed to employee for overtime hours.
#5. The employee should receive 1.5 times their normal pay rate for any overtime hours worked.
#6. Calculate the pay for regular hours.
#7. Display gross pay (total amount owed)
#8. Display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).


employee_name = input("Enter the employee's name (or type 'Done' to finish): ")

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

while employee_name != "Done":  
    hours_worked = float(input(f"Enter the number of hours {employee_name} worked: "))
    pay_rate = float(input(f"Enter the pay rate for {employee_name}: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    print("----------------------------------------")
    print(f"Employee name: {employee_name}")
    print("Hours Worked    Pay Rate    Overtime    Overtime Pay    Regular Pay    Gross Pay")
    print("----------------------------------------")
    print(f"{hours_worked:<15.2f} {pay_rate:<11.2f} {overtime_hours:<11.2f} {overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<12.2f}")
    print("----------------------------------------")

    num_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    employee_name = input("Enter the employee's name (or type 'Done' to finish): ")

print("\nSummary of Payroll Calculation:")
print("----------------------------------------")
print(f"Total employees entered: {num_employees}")
print(f"Total overtime paid: ${total_overtime_pay:.2f}")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")
print("----------------------------------------")
