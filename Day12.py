

lines_test = list()
lines_test.append("0 <-> 2")
lines_test.append("1 <-> 1")
lines_test.append("2 <-> 0, 3, 4")
lines_test.append("3 <-> 2, 4")
lines_test.append("4 <-> 2, 3, 6")
lines_test.append("5 <-> 6")
lines_test.append("6 <-> 4, 5")


def get_group_from_graph(graph, start):
    node_in_group = list()
    remaining = graph[start]
    while len(remaining):
        if remaining[0] in node_in_group:
            remaining.remove(remaining[0])
        else:
            node_in_group.append(remaining[0])
            remaining += graph[remaining[0]]
            remaining.remove(remaining[0])
    return node_in_group


if __name__ == "__main__":
    lines = list()
    with open("input12", "r") as f:
        for line in f:
            lines.append(line[:-1])

    #lines = lines_test

    # build graph
    graph = dict()
    for line in lines:
        name, neighbors = line.split(' <-> ')
        graph[name] = [ x.strip(',') for x in neighbors.split()]

    # cross graph from 0
    already_crossed = get_group_from_graph(graph, '0')
    print(len(already_crossed))

    # find all groups
    group_nb = 1
    for node in graph:
        if node not in already_crossed:
            already_crossed += get_group_from_graph(graph, node)
            group_nb += 1
    print(group_nb)
