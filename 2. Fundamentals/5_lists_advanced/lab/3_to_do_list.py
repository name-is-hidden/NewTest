to_do_list = ["" for i in range(11)]

command = input()

while command != "End":

    command_list = command.split("-")
    priority = int(command_list[0])
    task = command_list[1]

    # to_do_list.pop(priority)
    # to_do_list.insert(priority, task)

    to_do_list[priority] = task

    command = input()

final_list = [task for task in to_do_list if task != ""]

print(final_list)
