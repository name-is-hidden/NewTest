command = input()

courses_dict = dict()

while command != "end":
    student_data = command.split(" : ")
    course, student = student_data[0], student_data[1]

    if course not in courses_dict:
        courses_dict[course] = list()

    courses_dict[course].append(student)

    command = input()

for course, student in courses_dict.items():
    print(f"{course}: {len(student)}")
    print("-- ", end="")
    print(*student, sep="\n" "-- ")
