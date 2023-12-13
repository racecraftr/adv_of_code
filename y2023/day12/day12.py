from functools import cache # cache stuff

# read the file.
with open("y2023/day12/input.txt", "r") as file:
    data = file.read().strip()

# get the tuples of strings and numbers.
RECORDS = [
    (x, tuple(map(int, y.split(","))))
    for row in data.split("\n")
    for x, y in [row.split(" ")]
]

# dp function. it caches values based on the inputs to make it easier.
@cache
def dp(i, j, cur, seq, nums):
    # if the main index is the length of the current sequence it is searching
    if i == len(seq):
        # return if j is at the last number to consider
        # and the number at j is the current number

        # or if j is equal to the length of the considered numbers list
        # and the current number is 0.
        return (j == len(nums) - 1 and nums[j] == cur) or (j == len(nums) and cur == 0)

    # result
    res = 0

    # if the character at i could be a #:
    if seq[i] in "#?":
        # add recursion stuff: increment i and cur.
        res += dp(i + 1, j, cur + 1, seq, nums)

    # if the character could be a .:
    if seq[i] in ".?":

        # if the current number is 0:
        if cur == 0:
            # add dp with the index incremented by one,
            # and set cur to 0.
            res += dp(i + 1, j, 0, seq, nums)
        # else if other stuff:
        elif cur > 0 and j < len(nums) and nums[j] == cur:
            # add dp with i and j incremented by one,
            # and set cur to 0.
            res += dp(i + 1, j + 1, 0, seq, nums)
    # just return 0 if none of this shit applies.
    return res


def part_one():
    return sum(dp(0, 0, 0, seq, nums) for seq, nums in RECORDS)


def part_two():
    unfolded = [
        ("?".join(seq for _ in range(5)), tuple(nums * 5)) for seq, nums in RECORDS
    ]
    return sum(dp(0, 0, 0, seq, nums) for seq, nums in unfolded)


print(f"Part 1: {part_one()}")  # 7670
print(f"Part 2: {part_two()}")  # 157383940585037