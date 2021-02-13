import Characters


def checksum(numbers):
    sum = 0

    for index, number in enumerate(numbers):
        if isinstance(number, str):
            number = Characters.get_number_from_hex(number)

        print(number)
        sum += number * (9 - index)

    if sum % 11 == 0:
        return True
    else:
        return False


