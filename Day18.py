

# part1
def step(regs, cmd, args, freq):
    pc_diff = 1
    args = args.split()

    if len(args) > 1:
        try:
            args[1] = int(args[1])
        except ValueError:
            args[1] = regs[args[1]]

    if cmd == "set":
        regs[args[0]] = args[1]
    elif cmd == "add":
        regs[args[0]] += args[1]
    elif cmd == "mul":
        regs[args[0]] *= args[1]
    elif cmd == "mod":
        regs[args[0]] %= args[1]
    elif cmd == "snd":
        try:
            args[0] = int(args[0])
        except ValueError:
            args[0] = regs[args[0]]
        freq.append(args[0])
    elif cmd == "rcv":
        if regs[args[0]] != 0:
            # break equivalent
            pc_diff = 10000
    elif cmd == "jgz":
        try:
            args[0] = int(args[0])
        except ValueError:
            args[0] = regs[args[0]]
        pc_diff = args[1] if args[0] > 0 else 1
    return pc_diff


# for part2
def step2(regs, cmd, args, freqin, freqout):
    pc_diff = 1
    args = args.split()
    if len(args) > 1:
        try:
            args[1] = int(args[1])
        except ValueError:
            args[1] = regs[args[1]]

    if cmd == "set":
        regs[args[0]] = args[1]
    elif cmd == "add":
        regs[args[0]] += args[1]
    elif cmd == "mul":
        regs[args[0]] *= args[1]
    elif cmd == "mod":
        regs[args[0]] %= args[1]
    elif cmd == "snd":
        try:
            args[0] = int(args[0])
        except ValueError:
            args[0] = regs[args[0]]
        freqout.append(args[0])
    elif cmd == "rcv":
        try:
            regs[args[0]] = freqin.pop(0)
        except IndexError:
            # nothing to pop -> wait here
            pc_diff = 0
    elif cmd == "jgz":
        try:
            args[0] = int(args[0])
        except ValueError:
            args[0] = regs[args[0]]
        pc_diff = args[1] if args[0] > 0 else 1
    return pc_diff


if __name__ == "__main__":
    lines = list()
    with open("input18", "r") as f:
        for line in f:
            lines.append(line[:-1])

    # test
    instruction_list_test = list()
    instruction_list_test.append("set a 1")
    instruction_list_test.append("add a 2")
    instruction_list_test.append("mul a a")
    instruction_list_test.append("mod a 5")
    instruction_list_test.append("snd a")
    instruction_list_test.append("set a 0")
    instruction_list_test.append("rcv a")
    instruction_list_test.append("jgz a -1")
    instruction_list_test.append("set a 1")
    instruction_list_test.append("jgz a -2")

    # test activation
    # lines = instruction_list_test

    # create register used
    reg_list = dict()
    for instr in lines:
        reg = instr.split()[1]
        if reg not in reg_list:
            reg_list[reg] = 0

    freq = [0]
    pc = 0
    while pc in range(0,len(lines)):
        cmd, args = lines[pc].split(' ', 1)

        pc += step(reg_list, cmd, args, freq)

    print(freq[-1])

    # test
    instruction_list_test = list()
    instruction_list_test.append("snd 1")
    instruction_list_test.append("snd 2")
    instruction_list_test.append("snd p")
    instruction_list_test.append("rcv a")
    instruction_list_test.append("rcv b")
    instruction_list_test.append("rcv c")
    instruction_list_test.append("rcv d")

    # test activation
    # lines = instruction_list_test

    # part2
    # create register used
    reg_list0 = dict()
    for instr in lines:
        reg = instr.split()[1]
        if not reg.isdecimal() and reg not in reg_list0:
            reg_list0[reg] = 0

    # create register 2 used
    reg_list1 = dict()
    for instr in lines:
        reg = instr.split()[1]
        if not reg.isdecimal() and reg not in reg_list1:
            reg_list1[reg] = 0
    reg_list1['p'] = 1

    freq0 = list()
    freq1 = list()
    pc0 = 0
    pc1 = 0
    count_send1 = 0
    while pc0 in range(0,len(lines)) and pc1 in range(0,len(lines)):
        cmd0, args0 = lines[pc0].split(' ', 1)
        cmd1, args1 = lines[pc1].split(' ', 1)

        inc_pc0 = step2(reg_list0, cmd0, args0, freq0, freq1)
        prev_len = len(freq0)
        inc_pc1 = step2(reg_list1, cmd1, args1, freq1, freq0)
        cur_len = len(freq0)
        if cur_len == prev_len + 1:
            count_send1 += 1

        if inc_pc0 == 0 and inc_pc1 == 0:
            # deadlock !
            break
        else:
            pc0 += inc_pc0
            pc1 += inc_pc1

    print(count_send1)
