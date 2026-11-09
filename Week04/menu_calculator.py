# Repeat calculator operations until the user chooses to exit.
while True:
    print("\nCALCULATOR MENU")
    print("===============")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Calculator closed. Goodbye!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Select a number from 1 to 5.")
        continue

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    if choice == "1":
        result = first_number + second_number
        print(f"Result: {result:.2f}")
    elif choice == "2":
        result = first_number - second_number
        print(f"Result: {result:.2f}")
    elif choice == "3":
        result = first_number * second_number
        print(f"Result: {result:.2f}")
    elif choice == "4":
        if second_number == 0:
            print("Cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"Result: {result:.2f}")
