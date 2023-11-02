factor = int(input())
count = int(input())

multiples_list = list()

for number in range(1, count + 1):

    multiples_list.append(abs(number * factor))          # The numbers should be only positive

if len(multiples_list) == count:                  # The len() of the list must be equal to the given count
    print(sorted(multiples_list))                 # The list must be in ascending order
