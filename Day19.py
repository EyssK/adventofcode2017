
def go_vert(lines, idx, start_line):
    # find direction up or down
    if start_line != 0:
        if lines[start_line - 1][idx] != ' ':
            direction = 'u'
            cur_line = start_line - 1
        else:
            direction = 'd'
            cur_line = start_line + 1
    else:
        direction = 'd'
        cur_line = start_line + 1

    letters_crossed = ""

    while lines[cur_line][idx] != '+':
        if lines[cur_line][idx] == ' ':
            break
        if lines[cur_line][idx].isalpha():
            letters_crossed += lines[cur_line][idx]
        if direction == 'u':
            if cur_line - 1 < 0:
                break
            else:
                cur_line -= 1
        else:
            if cur_line + 1 == len(lines):
                break
            else:
                cur_line += 1

    return (cur_line, letters_crossed)


def go_horiz(lines, line, start_idx):
    # find direction left or right
    if start_idx != 0:
        if lines[line][start_idx - 1] != ' ':
            direction = 'l'
            cur_idx = start_idx - 1
        else:
            direction = 'r'
            cur_idx = start_idx + 1
    else:
        direction = 'r'
        cur_idx = start_idx + 1

    letters_crossed = ""
    last_path = False

    while lines[line][cur_idx] != '+':
        if lines[line][cur_idx] == ' ':
            break
        if lines[line][cur_idx].isalpha():
            letters_crossed += lines[line][cur_idx]
        if direction == 'l':
            if cur_idx - 1 < 0:
                break
            else:
                cur_idx -= 1
        else:
            if cur_idx + 1 == len(lines[line]):
                break
            else:
                cur_idx += 1

    return (cur_idx, letters_crossed)


def go_through(lines, idx, line_idx, vertical):
    if vertical == True:
        cur_line, letters_crossed = go_vert(lines, idx, line_idx)
        return (idx, cur_line, letters_crossed)
    else:
        cur_idx, letters_crossed = go_horiz(lines, line_idx, idx)
        return (cur_idx, line_idx, letters_crossed)


if __name__ == "__main__":
    lines = list()
    with open("input19", "r") as f:
        for line in f:
            lines.append(line[:-1])

    list_test = list()
    list_test.append("     |          ")
    list_test.append("     |  +--+    ")
    list_test.append("     A  |  C    ")
    list_test.append(" F---|----E|--+ ")
    list_test.append("     |  |  |  D ")
    list_test.append("     +B-+  +--+ ")
    #lines = list_test

    #for line in lines:
    #    print(line)

    start_idx = lines[0].index('|')
    cur_idx = start_idx
    cur_line = 0
    letters = ""
    vertical = True
    distance_traveled = 1

    while True:
        new_idx, new_line, letters_crossed = go_through(lines, cur_idx, cur_line, vertical)
        vertical = ~vertical

        distance_traveled += abs(new_idx - cur_idx) + abs(new_line - cur_line)
        cur_idx, cur_line = new_idx, new_line

        if lines[cur_line][cur_idx] == ' ':
            distance_traveled -= 1
            letters += letters_crossed
            break
        else:
            letters += letters_crossed
    print(letters, distance_traveled)

