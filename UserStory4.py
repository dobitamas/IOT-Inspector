import UserStory3
import UserStory2
import Characters


def check_if_possible(original_digit, new_digit):
    if new_digit in Characters.get_similars(original_digit):
        return True

    return False


def fix_error(line):
    number = str(line.split(' ')[0])

    possibilities = []

    for digit_index in range(len(number)):
        new_number = number
        for counter in range(9):
            new_number = list(new_number)
            new_number[digit_index] = str(counter)
            if UserStory2.checksum(new_number):
                if check_if_possible(number[digit_index], counter):
                    possibilities.append(new_number)

    if len(possibilities) > 1:
        return number + ' AMB -->' + str(possibilities)
    elif len(possibilities) == 1:
        return ''.join(possibilities[0])
    else:
        return str(line.split(' ')[0]) + ' ILL'


def fix_ill(line):
    number = str(line.split(' ')[0])

    possibilities = []

    for digit_index in range(len(number)):
        new_number = number

        if number[digit_index] == "?":
            for counter in range(9):
                new_number = list(new_number)
                new_number[digit_index] = str(counter)
                if UserStory2.checksum(new_number):
                    possibilities.append(new_number)

    if len(possibilities) > 1:
        return number + ' AMB -->' + str(possibilities)
    elif len(possibilities) == 1:
        return ''.join(possibilities[0])
    else:
        return line


def fix_numbers():
    lines = UserStory3.check_all_numbers()

    faulty_numbers = []

    for line in lines:
        if 'ERR' in line or 'ILL' in line:
            faulty_numbers.append(line)

    for i in range(len(faulty_numbers)):
        if 'ERR' in faulty_numbers[i]:
            faulty_numbers[i] = fix_error(faulty_numbers[i])

        if 'ILL' in faulty_numbers[i]:
            faulty_numbers[i] = fix_ill(faulty_numbers[i])

    faulty_index = 0
    for index in range(len(lines)):
        if 'ERR' in lines[index] or 'ILL' in lines[index]:
            lines[index] = faulty_numbers[faulty_index]
            faulty_index += 1

    return lines


def compare_old_and_new():
    old_lines = UserStory3.check_all_numbers()
    new_lines = fix_numbers()

    for i in range(len(old_lines)):
        print("--------------------------")
        print("OLD LINE: ", old_lines[i])
        print("                           ")
        print("NEW LINE: ", new_lines[i])
        print("--------------------------")


compare_old_and_new()
