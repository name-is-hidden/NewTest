def sorted_numbers(numbers):
    sorted_numbers_list = list()

    for i in numbers:
        sorted_numbers_list.append(i)

    print(sorted(sorted_numbers_list))


input_numbers = list(map(int, input().split()))

sorted_numbers(input_numbers)
