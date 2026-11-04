# Student Grade Application

name = input("Enter student name: ")
age = input("Enter student age: ")

try:
    age = int(age)
    marks = int(input("Enter student marks: "))

    if age <= 0:
        raise ValueError("Age must be greater than 0")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

except ValueError as e:
    print("Invalid Input:", e)

else:
    print("\n----- Student Result -----")
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)

    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
        print("Result: Fail")

finally:
    print("\nThank you for using Student Grade Application!")