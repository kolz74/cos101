# Week 3 take-home: extend the weekly expense calculator with a budget check.
student_name = input("Enter your name: ")
daily_transport = int(input("Enter daily transport expense in naira: "))
daily_feeding = int(input("Enter daily feeding expense in naira: "))
days = int(input("Enter number of days: "))
other_expenses = int(input("Enter other weekly expenses in naira: "))
weekly_budget = int(input("Enter your weekly budget in naira: "))

if (daily_transport < 0 or daily_feeding < 0 or days < 0
        or other_expenses < 0 or weekly_budget < 0):
    print("Invalid input. Expenses, days, and budget cannot be negative.")
else:
    total_transport = daily_transport * days
    total_feeding = daily_feeding * days
    total_expenses = total_transport + total_feeding + other_expenses

    print()
    print("WEEKLY EXPENSE SUMMARY")
    print("======================")
    print(f"Name: {student_name}")
    print(f"Transport: NGN {total_transport:,}")
    print(f"Feeding: NGN {total_feeding:,}")
    print(f"Other expenses: NGN {other_expenses:,}")
    print(f"Total expenses: NGN {total_expenses:,}")
    print(f"Weekly budget: NGN {weekly_budget:,}")

    if total_expenses < weekly_budget:
        print("Status: Within budget")
        print(f"Amount remaining: NGN {weekly_budget - total_expenses:,}")
    elif total_expenses == weekly_budget:
        print("Status: Exactly on budget")
        print("Amount remaining: NGN 0")
    else:
        print("Status: Over budget")
        print(f"Amount exceeded: NGN {total_expenses - weekly_budget:,}")
