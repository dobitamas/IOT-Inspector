from UserStory4 import run_fix_lines


def write_to_file():
    lines = run_fix_lines()
    correct_lines = lines[0]
    amb_lines = lines[1]
    ill_lines = lines[2]

    output = open('output.txt', "w+")

    for correct in correct_lines:
        output.write(str(correct) + "\r\n")

    for amb in amb_lines:
        output.write(amb + "\r\n")

    for ill in ill_lines:
        output.write(ill + "\r\n")


write_to_file()
