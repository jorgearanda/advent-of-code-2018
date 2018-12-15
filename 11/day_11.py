def calc_power_level(serial):
    field = [[0] * 300 for _ in range(300)]
    for i in range(300):
        rack_id = i + 11
        for j in range(300):
            cell = j + 1
            field[i][j] = ((rack_id * cell + serial) * rack_id) % 1000 // 100 - 5

    return field


def find_max_power(field):
    max_power = -100
    max_coords = (-1, -1)
    for s in range(3, 301):
        print('Evaluating size', s, 'max power so far', max_power, 'coords', max_coords)
        for i in range(300 - s):
            for j in range(300 - s):
                power = sum([sum(field[x][j:j + s]) for x in range(i, i + s)])
                if power > max_power:
                    max_power = power
                    max_coords = (i + 1, j + 1)

    return max_coords, max_power, size


field = calc_power_level(9424)
print(find_max_power(field))
