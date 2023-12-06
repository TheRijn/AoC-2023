import fileinput

reader = fileinput.input()

seeds = [int(x) for x in next(reader).strip().split(":")[1].split()]

next(reader) # skip empty

maps: list[list[tuple[range, range]]] = []

current: list(tuple[range, range]) = []

for line in reader:
    line = line.strip()
    if line == "":
        maps.append(current)
        current = []
        continue

    if line[0].isalpha():
        continue

    dest, src, length = [int(x) for x in line.split()]
    current.append((range(src, src + length), range(dest, dest + length)))

maps.append(current)

locations = []
for seed in seeds:
    number = seed
    for lst in maps:
        for src_range, dest_range in lst:
            if number in src_range:
                number = dest_range[src_range.index(number)]
                break
    locations.append(number)

print(f"Day 1: {min(locations)}")

# Part 2
pairs = []
for i in range(0, len(seeds), 2):
    pairs.append((seeds[i], seeds[i + 1]))

locations = []

for seed_begin, seed_length in pairs:
    seed_range = range(seed_begin, seed_begin + seed_length)

    number = seed
    for lst in maps:
        for src_range, dest_range in lst:
            if number in src_range:
                number = dest_range[src_range.index(number)]
                break
    locations.append(number)

print(f"Day 2: {min(locations)}")
