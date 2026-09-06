# Cybersecurity Training Performance Calculator

# Input student information
student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
completed_labs = int(input("Enter number of completed labs: "))
total_labs = int(input("Enter total number of labs: "))
quiz_marks = float(input("Enter quiz marks: "))
assignment_marks = float(input("Enter assignment marks: "))
project_marks = float(input("Enter project marks: "))

# Calculate lab completion percentage
if total_labs > 0:
    lab_completion_percentage = (completed_labs / total_labs) * 100
else:
    lab_completion_percentage = 0.0

# Calculate total academic score
total_academic_score = quiz_marks + assignment_marks + project_marks

# Display report
print("\n" + "=" * 45)
print("       CYBERSECURITY TRAINING REPORT")
print("=" * 45)
print(f"Student Name        : {student_name}")
print(f"Student ID          : {student_id}")
print(f"Completed Labs      : {completed_labs}")
print(f"Total Labs          : {total_labs}")
print(f"Lab Completion      : {lab_completion_percentage:.2f}%")
print(f"Quiz Marks          : {quiz_marks:.2f}")
print(f"Assignment Marks    : {assignment_marks:.2f}")
print(f"Project Marks       : {project_marks:.2f}")
print(f"Total Academic Score: {total_academic_score:.2f}")
print("=" * 45)

