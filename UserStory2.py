
import Characters


def parse_to_int_list(numbers):
    return_list = []
    for number in numbers:
        if number not in Characters.hex_values:
            return_list.append(int(number))
        else:
            return_list.append(number)

    return return_list


def checksum(numbers):
    sum = 0
    numbers = parse_to_int_list(numbers)
    for index, number in enumerate(numbers):

        if isinstance(number, str):
            hex_number = Characters.get_number_from_hex(number)
            if hex_number is not None:
                number = hex_number
                sum += number * (9 - index)
        else:
            sum += number * (9 - index)

    if sum % 11 == 0:
        return True
    else:
        return False


def try_user_story2():
    number1 = ['8', '8', 'A', '8', '8', '8', '8', '8', '8']
    number2 = ['8', '8', '8', '8', '8', '6', '8', '8', '8']
    number3 = ['8', '8', '8', '8', '8', '8', '8', '8', '0']

    print("----------------------------")
    print("NUMBER: ", number1)
    print("RESULT IS: ", checksum(number1))
    print("----------------------------")
    print("----------------------------")
    print("NUMBER: ", number2)
    print("RESULT IS: ", checksum(number2))
    print("----------------------------")
    print("----------------------------")
    print("NUMBER: ", number3)
    print("RESULT IS: ", checksum(number3))
    print("----------------------------")


try_user_story2()
