numbers_string = input().split()        # this is a stack

while numbers_string:
    last_element = numbers_string.pop()     # this is the last element in the stack ([-1])

    print(last_element, end=" ")
