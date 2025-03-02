# Elizabeth Pettit
# 03/02/2025
# P1HW2
# Creating a program that does basic math on numbers entered.

print("This program calculates and displays travel expenses")
budget = int(input("Enter budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accomodation = int(input("Approximately, how much will you spend on accomodation: "))
food = int(input("How much will you spend on food? "))
expenses = gas + accomodation + food
balance = budget - expenses
print("------------Travel Expenses-----------")
print("Location: ", destination)
print("Initial Budget: ", budget)
print("Fuel: ", gas)
print("Accomodation: ", accomodation)
print("Food: ", food)
print("Remaining Balance: ", balance)
