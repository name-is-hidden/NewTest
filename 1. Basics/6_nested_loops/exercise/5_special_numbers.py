input_number = int(input())

current_string = ""
counter = 0
special_number = ""

for number in range(1111, 10000):
    number_as_string = str(number)

    for i in number_as_string:
        if i != "0" and input_number % int(i) == 0:
            current_string += i
            counter += 1

            if counter == 4 and current_string == number_as_string:
                special_number += current_string + " "

                current_string = ""
                counter = 0

        else:
            current_string = ""
            counter = 0

print(special_number)
