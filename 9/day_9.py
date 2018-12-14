from collections import deque, defaultdict

PLAYERS = 462
LAST_MARBLE = 7193800


def play(max_players, last_marble):
    circle = deque([0])
    players = defaultdict(int)

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            players[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(players.values()) if players else 0


print('Part 1:', play(PLAYERS, LAST_MARBLE))
