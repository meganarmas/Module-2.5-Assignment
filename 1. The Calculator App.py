# Objective: The aim of this assignment is to build a basic calculator 
# that can perform addition, subtraction, multiplication, and division.
# Task 1: Create functions for each arithmetic operation.
# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# Task 3: Ensure your code can handle division by zero and other potential errors. 
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter 1, 2, 3, 4: ")
    if choice in ('1', '2', '3', '4',):
            number_1 = float(input("Enter number 1: "))
            number_2 = float(input("Enter number 2: "))
    if choice == '1':
            print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif choice == '2':
            print(number_1, "-", number_2, "=", subtract(number_1, number_2))   
    elif choice == '3':
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif choice == '4':
            print(number_1, "/", number_2, "=", divide(number_1, number_2))
    else:
         print("Invalid numbers. Please restart.")