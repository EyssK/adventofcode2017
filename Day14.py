from Day10 import knotHash
import encodings

input = 'xlqgujun'

# test
# input = 'flqrgnkx'


def bitcount(n):
    count = 0
    while n > 0:
        if (n & 1 == 1): count += 1
        n >>= 1
    return count


if __name__ == "__main__":

    defrag_table = list()
    for row in range(128):
        defrag_table.append(knotHash(input + "-" + str(row)))

    sum_used = 0
    for row in defrag_table:
        sum_used += bitcount(int(row, 16))
    print('part1: ', sum_used)

    # table = dict{ row: [list of groups in this line]}
    # group = dict{ min, max: , connected: [ list of groups ]

