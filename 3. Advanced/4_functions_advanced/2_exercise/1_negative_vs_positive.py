def negative_vs_positive(*args):
    positive_sum = 0
    negative_sum = 0

    for number in args:
        if number > 0:
            positive_sum += number

        else:
            negative_sum += number

    return positive_sum, negative_sum


input_numbers = [int(x) for x in input().split()]

positive, negative = negative_vs_positive(*input_numbers)

print(negative)
print(positive)

if positive > abs(negative):
    print("The positives are stronger than the negatives")

else:
    print("The negatives are stronger than the positives")
