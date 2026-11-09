# Assessed task: validate component scores, calculate total, grade, and decision.
student_name = input("Enter the student's name: ")
coursework = float(input("Enter coursework score out of 30: "))
examination = float(input("Enter examination score out of 70: "))

if coursework < 0 or coursework > 30 or examination < 0 or examination > 70:
    print("Invalid input. Coursework must be 0-30 and examination must be 0-70.")
else:
    total = coursework + examination

    if total >= 70:
        grade = "A"
    elif total >= 60:
        grade = "B"
    elif total >= 50:
        grade = "C"
    elif total >= 45:
        grade = "D"
    elif total >= 40:
        grade = "E"
    else:
        grade = "F"

    if total >= 50:
        decision = "Pass"
    else:
        decision = "Resit required"

    print()
    print("STUDENT RESULT SUMMARY")
    print("======================")
    print(f"Name: {student_name}")
    print(f"Coursework: {coursework:.2f} / 30")
    print(f"Examination: {examination:.2f} / 70")
    print(f"Total: {total:.2f} / 100")
    print(f"Grade: {grade}")
    print(f"Decision: {decision}")
