from tools import read_input
from itertools import permutations


if __name__ == '__main__':
    lines = list()
    lines.append("5\t1\t9\t5")
    lines.append("7\t5\t3")
    lines.append("2\t4\t6\t8")

    lines = read_input(2)

    checksum = 0
    res = list()
    for line in lines:
        elem = [int(e) for e in line.split('\t')]
        for e in permutations(elem, 2):
            if (e[0] % e[1]) == 0:
                res.append(int(e[0]/e[1]))


    checksum += max(elem) - min(elem)
    print('part 1:', checksum)
    print (len(res),sum(res),res)
    print('part 2:', sum(res))