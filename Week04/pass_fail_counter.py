# Count passes and failures using a pass mark of 50.
student_count = int(input("How many students? "))

if student_count <= 0:
    print("The number of students must be greater than zero.")
else:
    pass_count = 0
    fail_count = 0

    for student_number in range(1, student_count + 1):
        score = float(input(f"Enter score for student {student_number}: "))
        if score >= 50:
            pass_count += 1
        else:
            fail_count += 1

    print(f"Number of students: {student_count}")
    print(f"Number of passes: {pass_count}")
    print(f"Number of failures: {fail_count}")
