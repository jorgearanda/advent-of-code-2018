def load_notes():
    return sorted([note.strip() for note in open('input-04.txt', 'r')])


def add_guard(id):
    global guards
    guards[id] = [0] * 60


def set_minutes_asleep(id, from_minute, to_minute):
    global guards
    for i in range(from_minute, to_minute):
        guards[id][i] += 1


guards = {}
notes = load_notes()

for note in notes:
    split_note = note.split()
    if 'begins shift' in note:
        curr_guard = int(split_note[3][1:])
        if curr_guard not in guards:
            add_guard(curr_guard)
    elif 'falls asleep' in note:
        from_minute = int(split_note[1][3:-1])
    elif 'wakes up' in note:
        to_minute = int(split_note[1][3:-1])
        set_minutes_asleep(curr_guard, from_minute, to_minute)

top_sleeper = max(guards, key=lambda key: sum(guards[key]))
minute = guards[top_sleeper].index(max(guards[top_sleeper]))

print('Part 1:', top_sleeper * minute)

top_sleeper = max(guards, key=lambda key: max(guards[key]))
minute = guards[top_sleeper].index(max(guards[top_sleeper]))

print('Part 2:', top_sleeper * minute)
