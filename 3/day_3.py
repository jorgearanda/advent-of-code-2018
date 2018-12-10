from collections import namedtuple

Claim = namedtuple('Claim', ['id', 'left', 'top', 'width', 'height'])
size = 1000
fabric = [
    [0 for _ in range(size)]
    for _ in range(size)
]


def parse_claim(claim):
    fields = claim.strip().split()
    coords = fields[2].split(',')
    sizes = fields[3].split('x')
    return Claim(
        id=int(fields[0][1:]),
        left=int(coords[0]),
        top=int(coords[1][:-1]),
        width=int(sizes[0]),
        height=int(sizes[1])
    )


def set_claim_square(claim):
    global fabric
    for i in range(claim.width):
        for j in range(claim.height):
            fabric[claim.left + i][claim.top + j] += 1


def count_conflicts():
    conflicts = 0
    for i in range(size):
        for j in range(size):
            if fabric[i][j] > 1:
                conflicts += 1
    return conflicts


def overlaps(claim):
    for i in range(claim.width):
        for j in range(claim.height):
            if fabric[claim.left + i][claim.top + j] != 1:
                return True
    return False


claims = [parse_claim(claim) for claim in open('input-03.txt', 'r')]
for claim in claims:
    set_claim_square(claim)

print('Part 1:', count_conflicts())

for claim in claims:
    if not overlaps(claim):
        print('Part 2:', claim.id)
        break
