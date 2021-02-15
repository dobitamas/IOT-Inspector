import Characters


def read_from_file(input_file):
    return open(input_file).readlines()


def split_lines_to_entries(lines):

    entries = []

    for i in range(0, len(lines), 4):
        entries.append(lines[i: i+4])

    return entries


def read_entries(entries):
    numbers = []

    for entry in entries:
        entry_number = []
        for index in range(0, 27, 3):
            number = [entry[0][index:index+3],
                      entry[1][index:index+3],
                      entry[2][index:index+3]]
            new_entry_number = Characters.get_str_from_digit(number)
            if new_entry_number is None:
                entry_number.append(number)
            else:
                entry_number.append(new_entry_number)
        numbers.append(entry_number)

    return numbers


def get_numbers():
    original_lines = read_from_file("input.txt")
    entries = split_lines_to_entries(original_lines)
    return read_entries(entries)
