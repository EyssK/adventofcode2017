

conditions = {
    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y
}

actions = {
    "inc": lambda x, y: x + y,
    "dec": lambda x, y: x - y,
}

lines_test = list()
lines_test.append("b inc 5 if a > 1")
lines_test.append("a inc 1 if b < 5")
lines_test.append("c dec -10 if a >= 1")
lines_test.append("c inc -20 if c == 10")

if __name__ == "__main__":
    lines = list()
    with open("input8", "r") as f:
        for line in f:
            lines.append(line[:-1])

    # test
    # lines = lines_test

    registers = dict()
    local_max_val = 0
    for line in lines:
        reg, action, val, _, reg_cond, cond, val_cond = line.strip().split(' ')
        val_cond = int(val_cond)
        val = int(val)
        # init registers at 0 if not existing
        registers[reg] = registers.get(reg, 0)
        registers[reg_cond] = registers.get(reg_cond, 0)
        if conditions[cond](registers[reg_cond], val_cond):
            registers[reg] = actions[action](registers[reg], val)
        cur_max_key = max(registers, key=registers.get)
        if registers[cur_max_key] > local_max_val:
            local_max_val = registers[cur_max_key]
            print("Local: ", cur_max_key, local_max_val)


    max_key = max(registers, key=registers.get)
    print(max_key, registers[max_key])
