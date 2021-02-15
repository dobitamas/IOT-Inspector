from UserStory4 import get_amb, get_correct, get_ill


correct_lines = get_correct()
amb_lines = get_amb()
ill_lines = get_ill()

print("CORRECT: ", correct_lines)


def write_to_file():
    print(correct_lines)
    output = open('output.txt', "w+")

    for correct in correct_lines:
        output.write(str(correct) + "\r\n")

    for amb in amb_lines:
        output.write(amb + "\r\n")

    for ill in ill_lines:
        output.write(ill + "\r\n")


write_to_file()
