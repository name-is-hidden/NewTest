movie_name = input()

kid_ticket = 0              # The following 4 variables will be reset in the nested loop
student_ticket = 0
standard_ticket = 0
tickets = 0

total_tickets = 0               # This will not be reset

kids = 0                        # These variables will keep count of the targets through every iteration
students = 0
standards = 0
movie_hall_percentage = 0

while movie_name != "Finish":
    free_seats = int(input())
    seats = free_seats              # This decreases with every input and ends the nested loop

    while seats:
        ticket_type = input()

        if ticket_type == "kid":
            seats -= 1
            kid_ticket += 1
            kids += 1
            tickets += 1
            total_tickets += 1

        elif ticket_type == "student":
            seats -= 1
            student_ticket += 1
            students += 1
            tickets += 1
            total_tickets += 1

        elif ticket_type == "standard":
            seats -= 1
            standard_ticket += 1
            standards += 1
            tickets += 1
            total_tickets += 1

        else:
            break

        movie_hall_percentage = (tickets / free_seats) * 100

    print(f"{movie_name} - {movie_hall_percentage:.2f}% full.")

    kid_ticket = 0                      # reset from here every "ticket" containing variable without the "total"
    student_ticket = 0
    standard_ticket = 0
    tickets = 0

    movie_hall_percentage = 0

    movie_name = input()

kids_percentage = (kids / total_tickets) * 100
students_percentage = (students / total_tickets) * 100
standard_percentage = (standards / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{students_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")

# this problem required 2 variables of each target due the need of reset at the end of the second loop
