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
            entry_number.append(Characters.get_str_from_digit(number))
        numbers.append(entry_number)

    return numbers


def try_user_story1(name_of_input_file="input.txt"):
    original_lines = read_from_file(name_of_input_file)
    entries = split_lines_to_entries(original_lines)
    numbers = read_entries(entries)

    for number in numbers:
        Characters.print_numbers_in_digit(number)


try_user_story1()
