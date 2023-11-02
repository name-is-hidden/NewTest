def words_sorting(*args):
    def ascii_sum(word):
        return sum(ord(x) for x in word)

    result = {word: ascii_sum(word) for word in args}

    sum_of_values = sum(result.values())

    if sum_of_values % 2 == 0:
        sorted_result = [f"{key} - {value}" for key, value in sorted(result.items(), key=lambda x: x[0])]

        return "\n".join(sorted_result)
    else:
        sorted_result = [f"{key} - {value}" for key, value in sorted(result.items(), key=lambda x: -x[1])]

        return "\n".join(sorted_result)
