# Calculate the sum from 1 to a supplied positive whole number.
end_number = int(input("Enter a positive whole number: "))

if end_number < 1:
    print("Invalid input. Enter a number greater than or equal to 1.")
else:
    total = 0
    for number in range(1, end_number + 1):
        total += number
    print(f"The sum from 1 to {end_number} is {total}.")
