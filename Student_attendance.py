number_of_students= int(input("How many students are there?"))
attendance = {}


for i in range(number_of_students):
    name_of_student = input("Name: ")
    days_attended = int(input("Present Days: "))
    attendance[name_of_student] = days_attended



total_classes = 20
students_attendance = {}
noteligible_student = {}

for student,attend in attendance.items():
    attendance_percentage = (attend / total_classes)*100
    if attendance_percentage >= 75:
        students_attendance[student] = f"{attendance_percentage} - Eligible"
    else:
        students_attendance[student] = f"{attendance_percentage} - Not Eligible"
        noteligible_student[student] = f"{attendance_percentage} "
print("********************** STUDENT ATTENDANCE ***********************")
print(students_attendance)
print()
print()
print("********************* Not Eligible *************************")
print(noteligible_student)