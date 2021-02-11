import Characters


def read_from_file():
    input_file = open('input.txt')
    lines = input_file.readlines()
    return lines


def split_lines():
    numbers = []

    lines = read_from_file()

    for index in range(0, 27, 3):
        number = [lines[0][index:index+3],
                  lines[1][index:index+3],
                  lines[2][index:index+3]]
        numbers.append(Characters.get_str_from_digit(number))

    return numbers


numbers = split_lines()

print(numbers)
