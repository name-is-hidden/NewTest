rows_count = int(input())

result_dictionary = dict()

for row in range(rows_count):
    student_name = input()
    student_result = float(input())

    if student_name not in result_dictionary:
        result_dictionary[student_name] = list()

    result_dictionary[student_name].append(student_result)

for name, result in result_dictionary.items():
    average_result = (sum(result_dictionary[name]) / len(result_dictionary[name]))

    if average_result >= 4.50:
        print(f"{name} -> {average_result:.2f}")
