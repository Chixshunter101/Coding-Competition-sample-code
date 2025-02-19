#Get the marks from the user
marks = float(input("Enter your marks: "))

# Determine the grade based on the marks
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Print the result
print(f"Your grade is: {grade}")
