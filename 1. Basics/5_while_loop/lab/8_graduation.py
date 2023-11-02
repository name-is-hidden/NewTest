student_name = input()

grade = 1
failed_tries = 0
grades_sum = 0
is_rejected = False

while grade <= 12:
    current_class_grade = float(input())

    if current_class_grade < 4:
        failed_tries += 1

        if failed_tries > 1:
            is_rejected = True
            break

        continue

    grade += 1
    grades_sum += current_class_grade

average = grades_sum / (grade - 1)

if is_rejected:
    print(f"{student_name} has been excluded at {grade} grade")

else:
    print(f"{student_name} graduated. Average grade: {average:.2f}")
