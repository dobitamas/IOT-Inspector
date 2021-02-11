import UserStory3
import UserStory2


def fix_error(line):
    number = str(line.split(' ')[0])

    for digit_index in range(len(number)):
        new_number = number
        for counter in range(9):
            new_number = list(new_number)
            new_number[digit_index] = str(counter)
            if UserStory2.checksum(new_number):

                return new_number

    return None


def fix_ill(line):
    number = str(line.split(' ')[0])

    for digit_index in range(len(number)):
        new_number = number

        if number[digit_index] == "?":
            for counter in range(9):
                new_number = list(new_number)
                new_number[digit_index] = str(counter)
                if UserStory2.checksum(new_number):

                    return new_number

    return None


def fix_numbers():
    lines = UserStory3.check_all_numbers()

    faulty_numbers = []

    for line in lines:
        if 'ERR' in line or 'ILL' in line:
            faulty_numbers.append(line)

    for i in range(len(faulty_numbers)):
        if 'ERR' in faulty_numbers[i]:
            result = fix_error(faulty_numbers[i])
            if result is not None:
                faulty_numbers[i] = ''.join(result)

        if 'ILL' in faulty_numbers[i]:
            result = fix_ill(faulty_numbers[i])

            if result is not None:
                faulty_numbers[i] = ''.join(result)

    faulty_index = 0
    for index in range(len(lines)):
        if 'ERR' in lines[index] or 'ILL' in lines[index]:
            lines[index] = faulty_numbers[faulty_index]
            faulty_index += 1

    return lines


fix_numbers()
