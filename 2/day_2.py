ids = [id for id in open('input-02.txt', 'r')]


def has_a_letter_repeated(id, reps):
    for letter in id:
        if id.count(letter) == reps:
            return 1
    return 0


def are_similar(first, second):
    diffs = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            diffs += 1
        if diffs > 1:
            return False
    return True


def fragments_in_common(first, second):
    id = ''
    for i in range(len(first)):
        if first[i] == second[i]:
            id += first[i]
    return id


with_two = sum([has_a_letter_repeated(id, 2) for id in ids])
with_three = sum([has_a_letter_repeated(id, 3) for id in ids])

print('Part 1: ', with_two * with_three)

for i in range(len(ids)):
    for j in range(i + 1, len(ids)):
        if are_similar(ids[i], ids[j]):
            print('Part 2: ', fragments_in_common(ids[i], ids[j]))
            break
