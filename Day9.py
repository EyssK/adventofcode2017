

lines_test = list()
lines_test.append("{{<a!>},{<a!>},{<a!>},{<ab>}}")
lines_test.append("{{<!!>},{<!!>},{<!!>},{<!!>}}")
lines_test.append("{{<ab>},{<ab>},{<ab>},{<ab>}}")
lines_test.append("{<a>,<a>,<a>,<a>}")
lines_test.append("{{{},{},{{}}}}")
lines_test.append("{{},{}}")
lines_test.append("{{{}}}")
lines_test.append("<{o\"i!a,<{i<a>")
lines_test.append("<!!!>>")
lines_test.append("<!!>")
lines_test.append("<{!>}>")
lines_test.append("<<<<>")
lines_test.append("<random characters>")



if __name__ == "__main__":
    lines = list()
    with open("input9", "r") as f:
        for line in f:
            lines.append(line[:-1])

    # test
    # lines = lines_test

    for line in lines:
        in_garbage = False
        cancelled_char = False
        depth = 0
        score = 0
        garbage_score = 0
        for char in line:
            if not in_garbage and char == '<':
                in_garbage = True
            elif not in_garbage and char == '{':
                depth += 1
            elif not in_garbage and char == '}':
                score += depth
                depth -= 1
            elif in_garbage and not cancelled_char and char == '!':
                cancelled_char = True
            elif in_garbage and not cancelled_char and char == '>':
                in_garbage = False
            elif in_garbage and cancelled_char:
                cancelled_char = False
            elif in_garbage:
                garbage_score += 1
            # print(char,~ depth, score, in_garbage, cancelled_char)
        if line in lines_test:
            print(line, score, garbage_score)
        else:
            print(score, garbage_score)
