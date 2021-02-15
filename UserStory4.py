import UserStory3
import UserStory2
import Characters
import copy

correct_lines = []
ill_lines = []
amb_lines = []


def get_correct():
    return correct_lines


def get_ill():
    return ill_lines


def get_amb():
    return amb_lines


def fix_lines(numbers):
    lines = copy.deepcopy(numbers)
    print("LINES: ", lines)
    for i in range(len(lines)):
        if UserStory3.check_number_for_illegal_digit(lines[i]):
            fix_multiple_similar(lines[i])
        elif UserStory3.check_number_for_character(lines[i]):
            temp_number = lines[i]
            # print("EZ JÖTT KARAKTERESRE: ", lines[i])
            for i in range(len(temp_number)):
                if RepresentsStr(temp_number[i]):
                    temp_number[i] = Characters.get_number_from_hex(
                        temp_number[i])
        else:
            number = lines[i]
            if UserStory2.checksum(number):
                correct_lines.append(number)
            else:
                print("EZT ADOM BE: ", number)
                fix_simple_ints(number)

    print("ILL LINES: ", ill_lines)
    print("CORRECT LINES: ", correct_lines)
    for line in amb_lines:
        print("AMB LINE: ", line)


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def RepresentsStr(s):
    try:
        str(s)
        return True
    except ValueError:
        return False


def fix_simple_ints(number):
    possible_number = []

    for i in range(len(number)):

        new_number = copy.deepcopy(number)
        if RepresentsInt(new_number[i]):
            similars = try_one_similar(
                new_number, i, Characters.get_digit_from_str(new_number[i]))

            for similar in similars:
                if similar is not None:
                    new_number[i] = Characters.get_str_from_digit(similar)
                    possible_number.append(new_number)
        elif RepresentsStr(new_number[i]):
            similars = try_one_similar(
                new_number, Characters.get_digit_from_str(new_number[i]), i)

            for similar in similars:
                if similar is not None:
                    new_number[i] = Characters.get_str_from_digit(similar)
                    possible_number.append(new_number)

    if len(possible_number) == 0:
        ill_lines.append(str(number) + " ILL")
    elif len(possible_number) == 1:
        correct_lines.append(number)
    else:
        amb_lines.append(str(number) + " AMB" + str(possible_number))


def fix_multiple_similar(number):
    new_number = copy.deepcopy(number)
    possible_numbers = []

    for i in range(len(number)):
        if isinstance(number[i], list):
            index_of_illegal = i
            similars = try_similars(number, number[i], i)

            for similar in similars:
                if similar is not None:
                    new_number[i] = Characters.get_str_from_digit(similar)
                    possible_numbers.append(new_number)

    if len(possible_numbers) == 0:
        new_number[index_of_illegal] = "?"
        ill_lines.append(str(new_number) + " ILL")
    elif len(possible_numbers) == 1:
        correct_lines.append(number)
    else:
        amb_lines.append(str(number) + " AMB" + str(possible_numbers))


def try_similars(number, similars, index):
    valid_similars = []

    for i in range(len(similars)):
        temp_number = number
        temp_number[index] = Characters.get_str_from_digit(similars[i])
        if UserStory2.checksum(temp_number):
            valid_similars.append(similars[i])

    return valid_similars


def try_one_similar(number, index, digit):

    similars = Characters.find_similars(digit)
    print(similars)
    valid_similars = []
    if similars is not None:
        for i in range(len(similars)):
            temp_number = number
            temp_number[index] = Characters.get_str_from_digit(similars[i])
            if UserStory2.checksum(temp_number):
                valid_similars.append(similars[i])

    return valid_similars


def compare_old_and_new():
    old_lines = UserStory3.check_all_numbers()
    fix_lines(old_lines)

    # for i in range(len(old_lines)):
    #   print("--------------------------")
    #  print("OLD LINE: ", old_lines[i])
    # print("                           ")
    # print("NEW LINE: ", new_lines[i])
    # print("--------------------------")


compare_old_and_new()
