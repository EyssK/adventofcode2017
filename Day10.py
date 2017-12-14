from itertools import cycle
from functools import reduce


def computeSparseHash(inputs, seq, iter):
    cur_pos = 0
    skip = 0
    res_len = len(seq)

    for idx, length in  enumerate(cycle(inputs)):
        if idx / len(inputs) >= iter:
            break
        pinchAndTwist(seq, cur_pos, length)
        cur_pos = (cur_pos + length + skip) % res_len
        skip += 1


def pinchAndTwist(in_list, cur_pos, length):
    sub_list = list()
    for idx, value in enumerate(cycle(in_list)):
        if idx < cur_pos:
            continue
        if idx >= cur_pos + length:
            break
        sub_list.append(value)
    sub_list.reverse()

    nex_list_idx = 0
    for idx, value in enumerate(cycle(in_list)):
        if idx < cur_pos:
            continue
        if idx >= cur_pos + length:
            break
        in_list[idx % len(in_list)] = sub_list[nex_list_idx]
        nex_list_idx += 1


def knotHash(line):
    inputs = list()
    for char in line:
        inputs.append(ord(char))
    inputs += [17, 31, 73, 47, 23]

    sparse_hash = [x for x in range(256)]
    computeSparseHash(inputs, sparse_hash, 64)

    dense_hash = list()
    for group in range(16):
        dense_hash.append(reduce(lambda x, y: x ^ y, sparse_hash[group*16:(group+1)*16]))

    khash = ""
    for val in dense_hash:
        khash += hex(val)[2:]
    return khash


if __name__ == "__main__":
    lines = list()
    with open("input10", "r") as f:
        for line in f:
            lines.append(line[:-1])

    inputs = [int(x) for x in lines[0].split(',')]

    # test
    # res_list = [0, 1, 2, 3, 4]
    # inputs = [3, 4, 1, 5]
    res_list = [x for x in range(256)]
    computeSparseHash(inputs, res_list, 1)
    print(res_list[0] * res_list[1])

    # Part 2

    # test
    # lines[0] = ""
    # lines[0] = "AoC 2017"
    # lines[0] = "1,2,3"
    # lines[0] = "1,2,4"

    khash = knotHash(lines[0])
    print(hash)