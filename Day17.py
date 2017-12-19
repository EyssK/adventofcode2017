

def insert(list_in, var, pos):
    return list_in[:pos] + [var] + list_in[pos:]


def part1(puzzle_in):
    full_list = [0]
    curpos = 0

    i = 1
    while i < 2018:
        full_list = insert(full_list, i, curpos+1)
        curpos = (curpos + 1 + puzzle_in) % (i + 1)
        i += 1
    return full_list

# does not scale with 50_000_000
def part2(puzzle_in):
    # We just need to find if something is inserted in front of 0
    curpos = 0
    pos_of_zero = 0
    current_next_zero = 1
    i = 1
    while i < 50*10**6+1:
        if curpos == pos_of_zero:
            current_next_zero = i
        elif curpos < pos_of_zero:
            pos_of_zero += 1
        curpos = (curpos + 1 + puzzle_in) % (i + 1)
        i += 1
    return current_next_zero


if __name__ == "__main__":
    puzzle_input = 324

    #test
    # puzzle_input = 3

    full_list = part1(puzzle_input)
    idx_2017 = full_list.index(2017)
    print(full_list[idx_2017 - 2:idx_2017 + 3])
    print("ResPart1 = ", full_list[idx_2017+1])


    val_after_zero_2 = part2(puzzle_input)
    print("ResPart2 = ", val_after_zero_2)
