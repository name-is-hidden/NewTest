# Write a program that calculates the volume of the pool, when the employee comes back.

pool_volume = int(input())
first_pipe = int(input())
second_pipe = int(input())
time_missing = float(input())

first_pipe_volume = first_pipe * time_missing

second_pipe_volume = second_pipe * time_missing

total = first_pipe_volume + second_pipe_volume

total_percentage = (total / pool_volume) * 100      # The total volume in percents

first_pipe_percentage = (first_pipe_volume / total) * 100

second_pipe_percentage = (second_pipe_volume / total) * 100

if pool_volume >= total:
    space_left = pool_volume - total
    print(f"The pool is {total_percentage:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. Pipe 2: {second_pipe_percentage:.2f}%")

else:
    overflow = total - pool_volume
    print(f"For {time_missing:.2f} hours the pool overflows with {overflow:.2f} liters.")
