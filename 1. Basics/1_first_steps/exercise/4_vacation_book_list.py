# Write a program that calculates the amount of pages the person must read every day:

book = int(input())
pages_per_hour = int(input())
days_count = int(input())

reading_time = book / pages_per_hour            # Calculate the reading time per book

days_to_read = reading_time // days_count       # Calculate the time for all books per day

print(f"{round(days_to_read)}")
