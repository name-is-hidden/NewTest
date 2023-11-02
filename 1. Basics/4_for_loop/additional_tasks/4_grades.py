students_count = int(input())

failed_students = 0  # these are the students with grades ranging between 2.00 and 2.99
middle_grade_students = 0  # these are the students with grades ranging between 3.00 and 3.99
good_grade_students = 0  # these are the students with grades ranging between 4.00 and 4.99
excellent_students = 0  # these are the students with grades starting from 5.00 and above

all_grades_sum = 0      # This variable will sum all the grades in order to calculate the average

for students in range(1, students_count + 1):
    current_student_grade = float(input())
    all_grades_sum += current_student_grade

    if 2 <= current_student_grade <= 2.99:
        failed_students += 1

    elif 3 <= current_student_grade <= 3.99:
        middle_grade_students += 1

    elif 4 <= current_student_grade <= 4.99:
        good_grade_students += 1

    else:
        excellent_students += 1

print(f"Top students: {(excellent_students / students_count * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(good_grade_students / students_count * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(middle_grade_students / students_count * 100):.2f}%")
print(f"Fail: {(failed_students / students_count * 100):.2f}%")
print(f"Average: {(all_grades_sum / students_count):.2f}")
