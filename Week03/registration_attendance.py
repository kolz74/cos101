# Check registration and attendance eligibility.
registration_status = input("Registration complete? Enter yes or no: ")
attendance = float(input("Enter attendance percentage: "))

if registration_status != "yes" and registration_status != "no":
    print("Invalid registration response. Enter yes or no in lowercase.")
elif attendance < 0 or attendance > 100:
    print("Invalid attendance. Enter a value from 0 to 100.")
elif registration_status == "yes" and attendance >= 75:
    print("Eligible for the practical assessment.")
else:
    print("Not eligible for the practical assessment.")
