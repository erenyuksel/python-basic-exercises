def count_repetition(names):
    counts = {}
    for name in names:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    return counts


names = ['kerouac', 'fante', 'fante', 'buk', 'hemingway', 'hornby', 'kerouac', 'buk', 'fante']

print(count_repetition(names))