# Demonstrate break.
print("Counting begins.")
for number in range(1, 11):
    if number == 6:
        print("Stopping at 6.")
        break
    print(number)
print("Program completed.")
