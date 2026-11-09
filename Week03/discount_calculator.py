# Calculate a discount using the supplied classroom policy.
purchase_amount = float(input("Enter the purchase amount in naira: "))

if purchase_amount < 0:
    print("Invalid amount. Purchase amount cannot be negative.")
else:
    if purchase_amount < 10000:
        discount_rate = 0
    elif purchase_amount < 50000:
        discount_rate = 0.05
    else:
        discount_rate = 0.10

    discount_amount = purchase_amount * discount_rate
    final_amount = purchase_amount - discount_amount

    print(f"Original amount: NGN {purchase_amount:,.2f}")
    print(f"Discount amount: NGN {discount_amount:,.2f}")
    print(f"Final amount payable: NGN {final_amount:,.2f}")
