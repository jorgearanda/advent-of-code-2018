from collections import namedtuple

Vector = namedtuple('Vector', ['position', 'velocity'])


def parse_vector(raw_vector):
    return Vector(
        position=[int(raw_vector[10:16]), int(raw_vector[18:24])],
        velocity=[int(raw_vector[36:38]), int(raw_vector[40:42])]
    )


def load():
    return [parse_vector(v) for v in open('input.txt', 'r')]


def plot(field):
    for row in field:
        line = ''
        for cell in row:
            if cell is None:
                line += '.'
            else:
                line += '#'
        print(line)


def bounds(vectors):
    top = min(vectors, key=lambda vector: vector.position[1]).position[1]
    bottom = max(vectors, key=lambda vector: vector.position[1]).position[1]
    left = min(vectors, key=lambda vector: vector.position[0]).position[0]
    right = max(vectors, key=lambda vector: vector.position[0]).position[0]

    return top, bottom, left, right


def make_field(vectors):
    top, bottom, left, right = bounds(vectors)
    field = [[None] * (right + 1 - left) for _ in range(bottom + 1 - top)]
    for vector in vectors:
        field[vector.position[1] - top][vector.position[0] - left] = True

    return field


def tick(vectors):
    for vector in vectors:
        vector.position[0] += vector.velocity[0]
        vector.position[1] += vector.velocity[1]

    return vectors


vectors = load()

# The following is to figure out which moment has the smallest box area;
# it is now commented to actually show the message
#
# min_area = 1000000000
# for i in range(100000):
#     top, bottom, left, right = bounds(vectors)
#     area = (bottom - top) * (right - left)
#     if area < min_area:
#         print('Area', area, 'moment', i)
#         min_area = area
#     vectors = tick(vectors)

for i in range(10932):
    vectors = tick(vectors)

field = make_field(vectors)
plot(field)
