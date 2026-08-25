#Calculator
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("\n1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for Division\n")
    operation = int(input("Enter the operation(1-4): "))
    if operation == 1:
        ans = add(a,b)
        print(f"{a} + {b} = {ans}")
    elif operation == 2:
        ans = subtract(a,b)
        print(f"{a} - {b} = {ans}")
    elif operation == 3:
        ans = multiply(a,b)
        print(f"{a} x {b} = {ans}")
    elif operation == 4:
        ans = divide(a,b)
        print(f"{a} / {b} = {ans}")
    else:
        print("Invalid option. Please try again")

except ZeroDivisionError:
    print("You cannot divide a number by zero")
except ValueError:
    print("Please Enter a valid number to calculate with")