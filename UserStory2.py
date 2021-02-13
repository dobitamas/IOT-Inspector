import Characters


def checksum(numbers):
    sum = 0

    for index, number in enumerate(numbers):

        if isinstance(number, str):
            hex_number = Characters.get_number_from_hex(number)
            if hex_number is not None:
                number = int(hex_number)
                sum += number * (9 - index)
        else:
            sum += number * (9 - index)

    if sum % 11 == 0:
        return True
    else:
        return False


print("[0, 0, 0, 0, 0, 0, 0, 0, A]      ",
      checksum([0, 0, 0, 0, 0, 0, 0, 0, "A"]))
print("[0, 0, B, 0, 0, 0, 0, 0, A]      ",
      checksum([0, 0, "B", 0, 0, 0, 0, 0, "A"]))
print("[0, 0, 0, 0, 0, 0, 0, 0, A]      ",
      checksum([0, 0, 0, 0, 0, 0, 0, 0, "A"]))
