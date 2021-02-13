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
            print("INSTANCE OF STR", number)
            hex_number = Characters.get_number_from_hex(number)
            if hex_number is not None:
                number = hex_number
                sum += number * (9 - index)
            elif hex_number is None:
                print("HEX NUMBER IS NONE", hex_number)
        else:
            print("NOT STR: ", number)
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
print("[0, 0, 0, 0, A, 0, 0, 9, 1]      ",
      checksum([0, 0, 0, 0, "A", 0, 0, 9, 1]))
print("HERE COMES INTERESTING:------------------")
print("[4, 9, 0, 8, 6, 7, 7, 1, 3]      ",
      checksum([0, 9, 0, 8, 6, 7, 7, 1, 3]))
print("HERE ENDS INTERESTING:-------------------")
print("[0, 0, 0, 0, 0, 0, 0, 5, 1]      ",
      checksum([0, 0, 0, 0, 0, 0, 0, 5, 1]))
