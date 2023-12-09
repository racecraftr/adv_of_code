lines = open('y2023/day9/input.txt').readlines()

def get_ls(ln: str) -> list[int]:
    return [int(s) for s in ln.split()]

def find_history(lists: list[list[int]]) -> list[list[int]]:
    most_recent = lists[-1][:]

    if not any(most_recent):
        return lists

    new_lists = lists[:]

    new_history = []
    for i in range(0, len(most_recent) - 1):
        new_history.append(most_recent[i + 1] - most_recent[i])
    new_lists.append(new_history)
    return find_history(new_lists)

def add_history(history: list[list[int]]) -> list[list[int]]:
    res = 0
    for ls in history:
        res += ls[-1]
    return res


def part_1():
    res = 0
    for ln in lines:
        ls = get_ls(ln)
        history = find_history([ls])
        last = add_history(history)
        res += last
    print(res)

def sub_history(history: list[list[int]]) -> list[list[int]]:
    res = 0
    for ls in history:
        res = ls[0] - res
    return res

def part_2():
    res = 0
    for ln in lines:
        ls = get_ls(ln)
        history = find_history([ls])
        first = sub_history(history)
        print(f'{res} + {first} = {res + first}')
        res += first
    print(res)

def part_2_test():
    ln = '5 13 45 115 234 420 731 1329 2591 5314 11131 23388 48974 102035 211293 434077 882526 1771333 3502944 6817585 13056927'
    ls = get_ls(ln)
    history = find_history([ls])
    for h in history:
        print(h)
    first = sub_history(history)
    print(first)


if __name__ == '__main__':
    part_2()