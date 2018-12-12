from string import ascii_lowercase, ascii_uppercase


def load_polymer():
    return [polymer.strip() for polymer in open('input-05.txt', 'r')][0]


def get_reductions():
    reductions = []
    for lower, upper in zip(ascii_lowercase, ascii_uppercase):
        reductions.extend([lower + upper, upper + lower])
    return reductions


def reduce(polymer):
    poly_length = len(polymer)
    while True:
        for reduction in get_reductions():
            polymer = polymer.replace(reduction, '')

        if len(polymer) == poly_length:
            return polymer

        poly_length = len(polymer)


polymer = load_polymer()
first_reduction = reduce(polymer)
print('Part 1:', len(first_reduction))

shortest = len(first_reduction)
for unit in ascii_lowercase:
    candidate = first_reduction.replace(unit, '')
    candidate = candidate.replace(unit.upper(), '')
    reduced_candidate = reduce(candidate)
    shortest = min(shortest, len(reduced_candidate))

print('Part 2:', shortest)
