from string import ascii_uppercase


def load():
    return [line for line in open('input.txt', 'r')]


def get_tracks(state):
    tracks = []
    for row in state:
        line = ''
        for cell in row[:-1]:
            if cell not in 'v^<>':
                line += cell
            elif cell in 'v^':
                line += '|'
            else:
                line += '-'
        tracks.append(line)

    return tracks


def set_carts(state):
    carts = {}
    new_state = []
    letter = iter(ascii_uppercase)
    for i, row in enumerate(state):
        line = ''
        for j, cell in enumerate(row[:-1]):
            if cell not in 'v^<>':
                line += cell
            else:
                id = next(letter)
                line += id
                carts[id] = {
                    'orientation': cell,
                    'turn': 'left',
                    'x': j,
                    'y': i,
                }
        new_state.append(line)

    return carts, new_state


def is_collision(id, carts):
    for cart in carts:
        if cart != id and carts[cart]['x'] == carts[id]['x'] and carts[cart]['y'] == carts[id]['y']:
            return cart

    return False


def tick():
    global carts
    sorted_carts = sorted(carts, key=lambda c: (carts[c]['y'], carts[c]['x']))
    remove = []
    for id in sorted_carts:
        cart = carts[id]
        if cart['orientation'] == 'v':
            cart['y'] += 1
        elif cart['orientation'] == '^':
            cart['y'] -= 1
        elif cart['orientation'] == '<':
            cart['x'] -= 1
        elif cart['orientation'] == '>':
            cart['x'] += 1

        collision = is_collision(id, carts)
        if collision:
            print('Collision at', cart['x'], cart['y'])
            remove.append(id)
            remove.append(collision)

        target_track = tracks[cart['y']][cart['x']]
        if target_track == '/':
            if cart['orientation'] == 'v':
                cart['orientation'] = '<'
            elif cart['orientation'] == '^':
                cart['orientation'] = '>'
            elif cart['orientation'] == '<':
                cart['orientation'] = 'v'
            else:
                cart['orientation'] = '^'
        elif target_track == '\\':
            if cart['orientation'] == 'v':
                cart['orientation'] = '>'
            elif cart['orientation'] == '^':
                cart['orientation'] = '<'
            elif cart['orientation'] == '<':
                cart['orientation'] = '^'
            else:
                cart['orientation'] = 'v'
        elif target_track == '+':
            if cart['turn'] == 'left':
                cart['orientation'] = left[cart['orientation']]
                cart['turn'] = 'straight'
            elif cart['turn'] == 'right':
                cart['orientation'] = right[cart['orientation']]
                cart['turn'] = 'left'
            else:  # straight
                cart['turn'] = 'right'

    for id in remove:
        carts.pop(id)

    if len(carts) == 1:
        print('Last cart', carts)
        return True
    else:
        print('Carts left', len(carts))

    return False


initial = load()
tracks = get_tracks(initial)
carts, state = set_carts(initial)
left = {
    'v': '>',
    '>': '^',
    '^': '<',
    '<': 'v'
}
right = {
    'v': '<',
    '<': '^',
    '^': '>',
    '>': 'v'
}

while True:
    if tick():
        break
