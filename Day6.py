

def redistribution(banks):
    new_banks = list(banks)
    max_bank_val = max(banks)
    max_bank_idx = banks.index(max_bank_val)

    new_banks[max_bank_idx] = 0
    max_bank_idx = (max_bank_idx + 1) % len(banks)
    while max_bank_val > 0:
        new_banks[max_bank_idx] += 1
        max_bank_val -= 1
        max_bank_idx = (max_bank_idx + 1) % len(banks)

    return new_banks


if __name__ == "__main__":
    lines = list()
    with open("input6", "r") as f:
        for line in f:
            lines.append(line[:-1])

    banks = [int(x) for x in lines[0].split('\t')]
    banks_configurations = list()

    # example
    #banks = [0,2,7,0]

    cycle_nb = 0
    while banks not in banks_configurations:
        # print(banks)
        banks_configurations.append(banks)

        # redistribution
        banks = redistribution(banks)
        cycle_nb += 1
    print("Part1: ", cycle_nb)

    print("Part2: ",len(banks_configurations) - banks_configurations.index(banks))


