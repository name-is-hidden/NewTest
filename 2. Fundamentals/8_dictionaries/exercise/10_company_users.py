text = input()

employees_dict = dict()

while text != "End":
    data = text.split(" -> ")

    company = data[0]
    employee_id = ("".join(data[1]))

    if company not in employees_dict:
        employees_dict[company] = list()

    if employee_id not in employees_dict[company]:
        employees_dict[company].append(employee_id)

    text = input()

for key, value in employees_dict.items():
    print(key)

    for i in value:
        print(f"-- {i}")
