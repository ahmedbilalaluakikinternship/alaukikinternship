name = input("Enter your name: ")
age = int(input("Enter your age: "))

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = 'A+'
    print("Congratulations! You have passed the exam with flying colors.")
elif marks >= 80:
    grade = 'A'
    print("You have passed the exam.")
elif marks >= 70:
    grade = 'B'
    print("You have passed the exam.")
elif marks >= 60:
    grade = 'C'
    print("You have passed the exam.")
else:
    grade = 'F'
    print("Sorry, you have failed the exam.")

print("\nStudent Details:")
    
print("Name: ", name)
print("Age: ", age)
print("Grade: ", grade) 