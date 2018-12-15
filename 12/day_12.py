start = '#...#..###.#.###.####.####.#..#.##..#..##..#.....#.#.#.##.#...###.#..##..#.##..###..#..##.#..##...'
rules = {
    '...#.': '#',
    '#..##': '#',
    '.....': '.',
    '##.##': '.',
    '.##..': '#',
    '.##.#': '.',
    '####.': '#',
    '.#.#.': '.',
    '..#.#': '.',
    '.#.##': '.',
    '.#..#': '.',
    '##...': '#',
    '#...#': '#',
    '#####': '.',
    '#.###': '#',
    '..###': '#',
    '###..': '.',
    '#.#.#': '#',
    '##..#': '#',
    '..#..': '#',
    '.####': '.',
    '#.##.': '.',
    '....#': '.',
    '...##': '.',
    '#....': '.',
    '#..#.': '.',
    '..##.': '.',
    '###.#': '#',
    '#.#..': '#',
    '##.#.': '#',
    '.###.': '.',
    '.#...': '.'
}
generations = 110
offset = generations * 3
state = '.' * offset + start + '.' * offset


def get_total(state):
    total = 0
    for index, pot in enumerate(state):
        if pot == '#':
            total += index - offset

    return total


total = get_total(state)
for gen in range(generations):
    new_state = '..'
    for index in range(2, len(state) - 2):
        condition = state[index - 2:index + 3]
        new_state += rules[condition]
    new_state += '..'
    state = new_state
    new_total = get_total(state)
    print(gen, new_total, new_total - total)
    total = new_total

# Equilibrium of +22 at the 94th iteration
print(49999999900 * 22 + 2675)
