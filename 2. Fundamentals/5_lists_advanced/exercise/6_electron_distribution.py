def electron_distribution(electrons):
    filled_shells = list()
    counter = 1
    while True:
        atom = 2 * (counter ** 2)

        if atom < electrons:
            electrons -= atom
            filled_shells.append(atom)

        else:
            filled_shells.append(electrons)
            break

        counter += 1
    print(filled_shells)


electrons_count = int(input())
electron_distribution(electrons_count)
