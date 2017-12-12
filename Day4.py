import itertools


if __name__ == "__main__":
    lines = list()
    with open("input4", "r") as f:
        for line in f:
            lines.append(line[:-1])
    total = 0
    for line in lines:
        # no duplicates in a set
        if len(line.split(' ')) == len(set(line.split(' '))):
            total += 1
    print("Part1: ", total)

    total = 0
    for line in lines:
        word_list = line.split(' ')
        if len(word_list) == len(set(word_list)):
            # take combinations of 2 words in the line
            for (word1, word2) in itertools.combinations(word_list, 2):
                # sorted gives away anagrams
                if sorted(word1) == sorted(word2):
                    break
            else:
                total += 1
    print("Part2: ", total)
