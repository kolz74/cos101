# Calculate the total and average of three scores.

score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: "))
score3 = float(input("Enter the third score: "))

total_score = score1 + score2 + score3
average_score = total_score / 3

print(f"Total score: {total_score:.2f}")
print(f"Average score: {average_score:.2f}")
