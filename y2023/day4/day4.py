import re

lines = open('y2023/day4/input.txt').readlines()

def parse_line(ln: str) -> (set[int], list[int]):
    [_, data] = re.split(r'\: +', ln, 1)
    data = data.strip()
    [winning, yours] = data.split(' | ', 1)
    winning = winning.strip()
    yours = yours.strip()
    return (
        {int(num) for num in re.split(r' +', winning)},
        [int(num) for num in re.split(r' +', yours)]
    )

def get_num_matched(ln: str):
    winning, yours = parse_line(ln)
    return len([i for i in yours if i in winning])

def part_1():
    res = 0
    for ln in lines:
        num_matched = get_num_matched(ln)
        res += 0 if num_matched < 1 else 1 << (num_matched - 1)
    print(res)


def part_2():
    cards = [1] * len(lines)
    for i, ln in enumerate(lines):
        winning, yours = parse_line(ln)
        n = len([x for x in yours if x in winning])
        for j in range(i + 1, min(i + 1 + n, len(lines))):
            cards[j] += cards[i]
    print(sum(cards))

if __name__ == '__main__':
    part_2()