lines = open('2023/day2/input.txt', 'r').readlines()

def set_is_possible(set: str):
    init = {
        'r': 12,
        'g': 13,
        'b': 14,
    }
    for cubes in set.replace(" ", '').split(','):
        # print(f'\t{cubes[:-1]}')
        c_type = cubes[-1]
        num = int(cubes[:-1])
        if init[c_type] - num < 0:
            return False
    return True

def part_1():
    res = 0
    for i in range(len(lines)):
        ln = lines[i][:-1]
        ln = ln.replace(" ", "")
        ln = ln.replace("red", "r")
        ln = ln.replace('green', 'g')
        ln = ln.replace('blue', 'b')
        [_, game] = ln.split(":")
        # print(f'line:{i + 1}')
        game_ok = True
        sets = game.split(";")
        for set in sets:
            # print(set)
            if not set_is_possible(set):
                game_ok = False
                break
        if game_ok:
            # print('\t works')
            res += (i + 1)
    print(res)

def min_required(sets: list[str]) -> int:
    res_map = {
        'r': 0,
        'g': 0,
        'b': 0,
    }
    for set in sets:
        for cubes in set.replace(' ', '').split(','):
            c_type = cubes[-1]
            num = int(cubes[:-1])
            if num > res_map[c_type]:
                res_map[c_type] = num

    res = 1
    for k in res_map:
        res *= res_map[k]
    return res



def part_2():
    res = 0
    for i in range(len(lines)):
        ln = lines[i][:-1]
        ln = ln.replace(" ", "")
        ln = ln.replace("red", "r")
        ln = ln.replace('green', 'g')
        ln = ln.replace('blue', 'b')
        [_, game] = ln.split(":")

        sets = game.split(';')
        res += min_required(sets)
    print(res)

if __name__ == '__main__':
    part_2()