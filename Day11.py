

move = {
    "n" : lambda x: (x[0], x[1]+2),
    "ne": lambda x: (x[0]+1, x[1]+1),
    "se": lambda x: (x[0]+1, x[1]-1),
    "s" : lambda x: (x[0], x[1]-2),
    "sw": lambda x: (x[0]-1, x[1]-1),
    "nw": lambda x: (x[0]-1, x[1]+1)
}


def distanceHex(pos1):
    distx = abs(pos1[0])
    disty = int( max([abs(pos1[1]) - distx, 0]) / 2)
    return distx+disty

if __name__ == "__main__":
    with open("input11", "r") as f:
        line = f.readline().strip()


    #line = "ne,ne,ne"
    #line = "ne,ne,sw,sw"
    #line = "ne,ne,s,s"
    #line = "se,sw,se,sw,sw"

    steps = [x for x in line.split(',')]


    pos = (0,0)
    max_distance = 0
    for step in steps:
        pos = move[step](pos)
        cur_distance = distanceHex(pos)
        max_distance = max([cur_distance, max_distance])

    print(pos)
    print(distanceHex(pos))
    print(max_distance)