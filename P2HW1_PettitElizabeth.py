# Elizabeth Pettit
# 03/12/2025
# P2HW1
# Changing the display from P2HW2

print("This program calculates and displays travel expenses")
budget = float(input("Enter budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you spend on accomodation: "))
food = float(input("How much will you spend on food? "))
expenses = gas + accommodation + food
balance = budget - expenses
print("------------Travel Expenses-----------")
print(f"{'Location: ' :<20} {destination}")
print(f"{'Initial Budget: ' :<20} $ {budget:.2f}")
print(f"{'Fuel: ' :<20} $ {gas:.2f}")
print(f"{'accommodation: ':<20} $ {accommodation:.2f}")
print(f"{'Food: ' :<20} $ {food:.2f}")
print(f"{'Remaining Balance: ' :<20} $ {balance:.2f}")
