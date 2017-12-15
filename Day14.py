from Day10 import knotHash
from itertools import product


TABLE_SIZE = 128

input = 'xlqgujun'

# test
# input = 'flqrgnkx'


def get_neighbors(coord):
    neighbors_list = list()
    if coord[0] > 0:
        neighbors_list.append((coord[0]-1, coord[1]))
    if coord[0] < (TABLE_SIZE - 1):
        neighbors_list.append((coord[0]+1, coord[1]))
    if coord[1] > 0:
        neighbors_list.append((coord[0], coord[1]-1))
    if coord[1] < (TABLE_SIZE - 1):
        neighbors_list.append((coord[0], coord[1]+1))
    return neighbors_list


def check_neighbors(table, coord):
    """ return list of neighbors in the group """
    neighbors_in_list = list()
    for neighbor in get_neighbors(coord):
        if table[neighbor[0]][neighbor[1]]:
            neighbors_in_list.append(neighbor)
    return neighbors_in_list

if __name__ == "__main__":

    defrag_list = list()
    defrag_table = [[0 for x in range(128)] for y in range(128)]
    for row in range(128):
        khash = knotHash(input + "-" + str(row))
        defrag_list.append(khash)
        khash_val = int(khash, 16)
        for col in range(128):
            defrag_table[col][row] = (khash_val & (1 << col)) >> col

    total_nb_of_region = sum(map(sum, defrag_table))
    print('part1: ', total_nb_of_region)

    # part 2
    # build group lists
    groups_list = list()
    group_nb = 0
    for col, row in product(range(TABLE_SIZE), range(TABLE_SIZE)):
        if (col, row) in groups_list:
            # this coord already in a group
            continue
        if defrag_table[col][row]:
            # explore new group
            group_nb += 1
            remain = [(col,row)]
            while len(remain):
                if remain[0] in groups_list:
                    # his neighbors had already been checked
                    remain = remain[1:]
                else:
                    remain += check_neighbors(defrag_table, remain[0])
                    groups_list.append(remain[0])
                    remain = remain[1:]

        else:
            # defrag_table = 0
            continue

    print("part2: ", group_nb)
