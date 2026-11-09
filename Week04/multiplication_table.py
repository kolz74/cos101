# Display a multiplication table from 1 to 12.
number = int(input("Enter a whole number: "))

print(f"\nMULTIPLICATION TABLE FOR {number}")
print("==============================")
for multiplier in range(1, 13):
    print(f"{number} x {multiplier} = {number * multiplier}")
