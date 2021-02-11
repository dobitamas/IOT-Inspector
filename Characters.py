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
    "9": nine
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


print(get_str_from_digit(nine))

print(get_digit_from_str("2"))
