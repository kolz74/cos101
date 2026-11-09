# Calculate the total cost of a purchase.

item_name = input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))
unit_price = float(input("Enter the unit price in naira: "))

total_cost = quantity * unit_price

print()
print("PURCHASE SUMMARY")
print("================")
print("Item:", item_name)
print("Quantity:", quantity)
print(f"Unit price: NGN {unit_price:,.2f}")
print(f"Total cost: NGN {total_cost:,.2f}")
