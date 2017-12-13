

def depth_caught(depth, range, delay):
    if not (depth+delay)%(2*range-2):
        return True
    else:
        return False


def part1(lines, delay):
    severity = 0
    for line in lines:
        depth, ran = line.split(': ')
        if depth_caught(int(depth), int(ran), delay):
            severity += int(depth) * int(ran)
    return severity


def part2(lines):
    wait_time = 0
    while part1(lines, wait_time) or depth_caught(0, 5, wait_time):
        wait_time += 1
    return wait_time


if __name__ == "__main__":
    lines = list()
    with open("input13", "r") as f:
        for line in f:
            lines.append(line[:-1])


    print(part1(lines, 0))
    print(part2(lines))


