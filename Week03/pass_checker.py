# Classify a valid score using a pass mark of 50.
score = float(input("Enter a score from 0 to 100: "))

if score < 0 or score > 100:
    print("Invalid score. Enter a value from 0 to 100.")
elif score >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
