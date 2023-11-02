text = input()

dict_students = dict()

while ":" in text:
    data = text.split(":")

    name, id, course = data[0], data[1], data[2]

    if course not in dict_students:
        dict_students[course] = dict()

    dict_students[course][id] = name

    text = input()

student_data = text.replace("_", " ")

for id in dict_students[student_data]:
    print(f"{dict_students[student_data][id]} - {id}")
