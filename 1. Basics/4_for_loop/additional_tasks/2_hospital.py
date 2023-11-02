time_period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, time_period + 1):
    current_day_patients = int(input())

# Every 3rd day a new doctor is added if untreated > treated patients

    if day % 3 == 0 and untreated_patients > treated_patients:
            doctors += 1

    if doctors >= current_day_patients:
        treated_patients += current_day_patients

    else:
        treated_patients += doctors     # I use variable doctors because it shows the amount of treated patients
        untreated_patients += current_day_patients - doctors

print(f'Treated patients: {treated_patients}')
print(f'Untreated patients: {untreated_patients}')
