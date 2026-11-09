# Assessed practical: process and summarise student scores.
student_count = int(input("How many students? "))

if student_count <= 0:
    print("The number of students must be greater than zero.")
else:
    total_score = 0.0
    pass_count = 0
    fail_count = 0

    for student_number in range(1, student_count + 1):
        score = float(input(f"Enter score for student {student_number}: "))

        while score < 0 or score > 100:
            print("Invalid score. Enter a value from 0 to 100.")
            score = float(input(f"Enter score for student {student_number}: "))

        total_score += score
        if score >= 50:
            pass_count += 1
        else:
            fail_count += 1

    average_score = total_score / student_count
    print("\nCLASS RESULT SUMMARY")
    print("====================")
    print(f"Number of students: {student_count}")
    print(f"Total score: {total_score:.2f}")
    print(f"Average score: {average_score:.2f}")
    print(f"Number of passes: {pass_count}")
    print(f"Number of failures: {fail_count}")
