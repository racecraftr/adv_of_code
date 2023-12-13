content = open('y2023/day13/input.txt', 'r').read()

def str_to_num(s: str) -> int:
    res = 0
    for c in s:
        res |= (1 if c == '#' else 0)
        res <<= 1
    return res >> 1

def get_grids() -> list[str]:
    return [grid for grid in content.split('\n\n')]

def parse_grid(grid: str) -> tuple[list[int], list[int]]:
    rows = [row for row in grid.split('\n')]
    cols = [col for col in list(zip(*grid.split('\n')))]

    return ([str_to_num(row) for row in rows], [str_to_num(col) for col in cols])

# [1, 2, 2, 1, 3]
# we need to only get the subarray [1, 2, 2, 1].
"""
[   1,  2,  2,  1,  3   ] len = 5
        i   i+1
i + 1           = 2
5 - (i + 1)     = 3
min_len = 2
subarrays to compare:
    [i + 1 - min_len : i + 1] = [0:2]                       -> [1, 2]
    [i + 1 : i + 1 + min_len].rev = [2:4].rev -> [2, 1].rev -> [1, 2]
"""

#############################################
# ------------- P A R T   1 --------------- #
#############################################
def find_reflection(ls: list[int]) -> int:
    for i in range(len(ls) - 1):
        n1, n2 = ls[i], ls[i + 1]
        if n1 == n2 :
            min_len = min(i + 1, len(ls) - (i + 1))
            sub_1 = ls[i+1 - min_len :i+1]
            sub_2 = ls[i + 1: i+1 + min_len]
            sub_2.reverse()
            if sub_1 == sub_2:
                return i + 1
    return 0

def part_1():
    grids = get_grids()
    res = 0
    for grid in grids:
        rows, cols = parse_grid(grid)
        res += find_reflection(rows) * 100 + find_reflection(cols)
    print(res)
#############################################
# ------------- P A R T   2 --------------- #
#############################################
def hamming_distance(a: int, b: int) -> int:
    x = a ^ b
    set_bits = 0

    while (x > 0) :
        set_bits += x & 1
        x >>= 1

    return set_bits

def find_reflection_2(ls: list[int]) -> int:
    for i in range(len(ls) - 1):
        # n1, n2 = ls[i], ls[i + 1]
        # if hamming_distance(n1, n2) <= 1:
        min_len = min(i + 1, len(ls) - (i + 1))
        sub_1 = ls[i+1 - min_len :i+1]
        sub_2 = ls[i + 1: i+1 + min_len]
        sub_2.reverse()
        if sum(list(map(hamming_distance, sub_1, sub_2))) == 1:
            return i + 1

    return 0

def part_2():
    grids = get_grids()
    res = 0
    for grid in grids:
        rows, cols = parse_grid(grid)
        res += find_reflection_2(rows) * 100 + find_reflection_2(cols)
    print(res)

if __name__ == '__main__':
    part_2()