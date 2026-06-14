while True:
    grade = float(input("Enter student grade: "))
    attendance = float(input("Enter attendance percentage: "))

    if grade >= 70 and attendance >= 80:
        print("Admitted")
    else:
        print("Not Admitted")

    again = input("Check another student? (yes/no): ").lower()

    if again != "yes":
        print("Program ended.")
        break