# Perform four arithmetic operations on two numbers.

print("BASIC ARITHMETIC CALCULATOR")
print("==========================")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number (not zero): "))

sum_result = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
quotient = first_number / second_number

print()
print(f"Sum: {sum_result:.2f}")
print(f"Difference: {difference:.2f}")
print(f"Product: {product:.2f}")
print(f"Quotient: {quotient:.2f}")
