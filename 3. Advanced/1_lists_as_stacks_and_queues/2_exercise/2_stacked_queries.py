number_of_lines = int(input())

queries_stack = list()          # this is a stack

for _ in range(number_of_lines):
    current_line = [int(x) for x in input().split()]

    if current_line[0] == 1:      # push the number into the stack
        queries_stack.append(current_line[1])

    elif current_line[0] == 2 and queries_stack:    # delete the number on top of the stack
        queries_stack.pop()

    elif current_line[0] == 3 and queries_stack:    # print the max number from the stack
        print(max(queries_stack))

    elif current_line[0] == 4 and queries_stack:    # print the min number from the stack
        print(min(queries_stack))

reversed_stack = list()

while queries_stack:
    reversed_stack.append(str(queries_stack.pop()))

print(", ".join(reversed_stack))
