# Perform one selected arithmetic operation safely.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = first_number + second_number
    print(f"Result: {result:.2f}")
elif operation == "-":
    result = first_number - second_number
    print(f"Result: {result:.2f}")
elif operation == "*":
    result = first_number * second_number
    print(f"Result: {result:.2f}")
elif operation == "/":
    if second_number == 0:
        print("Cannot divide by zero.")
    else:
        result = first_number / second_number
        print(f"Result: {result:.2f}")
else:
    print("Invalid operation. Choose +, -, *, or /.")
