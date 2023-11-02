students_count = int(input())

student_grades = dict()

for _ in range(students_count):
    details = input().split()

    if details[0] not in student_grades:
        student_grades[details[0]] = list()

    student_grades[details[0]].append(float(details[1]))

for student, grade in student_grades.items():
    grades = ' '.join(f"{x:.2f}" for x in grade)
    print(f"{student} -> {grades} (avg: {(sum(grade)) / len(grade):.2f})")
