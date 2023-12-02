lines = open('2023/day1/day1.txt', 'r').readlines() # change this to be the path relative to the project directory


def part_1():
    res = 0
    for ln in lines:
        for c in ln:
            if ord('0') <= ord(c) <= ord('9'):
                res += 10 * int(c)
                break
        for c in ln[::-1]:
            if ord('0') <= ord(c) <= ord('9'):
                res += int(c)
                break
    print(res)


def part_2():
    numset = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    res = 0
    for ln in lines:
        first = 0
        first_idx = len(ln) + 1

        last = 0
        last_idx = -1
        for num in numset:
            idx = ln.find(num)
            if 0 <= idx < first_idx:
                first_idx = idx
                first = numset[num] * 10
            idx = ln.rfind(num)
            if idx >= last_idx:
                last_idx = idx
                last = numset[num]
        res += first + last
    print(res)


if __name__ == '__main__':
    part_2()
