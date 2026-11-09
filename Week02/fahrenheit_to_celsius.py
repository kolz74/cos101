# Convert Fahrenheit to Celsius.

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit:.2f} degrees Fahrenheit = "
      f"{celsius:.2f} degrees Celsius")
