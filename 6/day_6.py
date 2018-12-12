def load_coords():
    return [
        tuple(map(int, coord.strip().split(', ')))
        for index, coord in enumerate(open('input.txt', 'r'))
    ]


def min_x(coords):
    return min(coords, key=lambda coord: coord[0])[0]


def min_y(coords):
    return min(coords, key=lambda coord: coord[1])[1]


def max_x(coords):
    return max(coords, key=lambda coord: coord[0])[0]


def max_y(coords):
    return max(coords, key=lambda coord: coord[1])[1]


def populate_coords_in_field():
    global field
    for index, coord in enumerate(coords):
        field[coord[0] - x_offset][coord[1] - y_offset] = index


def distance_to_coord(coord, cell):
    return abs(coord[0] - x_offset - cell[0]) + \
        abs(coord[1] - y_offset - cell[1])


def populate_cells_in_field():
    global field
    for i in range(len(field)):
        for j in range(len(field[i])):
            cell = [i, j]
            closest = 1000000
            closest_coord = None
            for id, coord in enumerate(coords):
                if distance_to_coord(coord, cell) < closest:
                    closest_coord = id
                    closest = distance_to_coord(coord, cell)
                elif distance_to_coord(coord, cell) == closest:
                    closest_coord = None
            field[i][j] = closest_coord


def populate_cells_in_safe_field():
    global safe_field
    for i in range(len(field)):
        for j in range(len(field[i])):
            cell = [i, j]
            total_distance = 0
            for coord in coords:
                total_distance += distance_to_coord(coord, cell)
            if total_distance < 10000:
                safe_field[i][j] = True


coords = load_coords()
field = [
    [None for i in range(min_y(coords), max_y(coords) + 1)]
    for j in range(min_x(coords), max_x(coords) + 1)
]

x_offset = min_x(coords)
y_offset = min_y(coords)

populate_coords_in_field()
populate_cells_in_field()

candidates = set(id for id in range(len(coords)))
for i in range(len(field)):
    if field[i][0] in candidates:
        candidates.remove(field[i][0])
    if field[i][-1] in candidates:
        candidates.remove(field[i][-1])
for j in range(len(field[0])):
    if field[0][j] in candidates:
        candidates.remove(field[0][j])
    if field[-1][j] in candidates:
        candidates.remove(field[-1][j])

biggest = 0
for candidate in candidates:
    candidate_area = sum(x.count(candidate) for x in field)
    biggest = max(biggest, candidate_area)

print('Part 1:', biggest)

safe_field = [
    [False for i in range(min_y(coords), max_y(coords) + 1)]
    for j in range(min_x(coords), max_x(coords) + 1)
]
populate_cells_in_safe_field()
safe_area = sum(x.count(True) for x in safe_field)
print('Part 2:', safe_area)
