# Calculate total and average expenses over several days.
number_of_days = int(input("How many days do you want to record? "))

if number_of_days <= 0:
    print("Enter a number of days greater than zero.")
else:
    total_expenses = 0.0
    for day in range(1, number_of_days + 1):
        expense = float(input(f"Enter expense for day {day}: "))
        while expense < 0:
            print("Expense cannot be negative. Please try again.")
            expense = float(input(f"Enter expense for day {day}: "))
        total_expenses += expense

    average_expense = total_expenses / number_of_days
    print("\nEXPENSE SUMMARY")
    print("===============")
    print(f"Number of days: {number_of_days}")
    print(f"Total expenses: NGN {total_expenses:,.2f}")
    print(f"Average per day: NGN {average_expense:,.2f}")
