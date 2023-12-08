import math


def get_lists() -> tuple[list[int], list[int]]:
    lines = open('y2023/day6/input.txt').readlines()
    [time_str, dist_str] = lines
    return (
        [int(s) for s in time_str.split()[1:]],
        [int(s) for s in dist_str.split()[1:]],
    )


'''
how to solve part 1:
basically, the calculation for d with time constraint t
x(t - x) >= d
where x is the number of milliseconds pressed
tx - x^2 = d
-x^2 + tx - d >= 0
x^2 - tx + d >= 0

find its roots and find all integers in that range.
x = (t + √(t^2 - 4d)) / 2 -> f(x) = 0

then, just subtract them.

how to solve part 2: the same thing
'''


def winning_races(time: int, dist: int):
    root1 = (time +((time**2 - 4*dist)**0.5))/2
    root2 = (time -((time**2 - 4*dist)**0.5))/2
    return math.floor(root1)-math.ceil(root2) + 1


def part_1():
    times, dists = get_lists()
    assert len(times) == len(dists)

    res = 1
    for i in range(len(times)):
        n = times[i]
        d = dists[i]
        res *= winning_races(n, d)
    print(res)


def part_2():
    times, dists = get_lists()
    big_time = int(''.join([str(t) for t in times]))
    big_dist = int(''.join([str(d) for d in dists]))
    print(winning_races(big_time, big_dist))


if __name__ == '__main__':
    part_1()
