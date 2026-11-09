# Repeat until a score from 0 to 100 is entered.
score = float(input("Enter a score from 0 to 100: "))
while score < 0 or score > 100:
    print("Invalid score. Please try again.")
    score = float(input("Enter a score from 0 to 100: "))
print(f"Accepted score: {score:.2f}")
