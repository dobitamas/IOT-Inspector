import Characters


def read_all_lines():
    return open('input.txt').readlines()


def split_lines_to_entries():
    lines = read_all_lines()
    entries = []

    for i in range(0, len(lines), 4):
        entries.append(lines[i: i+4])

    return entries


def read_entries():
    numbers = []

    entries = split_lines_to_entries()

    for entry in entries:
        entry_number = []
        for index in range(0, 27, 3):
            number = [entry[0][index:index+3],
                      entry[1][index:index+3],
                      entry[2][index:index+3]]
            entry_number.append(Characters.get_str_from_digit(number))
        numbers.append(entry_number)

    return numbers


numbers = read_entries()
print(numbers)
