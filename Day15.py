
# Generator A starts with 277
# Generator B starts with 349

def generatorA(prev):
    return prev * 16807 % 2147483647

def generatorB(prev):
    return prev * 48271 % 2147483647

def generatorA2(prev):
    while True:
        prev = prev * 16807 % 2147483647
        if not prev & 3:
            return prev

def generatorB2(prev):
    while True:
        prev = prev * 48271 % 2147483647
        if not prev & 7:
            return prev


if __name__ == "__main__":
    valA = 277
    valB = 349
    count = 0
    for round in range(40*10**6):
        if not round % 10**6 and round:
            print(int(round/(10**6)))
        valA = generatorA(valA)
        valB = generatorB(valB)
        if valA & 0xFFFF == valB & 0xFFFF:
            count += 1
    print("Part1:",count)

    #part2
    valA = 277
    valB = 349
    count = 0
    for round in range(5*10**6):
        if not round % 10**6 and round:
            print(int(round/(10**6)))
        valA = generatorA2(valA)
        valB = generatorB2(valB)
        if valA & 0xFFFF == valB & 0xFFFF:
            count += 1

    print("Part2:",count)
