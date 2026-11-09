# Repeat multiplication tables until the user enters no.
answer = "yes"

while answer == "yes":
    number = int(input("Enter a whole number: "))
    print(f"Multiplication table for {number}")
    for multiplier in range(1, 13):
        print(f"{number} x {multiplier} = {number * multiplier}")

    answer = input("Do you want another table? Enter yes or no: ")
    while answer != "yes" and answer != "no":
        print("Please enter yes or no in lowercase.")
        answer = input("Do you want another table? Enter yes or no: ")

print("Program ended.")
