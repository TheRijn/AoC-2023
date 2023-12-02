import fileinput

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

games = []


for line in fileinput.input():
    line = line.strip()
    _, rest = line.split(":")
    grabs = rest.split(";")
    numbers: dict[str, int] = {"red": 0, "green": 0, "blue": 0}

    for grab in grabs:
        cubes = grab.split(",")

        for cube in cubes:
            number, colour = cube.strip().split(" ")
            numbers[colour] = max(numbers[colour], int(number))

    games.append(numbers)

total = 0
power_total = 0

for i, game in enumerate(games):
    if (
        game["red"] <= MAX_RED
        and game["green"] <= MAX_GREEN
        and game["blue"] <= MAX_BLUE
    ):
        total += i + 1

    power_total += game["red"] * game["green"] * game["blue"]

print(f"Part 1: {total}")
print(f"Part 2: {power_total}")
