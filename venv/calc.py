flag = True

def addition():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    print(f"Sum is {num1 + num2}")

def subtraction():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    print(f"Difference is {num1 - num2}")

def multiplication():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    print(f"Product is {num1 * num2}")

def division():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    print(f"Division is {num1 / num2}")

while flag == True:
    operation = input("Please type +, -, *, / or q ")
    if operation == "+":
        addition()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiplication()
    elif operation == "/":
        division()
    elif operation == "q":
        flag = False
    else:
        print("Sorry! This operation is not available")