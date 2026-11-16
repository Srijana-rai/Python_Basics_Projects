students={
    "Sita": 78,
    "Ram": 45,
    "Hari": 32,
    "Gita": 91,
    "Bikash": 56,
    "Ramita": 40
}

passing_marks= 40

record_dictionary={}
failed_student = {}

for student,marks in students.items():
    if marks > passing_marks:
        above = marks - passing_marks
        result1 = f"Passed - {above} above"
        record_dictionary[student]=result1
    elif marks < passing_marks:
        below = passing_marks-marks
        result2 = f"Failed - {below} below"
        record_dictionary[student]=result2
        failed_student[student] = marks
    else:
        result3 = "Exactly Passed"
        record_dictionary[student]=result3
        
print()
print()
print("================ STUDENTS RECORDS ====================")
print()
print()
print(record_dictionary)
print()
print()
print('================ Failed Student Record ================')
print(failed_student)