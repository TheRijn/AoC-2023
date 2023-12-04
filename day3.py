import fileinput

from collections import defaultdict


class Day3:
    def __init__(self) -> None:
        self.grid: list[list[str]] = []

        for input_line in fileinput.input():
            self.grid.append(list(input_line.strip()))

        self.x_max = len(self.grid[0])
        self.y_max = len(self.grid)

        self.number_found = ""

        # Part 1
        self.adjacent_to_symbol = False
        self.adjacent_sum = 0

        # Part 2
        self.current_gear = None
        self.gears: dict[tuple[int, int], list[int]] = defaultdict(list)

        for y, line in enumerate(self.grid):
            for x, chr in enumerate(line):
                if chr.isdigit():
                    self.number_found += chr
                    gear = self.check_adjacency(x, y)
                    if gear:
                        self.current_gear = gear
                    continue
                self.end_of_number()
            self.end_of_number()

        gear_sum = 0

        for lst in self.gears.values():
            if len(lst) == 2:
                gear_sum += lst[0] * lst[1]

        print(f"Part 1: {self.adjacent_sum}")
        print(f"Part 2: {gear_sum}")

    def end_of_number(self) -> None:
        if not self.number_found:
            return

        if self.adjacent_to_symbol:
            self.adjacent_sum += int(self.number_found)

        if self.current_gear:
            self.gears[self.current_gear].append(int(self.number_found))

        self.current_gear = None
        self.number_found = ""
        self.adjacent_to_symbol = False

    def check_adjacency(self, x_adj: int, y_adj: int) -> tuple[int, int] | None:
        for y in range(max(0, y_adj - 1), min(self.y_max, y_adj + 2)):
            for x in range(max(0, x_adj - 1), min(self.x_max, x_adj + 2)):
                target = self.grid[y][x]
                if not target.isdigit() and target != ".":
                    self.adjacent_to_symbol = True
                    if target == "*":
                        return (x, y)
        return None


if __name__ == "__main__":
    Day3()
