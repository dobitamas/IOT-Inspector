import UserStory2
import UserStory1
import Characters


def check_if_valid(number):
    if UserStory2.checksum(number):
        return True
    return False


def check_number_for_illegal_digit(number):
    for char in number:
        if isinstance(char, list):
            return True

    return False


def check_number_for_character(number):
    for char in number:
        if char in Characters.hex_values:
            return True
    return False


def fix_illegal_digit(number):
    new_number = number
    for i in range(len(number)):
        if isinstance(number[i], list):
            similars = Characters.find_similars(number[i])
            new_number[i] = similars
    return new_number


def check_all_numbers():
    numbers = UserStory1.get_numbers()
    lines = numbers
    for i in range(len(numbers)):
        if check_number_for_illegal_digit(numbers[i]):
            lines[i] = fix_illegal_digit(numbers[i])

    return lines
