def even_odd_filter(**kwargs):
    result = dict()

    for key, values in kwargs.items():
        parity = 0 if key == "even" else 1
        filtered = [x for x in values if x % 2 == parity]
        result[key] = filtered

    return dict(sorted(result.items(), key=lambda x: -len(x[1])))
