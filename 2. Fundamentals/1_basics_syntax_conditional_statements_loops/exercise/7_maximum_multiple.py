divisor = int(input())
boundary = int(input())

maximum_multiple = 0

# The maximum_multiple is:
#   divisible by the given divisor
#   less than or equal to the given bound
#   greater than 0


if boundary % divisor == 0:
    maximum_multiple = boundary

else:
    maximum_multiple = (boundary // divisor) * divisor
    # We use // dividing to find how many times the divisor goes in the boundary and then
    # multiply the result to the divisor to fond the maximum_multiple

print(maximum_multiple)
