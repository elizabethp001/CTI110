# Elizabeth Pettit
# 04/18/25
# P5LAB
# Simulate a self-checkout machine
import random

def disperse_change(change):
    coins = int(change * 100)  

    dollars = coins // 100
    coins -= dollars * 100

    quarters = coins // 25
    coins -= quarters * 25

    dimes = coins // 10
    coins -= dimes * 10

    nickels = coins // 5
    coins -= nickels * 5

    pennies = coins

    print("Change Back:")
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

def main():
    amount_due = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_due}")

    amount_paid = float(input("How much cas will you put in the self-checkout? $"))

    
    change = round(amount_paid - amount_due, 2)
    print(f"Change is: ${change}")
    disperse_change(change)  

if __name__ == "__main__":
    main()
