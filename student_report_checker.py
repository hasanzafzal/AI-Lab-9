import csv
import re

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

input_file = "students.csv"
output_file = "report.txt"

low_marks_students = []
invalid_emails = []

with open(input_file, "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        name = row[0]
        marks = int(row[1])
        email = row[2]
        if marks < 12:
            low_marks_students.append(name)
        if not re.search(email_pattern, email):
            invalid_emails.append(name)

with open(output_file, "w") as file:
    file.write("STUDENT REPORT\n")
    file.write("Students with marks less than 12:\n")
    for student in low_marks_students:
        file.write(student + "\n")
    file.write("\nInvalid Email Addresses:\n")
    for student in invalid_emails:
        file.write(student + "\n")

print("=== STUDENT REPORT ===\n")

print("Students with marks < 12:")
for student in low_marks_students:
    print(student)

print("\nInvalid Emails:")
for student in invalid_emails:
    print(student)

print("\nReport saved as report.txt")