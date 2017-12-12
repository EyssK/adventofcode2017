

if __name__ == "__main__":
    lines = list()
    with open("input5", "r") as f:
        for line in f:
            lines.append(int(line[:-1]))

    instructions = list(lines)
    total_jmp = 0
    index = 0
    while index < len(instructions):
        cur_index = index;
        index += instructions[index]
        instructions[cur_index] += 1
        total_jmp += 1
    print("Part1: ", total_jmp)

    instructions = list(lines)
    total_jmp = 0
    index = 0
    while index < len(instructions):
        cur_index = index;
        index += instructions[index]
        if instructions[cur_index] >= 3:
            instructions[cur_index] -= 1
        else:
            instructions[cur_index] += 1
        total_jmp += 1
    print("Part2: ", total_jmp)

