import itertools


def update_particles(all_particles):
    for particle in all_particles:
        particle['v'][0] += particle['a'][0]
        particle['v'][1] += particle['a'][1]
        particle['v'][2] += particle['a'][2]

        particle['p'][0] += particle['v'][0]
        particle['p'][1] += particle['v'][1]
        particle['p'][2] += particle['v'][2]


def check_collisions(all_particles):
    list_of_particle_colisions = list()
    for particle1, particle2 in itertools.combinations(all_particles, 2):
        if particle1['p'] == particle2['p']:
            if particle1 not in list_of_particle_colisions:
                list_of_particle_colisions.append(particle1)
            if particle2 not in list_of_particle_colisions:
                list_of_particle_colisions.append(particle2)
    for particle in list_of_particle_colisions:
        all_particles.remove(particle)


if __name__ == "__main__":
    lines = list()
    all_particles = list()
    with open("input20", "r") as f:
        for line in f:
            lines.append(line[:-1])

            p, v, a = line.split()
            p = [int(x) for x in p.split('>')[0].split('<')[1].split(',')]
            v = [int(x) for x in v.split('>')[0].split('<')[1].split(',')]
            a = [int(x) for x in a.split('>')[0].split('<')[1].split(',')]
            all_particles.append({'p': p, 'v': v, 'a': a})

    # just look for the minimum acceleration
    min_accel = 99999
    min_accel_idx = 0
    for idx, particle in enumerate(all_particles):
        accel_amplitude = sum(map(abs, particle['a']))
        if accel_amplitude < min_accel:
            min_accel = accel_amplitude
            min_accel_idx = idx

    print("Part1: ", min_accel_idx)

    for i in range(0,100):
        update_particles(all_particles)
        check_collisions(all_particles)
        print(i, len(all_particles))
    print("Part2: ", len(all_particles))