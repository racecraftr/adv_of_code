import re


class Solution:
    input: str
    data: list
    re = re.compile(r'\d+')

    def __init__(self) -> None:
        with open(f'y2023/day3/input.txt') as f:
            self.input = f.read()
        self.data = self.input.strip().split('\n')

    def find_numbers(self, line: str):
        end = 0
        while m := self.re.search(line, end):
            start = max(m.start() - 1, 0)
            end = m.end() + 1
            yield start, min(end, len(line) - 1), int(m[0])

    def has_symbol(self, y: int, start: int, end: int, check):
        """Checks if the number has any symbols adjacent to it"""
        return [
            f"{x + start}-{ln}"  # a list of strings
            # for each line number in a range
            for ln in [max(y - 1, 0), y, min(y + 1, len(self.data) - 1)]
            for x, char in enumerate(self.data[ln][start:end])  # for each line
            if check(char)  # if the check function is correct
        ]

    def part_1(self):
        return sum(  # the sum of
            number  # numbers
            # for (y coordianate, line content) in data
            for y, line in enumerate(self.data)
            # for the start, end, and content of each number
            for start, end, number in self.find_numbers(line)
            # if any digit in the number is next to a valid symbol
            if any(self.has_symbol(y, start, end, lambda c: c not in '1234567890.'))
        )

    def part_2(self):
        numbers = [
            (number, coord)
            for y, line in enumerate(self.data)
            for start, end, number in self.find_numbers(line)
            for coord in self.has_symbol(y, start, end, lambda c: c == '*')
        ]

        checked = []

        def append(c, number):
            checked.append(c)
            return number

        result = [
            append(c1, n1 * n2)
            for i, (n1, c1) in enumerate(numbers)
            for j, (n2, c2) in enumerate(numbers)
            if c1 not in checked and c1 == c2 and j != i
        ]

        return sum(result)


if __name__ == "__main__":
    s = Solution()
    print(f"AOC y2023 Day 3 Part 1: {s.part_1()}")
    print(f"AOC y2023 Day 3 Part 2: {s.part_2()}")
