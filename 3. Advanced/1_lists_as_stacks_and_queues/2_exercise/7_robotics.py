from collections import deque


def read_robots():
    result = dict()
    input_robots = input().split(";")

    for robot in input_robots:
        details = robot.split("-")

        name = details[0]
        processing_time = int(details[1])

        result[name] = processing_time

    return result


robots = read_robots()

available_robots = [r for r in robots.keys()]

processing_robots = dict()

starting_time_parts = [int(x) for x in input().split(":")]


def to_seconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds            # 3600 are the seconds in 1 hour


time_in_seconds = to_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])


def read_products():
    result = deque()

    while True:
        line = input()
        if line == "End":
            break

        else:
            result.append(line)

    return result


def to_str_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 3600)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()

    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_product} [{to_str_time(time_in_seconds)}]")
            processing_robots[robot_name] = robots[robot_name]
            break

    else:
        products.append(current_product)
