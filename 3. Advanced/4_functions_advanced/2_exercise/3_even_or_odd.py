def even_odd(*args):
    ending = args[-1]
    evens = list()
    odds = list()

    for number in range(len(args) - 1):
        if int(args[number]) % 2 == 0:
            evens.append(args[number])

        else:
            odds.append(args[number])

    if ending == "even":
        return evens

    else:
        return odds

