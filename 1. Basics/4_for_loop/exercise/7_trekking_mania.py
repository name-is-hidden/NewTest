trekking_groups = int(input())

total_people = 0

people_musala = 0
people_montblanc = 0
people_kilimandjaro = 0
people_k2 = 0
people_everest = 0

for groups in range(trekking_groups):
    people_in_group = int(input())

    if people_in_group <= 5:
        people_musala += people_in_group

    elif 5 < people_in_group <= 12:
        people_montblanc += people_in_group

    elif 12 < people_in_group <= 25:
        people_kilimandjaro += people_in_group

    elif 25 < people_in_group <= 40:
        people_k2 += people_in_group

    elif people_in_group > 40:
        people_everest += people_in_group

    total_people = people_musala + people_montblanc + people_kilimandjaro + people_k2 + people_everest

percent_musala = people_musala / total_people * 100

percent_montblanc = people_montblanc / total_people * 100

percent_kilimandjaro = people_kilimandjaro / total_people * 100

percent_k2 = people_k2 / total_people * 100

percent_everest = people_everest / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_montblanc:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
