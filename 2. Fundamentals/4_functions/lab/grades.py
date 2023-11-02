def read_grade():
    grade = float(input())

    if grade < 3:
        return "Fail"

    elif grade < 3.5:
        return "Poor"

    elif grade < 4.5:
        return "Good"

    elif grade < 5.5:
        return "Very Good"

    else:
        return "Excellent"


print(read_grade())
