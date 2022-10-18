from utils import slurp, unpack
import re

filedata = unpack(slurp("06.txt"))


def box(x1, y1, x2, y2):
    coords = set()
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            coords.add((x, y))
    return coords


def parse_instruction(instruction):
    m = re.match(r"(.+)\s(\d+),(\d+) through (\d+),(\d+)", instruction)
    ins = m.group(1)
    x1, y1 = int(m.group(2)), int(m.group(3))
    x2, y2 = int(m.group(4)), int(m.group(5))
    return ins, x1, y1, x2, y2


def part1(instructions):
    grid = [0] * 1000 * 1000
    for instruction in instructions:
        ins, x1, y1, x2, y2 = parse_instruction(instruction)
        if ins == "turn on":
            for x, y in box(x1, y1, x2, y2):
                grid[x + y * 1000] = 1
        elif ins == "turn off":
            for x, y in box(x1, y1, x2, y2):
                grid[x + y * 1000] = 0
        elif ins == "toggle":
            for x, y in box(x1, y1, x2, y2):
                grid[x + y * 1000] = (grid[x + y * 1000] + 1) & 1
        else:
            assert False, ins
    return sum(grid)


def part2(instructions):
    grid = [0] * 1000 * 1000
    for instruction in instructions:
        ins, x1, y1, x2, y2 = parse_instruction(instruction)
        if ins == "turn on":
            for x, y in box(x1, y1, x2, y2):
                grid[x + y * 1000] += 1
        elif ins == "turn off":
            for x, y in box(x1, y1, x2, y2):
                if grid[x + y * 1000] > 0:
                    grid[x + y * 1000] -= 1
        elif ins == "toggle":
            for x, y in box(x1, y1, x2, y2):
                grid[x + y * 1000] += 2
        else:
            assert False, ins
    return sum(grid)


print("#--- Day 6: Probably a Fire Hazard: part1:", end=" ")
assert (
    part1(
        [
            "turn on 0,0 through 999,999",
            "toggle 0,0 through 999,0",
            "turn off 499,499 through 500,500",
        ]
    )
    == 1000000 - 1000 - 4
)
print(part1(filedata))

print("#--- Day 6: Probably a Fire Hazard: part2:", end=" ")
assert (
    part2(
        [
            "turn on 0,0 through 0,0",
            "toggle 0,0 through 999,999",
        ]
    )
    == 2000000 + 1
)
print(part2(filedata))
