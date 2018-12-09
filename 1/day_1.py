freq_deltas = [int(freq_delta) for freq_delta in open('input-01.txt', 'r')]


def find_first_repeated():
    seen_freqs = {0}
    current_freq = 0
    while True:
        for freq_delta in freq_deltas:
            current_freq += freq_delta
            if current_freq in seen_freqs:
                return current_freq
            seen_freqs.add(current_freq)


print('Part 1: ', sum(freq_deltas))
print('Part 2: ', find_first_repeated())
