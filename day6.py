import fileinput


reader = fileinput.input()
times = [int(x) for x in next(reader).strip().split(":")[1].split()]
distances = [int(x) for x in next(reader).strip().split(":")[1].split()]

total = 1

for i in range(len(times)):
    time = times[i]
    distance = distances[i]

    count = 0

    for hold in range(time):
        if (meters := (time - hold) * hold) > distance:
            count += 1

    total *= count

print(f"Part 1: {total}")

time = int("".join([str(x) for x in times]))
distance = int("".join([str(x) for x in distances]))

count = 0

for hold in range(time):
    if (meters := (time - hold) * hold) > distance:
        count += 1

print(f"Part 2: {count}")
