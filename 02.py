from utils import slurp
import re

filedata = slurp("02.txt")


def part1(dimensions):
    for dimension in dimensions.split("\n"):
        m = re.match(r"^(\d+)x(\d+)x(\d+)", dimension)
        x, y, z = int(m.group(1)), int(m.group(2)), int(m.group(3))
        sides = [x * y, x * z, y * z]
        yield 2 * sum(sides) + min(sides)


def part2(dimensions):
    for dimension in dimensions.split("\n"):
        m = re.match(r"^(\d+)x(\d+)x(\d+)", dimension)
        x, y, z = int(m.group(1)), int(m.group(2)), int(m.group(3))
        perimeters = [2 * (x + y), 2 * (x + z), 2 * (y + z)]
        volume = x * y * z
        yield min(perimeters) + volume


print("#--- Day 2: I Was Told There Would Be No Math: part1:", end=" ")

assert sum(part1("2x3x4")) == 58
assert sum(part1("1x1x10")) == 43
print(sum(part1(filedata)))

print("#--- Day 2: I Was Told There Would Be No Math: part2:", end=" ")

assert sum(part2("2x3x4")) == 34
assert sum(part2("1x1x10")) == 14
print(sum(part2(filedata)))
