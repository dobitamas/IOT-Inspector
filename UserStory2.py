def checksum(numbers):
    numbers = [int(d) for d in numbers]
    sum = 0

    for index, number in enumerate(numbers):
        sum += number * (9 - index)

    if sum % 11 == 0:
        return True
    else:
        return False

