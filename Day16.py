import unittest
import timeit
import random, numpy


class TestDay16(unittest.TestCase):

    def test_spin(self):
        self.assertEqual(spin('abcde', 1), 'eabcd')
        self.assertEqual(spin('abcde', 2), 'deabc')
        self.assertEqual(spin('abcde', 3), 'cdeab')

    def test_exchange(self):
        self.assertEqual(exchange('eabcd', (3, 4)), 'eabdc')
        self.assertEqual(exchange('eabcd', (0, 4)), 'dabce')
        self.assertEqual(exchange('eabcd', (1, 1)), 'eabcd')

    def test_partner(self):
        self.assertEqual(partner('eabdc', ('e', 'b')), 'baedc')
        self.assertEqual(partner('eabdc', ('a', 'b')), 'ebadc')
        self.assertEqual(partner('eabdc', ('c', 'e')), 'cabde')
        self.assertEqual(partner('eabdc', ('c', 'c')), 'eabdc')


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def spin(string, length):
    return string[-length:] + string[:len(string)-length]


def exchange(string, indexes):
    a = indexes[0]
    b = indexes[1]
    if a == b:
        return string
    elif a < b:
        return string[:a] + string[b] + string[a+1:b] + string[a] + string[b+1:]
    elif a > b:
        return string[:b] + string[a] + string[b + 1:a] + string[b] + string[a + 1:]


def partner(string, indexes):
    return exchange(string, (string.index(indexes[0]), string.index(indexes[1])))


if __name__ == "__main__":
    # test
    # unittest.main()

    with open("input16", "r") as f:
        file_raw = f.read().strip()
    dance_moves = file_raw.split(',')

    if False:
        print("#"*5 + "Time perf" + "#"*5)
        programs = 'abcdefghijklmnop'
        wrapped = wrapper(spin, programs, 12)
        print('spin ', timeit.timeit(wrapped, number=1000000)/1000000)
        wrapped = wrapper(exchange, programs, (13, 3))
        print('exchange ', timeit.timeit(wrapped, number=1000000)/1000000)
        wrapped = wrapper(partner, programs, ('o', 'k'))
        print('partner ', timeit.timeit(wrapped, number=1000000)/1000000)
        print("#" * 5 + len("Time perf")*'#' + "#" * 5)
    # even with µs execution times, it needs 10.000 for 1 iteration
    # so 10^⁻2 sec for 1 iteration
    # for a billion iteration that means 10^7 sec = 116 days !

    # process input, optim for "hard" method, too slow
    action = {'s': spin, 'x': exchange, 'p': partner}
    for idx, move in enumerate(dance_moves):
        if '/' in move:
            arg = move[1:].split('/')
            if arg[0].isnumeric():
                arg = (int(arg[0]), int(arg[1]))
        else:
            arg = int(move[1:])
        dance_moves[idx] = [action[move[0]], arg]

    # start to dance:
    programs = 'abcdefghijklmnop'
    for idx, move in enumerate(dance_moves):
        programs = move[0](programs, move[1])
    part1_res = programs
    print('Part1: ', part1_res)

    # "soft" method
    # check how long to find again the same position
    programs = 'abcdefghijklmnop'
    previous_programs = list()
    while programs not in previous_programs:
        previous_programs.append(programs)
        for move in dance_moves:
            programs = move[0](programs, move[1])
    period = len(previous_programs)
    print("Period: ", period)
    print("Offset: ", 10 ** 9 % period)
    for remain in range(10**9 % period):
        for move in dance_moves:
            programs = move[0](programs, move[1])
    part2_res = programs
    print('Part2: ', part2_res)

    # find min and max period
    period_list = list()
    for i in range(1,20):
        # generate random moves
        r_gen = random.Random()
        r_gen.seed()
        for dance_move_idx in range(len(dance_moves)):
            action_choosed = r_gen.choice('sxp')
            dance_moves[dance_move_idx] = [action[action_choosed]]
            if action_choosed == 's':
                dance_moves[dance_move_idx].append(r_gen.randint(1,15))
            elif action_choosed == 'x':
                dance_moves[dance_move_idx].append((r_gen.randint(0, 15), r_gen.randint(0, 15)))
            elif action_choosed == 'p':
                dance_moves[dance_move_idx].append([r_gen.choice('abcdefghijklmnop'), r_gen.choice('abcdefghijklmnop')])

        # measure periods
        programs = 'abcdefghijklmnop'
        previous_programs = list()
        while programs not in previous_programs:
            previous_programs.append(programs)
            for move in dance_moves:
                programs = move[0](programs, move[1])
        period = len(previous_programs)
        period_list.append(period)
        for remain in range(10 ** 9 % period):
            for move in dance_moves:
                programs = move[0](programs, move[1])
        part2_res = programs

    print("period statistics on 1000 iterations:")
    print("min = ", min(period_list), " max = ", max(period_list))
    print("avg = ", numpy.average(period_list)," std = ", numpy.std(period_list))
    print(period_list)