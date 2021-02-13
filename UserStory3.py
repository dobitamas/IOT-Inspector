import UserStory2
import UserStory1


def check_number_for_error(number):
    if "ERROR" in number:
        return True

    return False


def check_if_valid(number):
    if UserStory2.checksum(number):
        return True
    return False


def replace_error(number):
    for i in range(len(number)):
        if number[i] == "ERROR":
            number[i] = "?"

    return number


def check_number(number):
    if check_number_for_error(number):
        number = replace_error(number)
        return ''.join(number) + " ILL"

    if check_if_valid(number):
        return ''.join(number)

    return ''.join(number) + " ERR"


def check_all_numbers():
    numbers = UserStory1.get_numbers()
    lines = []
    for number in numbers:
        lines.append(check_number(number))

    return lines


def write_to_file():
    lines = check_all_numbers()
    output = open('output.txt', "a+")

    for line in lines:
        output.write(line + "\r\n")


write_to_file()
