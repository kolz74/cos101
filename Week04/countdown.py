# Count down from a positive whole number to 1.
start_number = int(input("Enter a positive number: "))

if start_number < 1:
    print("Invalid input. Enter a number greater than or equal to 1.")
else:
    number = start_number
    while number >= 1:
        print(number)
        number -= 1
    print("Countdown completed.")
