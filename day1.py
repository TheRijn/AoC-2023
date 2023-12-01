import fileinput

total1 = 0
total2 = 0


def find_number(line: str) -> int|None:
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for number, integer in numbers.items():
        if line.startswith(number):
            return integer

    return None


for line in fileinput.input():
    digits1: list[str] = []
    digits2: list[int|str] = []

    for i, char in enumerate(line.strip()):
        if char.isdigit():
            digits1.append(char)
            digits2.append(char)
        else:
            if digit := find_number(line[i:]):
                digits2.append(digit)

    total1 += int(f"{digits1[0]}{digits1[-1]}")
    total2 += int(f"{digits2[0]}{digits2[-1]}")


print(f"Part 1: {total1}")
print(f"Part 2: {total2}")
