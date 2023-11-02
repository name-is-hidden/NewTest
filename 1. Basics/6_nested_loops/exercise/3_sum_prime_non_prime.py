command = input()
primes = 0
non_primes = 0

while command != "stop":
    is_prime = True
    current_number = int(command)

    if current_number < 0:
        print("Number is negative.")
        command = input()

        continue

    for numbers in range(2, current_number):
        if current_number % numbers == 0:
            is_prime = False

            break

    if is_prime:
        primes += current_number

    else:
        non_primes += current_number

    command = input()

print(f"Sum of all prime numbers is: {primes}")
print(f"Sum of all non prime numbers is: {non_primes}")
