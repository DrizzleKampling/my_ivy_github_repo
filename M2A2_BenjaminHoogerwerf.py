# STUDENT DEAN'S LIST / HONOR ROLL EVALUATION
# Programmer: Benjamin Hoogerwerf
# This program will, upon being given a student's first and last name along with their GPA, determine whether that student has made either the Dean's List or the Honor Roll.

run = True

while run == True:
    stuLastName = input("Student's last name: ")

    if stuLastName == "ZZZ":
        break

    stuFirstName = input("Student's first name: ")
    stuGPA = float(input("Student's GPA: "))

    if stuGPA >= 3.5:
        print(f"{stuFirstName} {stuLastName} has made the Dean's List.\n")
    elif stuGPA >= 3.25:
        print(f"{stuFirstName} {stuLastName} has made the Honor Roll.\n")
    else:
        print(f"{stuFirstName} {stuLastName} has made neither list.\n")

quit