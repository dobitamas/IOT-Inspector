import UserStory3


def fix_numbers():
    lines = UserStory3.check_all_numbers()

    faulty_numbers = []

    for line in lines:
        if 'ERR' in line or 'ILL' in line:
            faulty_numbers.append(line)

    print(faulty_numbers)


fix_numbers()
