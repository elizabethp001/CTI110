# Elizabeth Pettit
# P4Lab2
# 04/10/25
# Tests student's knowledge on how to write code using loops.

num_a = int(input('Enter an integer: '))

if num_a < 0:
        print('This program does not handle negative numbers')

else:
    while num_a >= 0:
        print(f'Multiplication Table for {num_a}: ')
        for n in range(1, 13):
            print(f"{num_a} x {n} = {num_a * n}")

        run_again = input('Would you like to run the program again (yes/no): ')

        if run_again == "yes":
            num_a = int(input('Enter an integer: '))
        else:
            print('Exiting Program...')
            break
        
