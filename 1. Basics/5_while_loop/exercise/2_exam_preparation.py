fail_threshold = int(input())

failed_attempts = 0
solved_tasks = 0
last_task = " "
grades_total = 0
has_failed = True

while failed_attempts < fail_threshold:
    current_task = input()

    if current_task == "Enough":
        has_failed = False
        break

    grade = int(input())

    if grade <= 4:
        failed_attempts += 1

    solved_tasks += 1
    grades_total += grade
    last_task = current_task

if has_failed:
    print(f"You need a break, {fail_threshold} poor grades.")

else:
    print(f"Average score: {grades_total / solved_tasks:.2f}")
    print(f"Number of problems: {solved_tasks}")
    print(f"Last problem: {last_task}")