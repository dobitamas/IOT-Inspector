zero = [' _ ', '| |', '|_|']
one = ['   ', '  |', '  |']
two = [' _ ', ' _|', '|_ ']
three = [' _ ', ' _|', ' _|']
four = ['   ', '|_|', '  |']
five = [' _ ', '|_ ', ' _|']
six = [' _ ', '|_ ', '|_|']
seven = [' _ ', '  |', '  |']
eight = [' _ ', '|_|', '|_|']
nine = [' _ ', '|_|', ' _|']
A = [' _ ', '|_|', '| |']
B = [' _ ', '|_\\', '|_/']
C = [' _ ', '|  ', '|_ ']
D = [' _ ', '| \\', '|_/']
E = [' _ ', '|_ ', '|_ ']
F = [' _ ', '|_ ', '|  ']


STR_and_DIGIT = {
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F
}

hex_values = ["A", "B", "C", "D", "E", "F"]

similars = {
    "0": [8],
    "1": [7],
    "2": [],
    "3": [9],
    "4": [],
    "5": [6, 9],
    "6": [5, "E"],
    "7": [1],
    "8": [0, 9, "A"],
    "9": [3, 8],
    "A": [8],
    "B": [],
    "D": [],
    "E": [6],
    "F": []
}


def get_str_from_digit(digit):
    for key, value in STR_and_DIGIT.items():
        if digit == value:
            return key

    return "ERROR"


def get_digit_from_str(number):
    for key, value in STR_and_DIGIT.items():
        if number == key:
            return value

    return "ERROR"


def get_similars(number):
    return similars[number]


def get_number_from_hex(hex):
    switcher = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    return switcher.get(hex, None)


def print_numbers_in_digit(number):
    print(''.join(number))
    printing_lines = create_digital(number)

    for line in printing_lines:
        print(line)


def create_digital(number):
    line1 = ""
    line2 = ""
    line3 = ""

    for char in number:
        line1 += get_digit_from_str(char)[0]
        line2 += get_digit_from_str(char)[1]
        line3 += get_digit_from_str(char)[2]

    return [line1, line2, line3]
