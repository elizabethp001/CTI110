# Elizabeth Pettit
# 03/19/2025
# P3LAB
# Tests student's knowledge of how to weite code that displays info to users.

money = float(input('Enter the amount of money as a float: '))
coins = int(money * 100)

dollars = coins // 100
coins -= dollars * 100

quarters = coins // 25
coins -= quarters * 25

dimes = coins // 10
coins -= dimes * 10

nickels = coins // 5
coins -= nickels * 5

pennies = coins

if dollars > 0:
    print(f"{dollars} dollar" if dollars == 1 else f"{dollars} dollars")
if quarters > 0:
    print(f"{quarters} quarter" if quarters == 1 else f"{quarters} quarters")
if dimes > 0:
    print(f"{dimes} dime" if dimes == 1 else f"{dimes} dimes")
if nickels > 0:
    print(f"{nickels} nickel" if nickels == 1 else f"{nickels} nickels")
if pennies > 0:
    print(f"{pennies} penny" if pennies == 1 else f"{pennies} pennies")
    
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")
