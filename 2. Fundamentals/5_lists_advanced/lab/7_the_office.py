happiness_indicators = list(map(int, input().split()))
happiness_factor = int(input())

happy_employees = list(
    filter(lambda emp: emp >= sum(happiness_indicators) / len(happiness_indicators), happiness_indicators)
    )

if len(happy_employees) >= len(happiness_indicators) / 2:
    print(f"Score: {len(happy_employees)}/{len(happiness_indicators)}. Employees are happy!")

else:
    print(f"Score: {len(happy_employees)}/{len(happiness_indicators)}. Employees are not happy!")
