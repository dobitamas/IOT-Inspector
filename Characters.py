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
    "9": [3, 8]
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
        "A": 11,
        "B": 12,
        "C": 13,
        "D": 14,
        "E": 15,
        "F": 16
    }
    return switcher.get(hex, "None")
