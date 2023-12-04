import fileinput

from collections import defaultdict


class Day3:
    def __init__(self) -> None:
        self.grid: list[list[str]] = []
        self.number_found = ""
        self.adjacent_to_symbol = False

        self.adjacent_sum = 0

        for input_line in fileinput.input():
            self.grid.append(list(input_line.strip()))

        self.x_max = len(self.grid[0])
        self.y_max = len(self.grid)

        self.current_star = None

        self.part_one()
        self.part_two()

    def part_two(self):
        self.number_found = ""
        self.gears = defaultdict(list)

        for y, line in enumerate(self.grid):
            for x, chr in enumerate(line):
                if chr.isdigit():
                    self.number_found += chr
                    star = self.check_adjacent_to_star(x, y)
                    if star:
                        self.current_star = star
                    continue
                self.end_of_number_star()
            self.end_of_number_star()

        gear_sum = 0

        for lst in self.gears.values():
            if len(lst) != 2:
                continue
            gear_sum += lst[0] * lst[1]

        print(f"Part 2: {gear_sum}")

    def end_of_number_star(self):
        if not self.number_found:
            return
        if self.current_star:
            self.gears[self.current_star].append(int(self.number_found))
        self.number_found = ""
        self.current_star = None

    def check_adjacent_to_star(self, x_n, y_n) -> tuple[int, int] | None:
        for y in range(max(0, y_n - 1), min(self.y_max, y_n + 2)):
            for x in range(max(0, x_n - 1), min(self.x_max, x_n + 2)):
                if self.grid[y][x] != "*":
                    continue
                return (x, y)

        return None

    def part_one(self):
        for y, line in enumerate(self.grid):
            for x, chr in enumerate(line):
                if chr.isdigit():
                    self.number_found += chr
                    self.check_adjacent_to_symbol(x, y)
                    continue

                self.end_of_number(x, y)

            self.end_of_number(x, y)

        print(f"Part 1: {self.adjacent_sum}")

    def end_of_number(self, x: int, y: int):
        if not self.number_found:
            return

        if self.adjacent_to_symbol:
            self.adjacent_sum += int(self.number_found)

        self.number_found = ""
        self.adjacent_to_symbol = False

    def check_adjacent_to_symbol(self, x_n: int, y_n: int):
        for y in range(max(0, y_n - 1), min(self.y_max, y_n + 2)):
            for x in range(max(0, x_n - 1), min(self.x_max, x_n + 2)):
                target = self.grid[y][x]
                if not target.isdigit() and target != ".":
                    self.adjacent_to_symbol = True
                    continue


if __name__ == "__main__":
    Day3()
