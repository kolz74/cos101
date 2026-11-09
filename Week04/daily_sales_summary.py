# Take-home assignment: daily sales summary.
number_of_days = int(input("How many days? "))

if number_of_days <= 0:
    print("The number of days must be greater than zero.")
else:
    total_sales = 0.0
    high_sales_days = 0
    low_sales_days = 0

    for day in range(1, number_of_days + 1):
        sales = float(input(f"Enter sales for day {day}: "))
        while sales < 0:
            print("Sales cannot be negative. Please enter the amount again.")
            sales = float(input(f"Enter sales for day {day}: "))

        total_sales += sales
        if sales >= 10000:
            high_sales_days += 1
        else:
            low_sales_days += 1

    average_sales = total_sales / number_of_days
    print("\nDAILY SALES SUMMARY")
    print("===================")
    print(f"Total sales: NGN {total_sales:,.2f}")
    print(f"Average daily sales: NGN {average_sales:,.2f}")
    print(f"Days with sales of at least NGN 10,000: {high_sales_days}")
    print(f"Days with sales below NGN 10,000: {low_sales_days}")
