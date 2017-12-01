
def count_dbl_letter(string):
    dbl_number = 0
    for count, letter in enumerate(line[:-1]):
        if line[count + 1] == letter:
            dbl_number += int(letter)
    if line[0] == line[-1]:
        dbl_number += int(line[0])
    return  dbl_number


def count_dbl_letter_woff(string):
    dbl_number = 0
    off = len(string) >> 1
    for count, letter in enumerate(line):
        if line[(count + off) % (2*off)] == letter:
            dbl_number += int(letter)
    return  dbl_number


if __name__ == "__main__":

    debug = 0
    lines = list()
    if debug == 1:
        lines.append("1122")
        lines.append("1111")
        lines.append("1234")
        lines.append("91212129")
    elif debug == 2:
        lines.append("1212")
        lines.append("1221")
        lines.append("123425")
        lines.append("123123")
        lines.append("12131415")
    else:
        with open("input1", "r") as f:
            for line in f:
                lines.append(line[:-1])

    total = 0
    for line in lines:
        res = count_dbl_letter(line)
        if debug:
            print(res)
        total += res
    print("part 1 = ", total)

    total = 0
    for line in lines:
        res = count_dbl_letter_woff(line)
        if debug:
            print(res)
        total += res
    print("part 2 = ", total)