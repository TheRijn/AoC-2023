import fileinput

total = 0
card_count = []

matches = []

for line in fileinput.input():
    _, numbers = line.strip().split(":")
    winning, having = [set(x.split()) for x in numbers.split("|")]
    match = len(winning & having)

    if match != 0:
        total += 2 ** (match - 1)

    card_count.append(1)
    matches.append(match)

for i, match in enumerate(matches):
    current_card_count = card_count[i]

    for j in range(match):
        card_count[i + j + 1] += current_card_count

print(f"Part 1: {total}")
print(f"Part 2: {sum(card_count)}")
