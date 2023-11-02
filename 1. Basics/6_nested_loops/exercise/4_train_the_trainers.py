jury_count = int(input())
presentation_name = input()

current_grade = 0
grades_sum = 0
average_grade = 0
counter = 0                 # counter to follow the number of average grades
sum_of_average_grades = 0

while presentation_name != "Finish":
    for _ in range(jury_count):
        current_grade = float(input())
        grades_sum += current_grade

    average_grade = (grades_sum / jury_count)
    counter += 1

    print(f"{presentation_name} - {average_grade:.2f}.")

    sum_of_average_grades += average_grade

    grades_sum = 0                                      # clear both these variables before the next iteration
    average_grade = 0                                   #

    presentation_name = input()

print(f"Student's final assessment is {(sum_of_average_grades / counter):.2f}.")
