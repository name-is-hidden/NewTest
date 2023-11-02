def sorting_cheeses(**kwargs):
    cheeses_sorted = sorted(
        kwargs.items(),
        key=lambda x: (-len(x[1]), x[0])
    )

    result = list()

    for key, values in cheeses_sorted:
        result.append(key)
        result.extend(
            sorted(values, reverse=True)
        )

    return "\n".join([str(x) for x in result])
