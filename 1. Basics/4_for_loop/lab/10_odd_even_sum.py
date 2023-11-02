number = int(input())

odd_sum = 0
even_sum = 0

for numbers in range(number):
    current_number = int(input())

    if numbers % 2 == 0:
        even_sum += current_number

    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")

else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")
