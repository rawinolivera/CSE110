# grade = float(input("What is you grade percentage? "))

# if grade > 70:
#     print("Great Job, You passed the class")
# else:
#     print("Work hard the next time!")

# if grade > 90:
#     print("You letter grade is: A")
# elif grade >= 80:
#     print("You letter grade is: B")
# elif grade >= 70:
#     print("You letter grade is: C")
# elif grade >= 60:
#     print("You letter grade is: D")
# else:
#     print("You letter grade is: F")

grade = float(input("What is you grade percentage? "))

if grade > 70:
    print("Great Job, You passed the class")
else:
    print("Work hard the next time!")

if grade >= 93:
    print("You letter grade is: A")
elif grade < 93:
    print("You letter grade is: A-")
elif grade >= 87:
    print("You letter grade is: B+")
elif grade < 87 and grade >= 83:
    print("You letter grade is: B")
elif grade < 83:
    print("You letter grade is: B-")
elif grade >= 77:
    print("You letter grade is: C+")
elif grade >= 73:
    print("You letter grade is: C")
elif grade < 73:
    print("You letter grade is: C-")
elif grade >= 67:
    print("You letter grade is: D+")
elif grade >= 63:
    print("You letter grade is: D")
elif grade < 63:
    print("You letter grade is: D-")
else:
    print("You letter grade is: F")