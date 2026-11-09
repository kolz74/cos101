# Compare two numbers.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number > second_number:
    print("The first number is larger.")
elif second_number > first_number:
    print("The second number is larger.")
else:
    print("Both numbers are equal.")
